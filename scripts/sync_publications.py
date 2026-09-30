#!/usr/bin/env python3
"""
Cytoskeleton Lab — Automated Publication Sync Script
Fetches peer-reviewed publications and preprints using the free, unblocked OpenAlex API
(author: Dr. Minhaj Sirajuddin / inStem) and automatically generates/updates HugoBlox publication pages.

Features:
- Free public API without CAPTCHA or API key requirement.
- Filters & tags: "Research Article" vs "Review".
- Categorizes by era: "inStem Era" (2015–Present) vs "Prior to inStem" (Pre-2015).
- Prevents duplication of existing publications by checking DOI and title slugs.
- Supports --dry-run to preview changes without writing to disk.

Usage:
    python scripts/sync_publications.py
    python scripts/sync_publications.py --dry-run
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.parse
import urllib.request

# Ensure UTF-8 output on Windows terminal
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

# Author configuration
AUTHOR_SEARCH = "Minhaj Sirajuddin"
OPENALEX_AUTHOR_ID = "A5071834063"  # Minhajuddin Sirajuddin (inStem)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(BASE_DIR, "content", "publication")


def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")[:60]


def normalize_doi(doi):
    if not doi:
        return ""
    doi = doi.strip().lower()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi)
    return doi.strip("/")


def get_existing_publications(pub_dir):
    """Scan existing publications to avoid overwriting or duplicating."""
    existing_dois = set()
    existing_slugs = set()

    for path in glob.glob(os.path.join(pub_dir, "*", "index.md")):
        folder_name = os.path.basename(os.path.dirname(path))
        existing_slugs.add(folder_name)

        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                # Find DOI
                m_doi = re.search(r"doi:\s*[\"']?([^\"'\r\n]+)", content)
                if m_doi:
                    clean_doi = normalize_doi(m_doi.group(1))
                    if clean_doi:
                        existing_dois.add(clean_doi)
        except Exception as e:
            print(f"[!] Warning reading {path}: {e}")

    return existing_dois, existing_slugs


def fetch_openalex_works(author_id):
    """Fetch all works for given OpenAlex author ID."""
    url = f"https://api.openalex.org/works?filter=author.id:{author_id}&per-page=100&sort=publication_year:desc"
    headers = {
        "User-Agent": "CytoskeletonLabPublicationsSync/1.0 (mailto:lab@instem.res.in)"
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data.get("results", [])
    except Exception as e:
        print(f"[-] Error querying OpenAlex API: {e}")
        return []


def main():
    parser = argparse.ArgumentParser(description="Sync publications from OpenAlex")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Simulate sync without creating any files",
    )
    parser.add_argument(
        "--force", action="store_true", help="Overwrite existing publication files"
    )
    args = parser.parse_args()

    print(
        f"[*] Starting publication sync for OpenAlex Author {OPENALEX_AUTHOR_ID} ({AUTHOR_SEARCH})..."
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    existing_dois, existing_slugs = get_existing_publications(OUTPUT_DIR)
    print(
        f"[*] Found {len(existing_slugs)} existing publication folder(s) ({len(existing_dois)} unique DOIs)."
    )

    works = fetch_openalex_works(OPENALEX_AUTHOR_ID)
    print(f"[+] Retrieved {len(works)} works from OpenAlex.")

    created_count = 0
    skipped_count = 0

    for work in works:
        title = work.get("title") or ""
        title = title.strip().replace('"', '\\"')
        if not title:
            continue

        raw_doi = work.get("doi") or ""
        clean_doi = normalize_doi(raw_doi)

        # Check for duplication
        if clean_doi and clean_doi in existing_dois and not args.force:
            skipped_count += 1
            continue

        year = work.get("publication_year") or 2024
        pub_date = work.get("publication_date") or f"{year}-01-01"

        # Journal / Source
        journal = ""
        primary_loc = work.get("primary_location") or {}
        source = primary_loc.get("source") or {}
        if source and source.get("display_name"):
            journal = source.get("display_name").strip()

        # Authors
        authors = []
        for authorship in work.get("authorships", []):
            name = authorship.get("author", {}).get("display_name")
            if name:
                authors.append(name.strip())
        if not authors:
            authors = ["Minhaj Sirajuddin"]

        # Classification: Research vs Review
        openalex_type = work.get("type", "").lower()
        is_review = (
            openalex_type == "review"
            or "review" in title.lower()
            or "perspective" in title.lower()
        )
        article_type_str = "review" if is_review else "research"
        article_badge = "Review" if is_review else "Research Article"

        # Classification: inStem Era vs Prior
        is_instem = int(year) >= 2015
        era_badge = "inStem Era" if is_instem else "Prior to inStem"

        # Generate folder slug
        slug = f"{slugify(title)}-{year}"
        if slug in existing_slugs and not args.force:
            skipped_count += 1
            continue

        work_dir = os.path.join(OUTPUT_DIR, slug)

        authors_yaml = "\n".join([f"  - {a}" for a in authors])

        frontmatter = f"""---
title: "{title}"
authors:
{authors_yaml}
date: '{pub_date}'
publication_types:
  - article-journal
publication: "*{journal}*"
doi: "{clean_doi}"
tags:
  - "{article_badge}"
  - "{era_badge}"
article_type: "{article_type_str}"
---
"""
        if args.dry_run:
            print(f"[DRY-RUN] Would create: {slug} ({year}) - {title[:50]}...")
            created_count += 1
        else:
            os.makedirs(work_dir, exist_ok=True)
            index_path = os.path.join(work_dir, "index.md")
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(frontmatter)
            existing_slugs.add(slug)
            if clean_doi:
                existing_dois.add(clean_doi)
            created_count += 1
            print(f"[+] Created: {slug}")

    print("\n" + "=" * 50)
    print(
        f"[*] Sync Summary: {created_count} new publication(s) added, {skipped_count} existing skipped."
    )
    print("=" * 50)


if __name__ == "__main__":
    main()

# Cytoskeleton Lab Website

Official website for the **Cytoskeleton Lab** led by **Prof. Minhaj Sirajuddin** at the **Institute for Stem Cell Science and Regenerative Medicine (iBRIC-inStem), Bangalore, India**.

- **Live URL**: [https://cytoskeleton-lab.netlify.app](https://cytoskeleton-lab.netlify.app) (and [http://cytoskeleton-lab.org](http://cytoskeleton-lab.org))
- **GitHub Organization**: `Minhajlab`
- **Framework**: [Hugo](https://gohugo.io/) (Extended) with [HugoBlox](https://hugoblox.com/) Academic Builder
- **CI/CD**: GitHub Actions → Netlify

---

## 🚀 How to Update Content (No Coding Required)

This website is designed for researchers. You **never need to edit website code or HTML** to update the site. Simply edit the data files and push to GitHub — GitHub Actions and Netlify automatically rebuild and publish the site in ~1 minute.

### 1. Adding or Updating Lab Members

Current lab members are stored in individual folders under `content/authors/`:

```
content/authors/
├── admin/                  # Prof. Minhaj Sirajuddin (PI)
├── drisya-dileep/
├── nivya-mendon/
├── rayees-ahmad-ganie/
├── ishan-kale/
├── anwesha-biswas/
├── victor-samuel/
└── lakshmi-prasanna/
```

**To add a new member:**
1. Create a new folder inside `content/authors/` (e.g. `john-doe/`).
2. Add an `_index.md` file with the following front matter:
   ```yaml
   ---
   title: John Doe
   role: Graduate Student (GS-2024)
   organizations:
     - name: iBRIC-inStem, Bangalore
   bio: Investigating microtubule motor dynamics.
   interests:
     - Biochemistry
     - Structural Biology
   education:
     courses:
       - course: MSc Biotechnology
         institution: University of Delhi
   social:
     - icon: envelope
       icon_pack: fas
       link: 'mailto:johnd@instem.res.in'
   user_groups:
     - Graduate Students      # Options: Principal Investigator, Postdoctoral Fellows, Graduate Students, Research Fellows
   ---

   **Project**: Microtubule Motor Dynamics

   **Outside Lab**: Hiking, badminton, reading.
   ```
3. (Optional) Place a square headshot named `avatar.jpg` inside the same folder (`content/authors/john-doe/avatar.jpg`).

---

### 2. Updating the Alumni List (`alumni.csv`)

Past lab members are managed in a simple CSV spreadsheet at `assets/data/alumni.csv`. You can edit this file directly in Excel, Google Sheets, or GitHub:

```csv
Name,Lab Role,Period,Current Position / Institution,LinkedIn / Profile
"Jane Smith","Postdoctoral Fellow","2020–2024","Assistant Professor, IIT Bombay",""
"John Doe","Graduate Student (PhD)","2018–2023","Postdoc, Harvard University",""
```

- When you commit a new row to `assets/data/alumni.csv`, the searchable and filterable Alumni table on `/people/` updates automatically.

---

### 3. Adding New Publications (`publications.bib`)

Publications are managed in standard academic **BibTeX** format in `publications.bib`:

1. Export the citation in BibTeX format from **Google Scholar, PubMed, or Zotero**.
2. Paste the entry into `publications.bib`:
   ```bibtex
   @article{author2026paper,
     title = {Title of the paper},
     author = {Author, First and Sirajuddin, Minhaj},
     journal = {Nature Cell Biology},
     year = {2026},
     doi = {10.1038/...}
   }
   ```
3. Commit and push. The GitHub Action will import the publication and update `/publication/`.
4. (Optional) You can also run locally:
   ```bash
   academic import publications.bib content/publication/ --compact
   ```

---

### 4. Updating Research Themes

Research themes are located in `content/research/`:

```
content/research/
├── microtubule-modifications/index.md
├── actin-cytoskeleton/index.md
├── cardiac-cytoskeleton/index.md
├── cilia-and-flagella/index.md
└── septins/index.md
```

To edit or add a research area:
- Edit the Markdown text inside any theme's `index.md`.
- To add a new theme, duplicate an existing folder, update `title`, `summary`, and write your narrative in standard Markdown.

---

### 5. Adding Lab Photos to the Gallery

The gallery is driven by `data/gallery.yaml`:

```yaml
- title: "Cryo-EM Session"
  category: "Science"
  caption: "Collecting data at the National Cryo-EM Facility"
  image: "media/gallery/cryo-session.jpg"
```

1. Place image files into `assets/media/gallery/`.
2. Add an entry to `data/gallery.yaml` with title, category, caption, and image path.

---

### 6. Updating Useful Links & Resources

Curated links (collaborators, funding databases, student guides) are maintained in `data/useful_links.yaml`. Simply append a new link under the appropriate category.

---

## 💻 Local Development (For Developers)

### Prerequisites

1. **Hugo Extended**: `v0.135+` or `v0.166+`
2. **Go**: `v1.22+`
3. **Node.js**: `v20+`

### Running the Site Locally

```bash
# Clone the repository
git clone https://github.com/Minhajlab/lab-website.git
cd lab-website

# Start the Hugo local development server
hugo server -D
```

Open [http://localhost:1313](http://localhost:1313) in your browser. Any edits you make will live-reload automatically.

### Building for Production

```bash
hugo --gc --minify
```

The compiled static HTML/CSS/JS is output into the `public/` directory.

---

## ☁️ Deployment Pipeline (Netlify Setup)

1. Create a free account on [Netlify](https://www.netlify.com).
2. Connect your GitHub repository (`Minhajlab/lab-website`) or use GitHub Actions:
   - Go to GitHub repo **Settings → Secrets and variables → Actions**.
   - Add secret: `NETLIFY_AUTH_TOKEN` (Generated from Netlify User Settings → Applications → Personal access tokens).
   - Add secret: `NETLIFY_SITE_ID` (Found in Netlify Site Configuration → General → Site details → Site ID).
3. Every push to `main` automatically triggers `.github/workflows/deploy.yml` which builds and deploys to Netlify.

---

## 📄 License & Attribution

- Built for the **Cytoskeleton Lab, iBRIC-inStem, Bangalore**.
- Theme powered by [HugoBlox (Academic)](https://hugoblox.com).

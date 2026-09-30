# Lab Website UI & Visual Verification Rules

These rules guide the agent when evaluating and testing frontend styling, layout responsiveness, and dark-theme contrast for the Cytoskeleton Lab website.

---

## 🎯 Target Environments
- **Primary Target (Local Deployment)**: `http://localhost:1313/`
  - Spun up via `hugo server -D` for instant local feedback before committing or pushing.
- **Production Target (Fallback / Verification)**: `https://minhajlab-instem.github.io/lab-website/`

---

## 📄 Key Pages to Audit
- **Homepage**: `http://localhost:1313/` (Carousel with bottom caption bar, Welcome section, 5-column Research row, News/Milestones split card, Outreach row, Recent publications)
- **People Page**: `http://localhost:1313/people/` (4-tier horizontal cards: Scientist, Postdocs, PhDs, Project Staff, and Alumni table)
- **Research Page**: `http://localhost:1313/research/` (5 core thematic areas)
- **Publications Page**: `http://localhost:1313/publication/` (Peer-reviewed citations & DOIs)

---

## 📸 Puppeteer Visual Inspection Protocol
When instructed to visually audit or verify UI changes:
1. **Launch Local Server** (if not already running):
   - Command: `hugo server -D`
   - Address: `http://localhost:1313/`
2. **Navigate**: Open the local deployment using Puppeteer.
3. **Test Responsive Viewports**:
   - **Mobile** (`375px × 812px`): Ensure cards stack gracefully without horizontal overflow, text remains readable, and mobile navigation toggles smoothly.
   - **Tablet** (`768px × 1024px`): Ensure 2-column grids and carousels display without clipping.
   - **Desktop** (`1200px × 800px`): Ensure the `1200px` max-width container clamp prevents elements from stretching indefinitely.
4. **Contrast & Legibility Checks**:
   - Canvas Background: `#0b1120` (Deep slate)
   - Card Background: `#111c33` (Elevated dark slate)
   - Accent & Headings: `#2dd4bf` / `#ffffff` (High contrast, WCAG AA compliant)
   - Secondary Text: `#94a3b8` / `#cbd5e1` (Legible muted slate)
5. **Member Cards**: Confirm avatars render on the left with 110px/140px dimensions, dummy SVGs display where photos are absent, and name/role/education/bio/links render cleanly on the right.

---

## 🌐 External Reference Scraping (Fetch MCP)
- Use the `fetch` tool to retrieve external design documentation, BioIcons SVG definitions, or API reference specs directly into clean markdown format.

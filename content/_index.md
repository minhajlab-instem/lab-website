---
title: "Cytoskeleton Lab"
date: 2026-01-01
type: landing

sections:
  - block: slider
    content:
      slides:
        - title: "Cytoskeleton & Motility Across Scales"
          content: "Investigating eukaryotic cytoskeleton systems from atomic cryo-EM structures to the mechanics of beating heart walls."
          align: left
          background:
            image:
              filename: hero/cytoskeleton-EM-1.png
              filters:
                brightness: 0.52
            size: cover
            position: center
          link:
            url: /research/
            text: Explore Research
            icon: microscope
            icon_pack: fas
        - title: "Decoding the Tubulin Code & Motors"
          content: "Deciphering how tubulin post-translational modifications regulate kinesin and dynein motility in cellular dynamics and disease."
          align: left
          background:
            image:
              filename: hero/CTT-MTs.png
              filters:
                brightness: 0.52
            size: cover
            position: center
          link:
            url: /publication/
            text: Latest Publications
            icon: book-open
            icon_pack: fas
        - title: "Mitotic Spindle & Cellular Dynamics"
          content: "Bridging the knowledge gap between clinical genetic findings and fundamental molecular biology."
          align: left
          background:
            image:
              filename: hero/mitosis.png
              filters:
                brightness: 0.52
            size: cover
            position: center
          link:
            url: /people/
            text: Meet the Team
            icon: users
            icon_pack: fas
    design:
      slide_height: '560px'
      is_fullscreen: false

  - block: collection
    content:
      title: "Research Themes"
      subtitle: "Cytoskeleton across length scales"
      text: "Our core areas of structural biology, biochemistry, and cellular dynamics"
      page_type: research
      count: 6
      sort_by: weight
    design:
      view: card
      columns: 3

  - block: people
    content:
      title: "Our Team"
      subtitle: "Meet the researchers driving our discoveries"
      user_groups:
        - Principal Investigator
        - Postdoctoral Fellows
        - Graduate Students
        - Research Fellows
    design:
      show_interests: true
      show_role: true
      show_social: true

  - block: collection
    content:
      title: "Recent Publications"
      subtitle: "Peer-reviewed findings and preprints from our group"
      text: "Explore our latest structural insights, biosensors, and physiological studies."
      page_type: publication
      count: 4
      order: desc
    design:
      view: citation
      columns: 1

  - block: markdown
    content:
      title: "Public Engagement & Outreach"
      subtitle: "Connecting fundamental science with society"
      text: |
        <div class="row g-4 align-items-center">
          <div class="col-md-6">
            <div class="p-4 bg-light rounded-4 shadow-sm h-100 border-start border-4 border-primary">
              <h4 class="fw-bold mb-2"><i class="fas fa-book-open me-2 text-primary"></i> Actually, Colors Speak</h4>
              <p class="text-muted small">An illustrated popular science book authored by the lab explaining the molecular cytoskeletal basis of animal color change.</p>
              <a href="/outreach/actually-colors-speak/" class="btn btn-outline-primary btn-sm rounded-pill px-3">Read More →</a>
            </div>
          </div>
          <div class="col-md-6">
            <div class="p-4 bg-light rounded-4 shadow-sm h-100 border-start border-4 border-info">
              <h4 class="fw-bold mb-2"><i class="fas fa-film me-2 text-info"></i> Written Out of History</h4>
              <p class="text-muted small">A documentary film spotlighting three pioneering Indian scientists: Dr. Sambhunath De, Dr. Sipra Guha-Mukherjee, and Dr. Obaid Siddiqi.</p>
              <a href="/outreach/forgotten-indian-scientists/" class="btn btn-outline-info btn-sm rounded-pill px-3">Watch Documentary →</a>
            </div>
          </div>
        </div>
    design:
      columns: '1'
---

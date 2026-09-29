---
title: "Cytoskeleton Lab"
date: 2026-01-01
type: landing

sections:
  - block: slider
    content:
      slides:
        - title: "Microtubule Architectures & Cryo-EM"
          content: "Sub-nanometer cryo-EM visualization of native tubulin lattices, protofilament dynamics, and motor interfaces."
          align: left
          background:
            image:
              filename: hero/cytoskeleton-EM-1.png
              filters:
                brightness: 0.65
            size: cover
            position: center
        - title: "The Tubulin Code & Molecular Motors"
          content: "Deciphering how polyglutamylation and tyrosination states on C-terminal tails orchestrate cellular transport."
          align: left
          background:
            image:
              filename: hero/CTT-MTs.png
              filters:
                brightness: 0.65
            size: cover
            position: center
        - title: "Mitotic Spindle & Force Generation"
          content: "Super-resolution and fluorescence imaging unraveling tension, kinetochore capture, and chromosome segregation."
          align: left
          background:
            image:
              filename: hero/mitosis.png
              filters:
                brightness: 0.65
            size: cover
            position: center
    design:
      slide_height: '500px'
      is_fullscreen: false

  - block: markdown
    content:
      title: ""
      subtitle: ""
      text: |
        <div class="welcome-section text-center py-4 my-2">
          <div class="badge rounded-pill px-3 py-2 text-uppercase tracking-wider mb-3 fw-semibold welcome-badge">
            <i class="fas fa-microscope me-2"></i> Welcome to the Cytoskeleton Lab @ inStem
          </div>
          <h2 class="welcome-heading fw-bold mb-3">
            Exploring Cytoskeleton Systems <span class="text-teal-gradient">Across Length Scales</span>
          </h2>
          <p class="welcome-lead mx-auto mb-4 text-muted">
            The eukaryotic cytoskeleton is a marvel of cellular engineering—providing structural integrity, powering intracellular highways, and driving cell division and motility. At the <strong>Minhaj Sirajuddin Lab</strong>, Centre for Cardiovascular Biology and Disease (CCBD), Institute for Stem Cell Science and Regenerative Medicine (inStem), Bengaluru, we explore how molecular mechanics at the single-protein level scale up to govern organ physiology and human disease.
          </p>
          <div class="row g-3 justify-content-center text-start mt-2">
            <div class="col-12 col-md-4">
              <div class="p-3 rounded-4 welcome-feature-card h-100">
                <div class="d-flex align-items-center mb-2">
                  <div class="welcome-icon-box me-3"><i class="fas fa-atom"></i></div>
                  <h6 class="fw-bold mb-0 text-white">Structural Biology</h6>
                </div>
                <p class="small text-muted mb-0">High-resolution cryo-EM and crystallography revealing atomic mechanisms of tubulin-modifying enzymes.</p>
              </div>
            </div>
            <div class="col-12 col-md-4">
              <div class="p-3 rounded-4 welcome-feature-card h-100">
                <div class="d-flex align-items-center mb-2">
                  <div class="welcome-icon-box me-3"><i class="fas fa-vial"></i></div>
                  <h6 class="fw-bold mb-0 text-white">Single-Molecule Biophysics</h6>
                </div>
                <p class="small text-muted mb-0">Total Internal Reflection Fluorescence (TIRF) and biosensors tracking motor stepping and modification waves.</p>
              </div>
            </div>
            <div class="col-12 col-md-4">
              <div class="p-3 rounded-4 welcome-feature-card h-100">
                <div class="d-flex align-items-center mb-2">
                  <div class="welcome-icon-box me-3"><i class="fas fa-heartbeat"></i></div>
                  <h6 class="fw-bold mb-0 text-white">Cardiomyopathy & Physiology</h6>
                </div>
                <p class="small text-muted mb-0">Translating microtubule detyrosination dynamics to heart wall stiffness, contractility, and cardiac therapeutics.</p>
              </div>
            </div>
          </div>
        </div>
    design:
      columns: '1'

  - block: research_row
    content:
      title: "Research Programs"
      subtitle: "Cytoskeleton across length scales: from atomic structures to tissue physiology"

  - block: news_milestones
    content:
      title: "News & Milestones"
      subtitle: "Latest Breakthroughs, Preprints & Social Updates"

  - block: outreach_row
    content:
      title: "Science Communication & Outreach"
      subtitle: "Connecting Fundamental Cytoskeleton Science with Society"

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
---

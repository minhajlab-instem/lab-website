---
title: "People"
date: 2026-01-01

type: landing

sections:
  - block: people
    content:
      title: Lab Members
      subtitle: Meet our research team
      user_groups:
        - Principal Investigator
        - Postdoctoral Fellows
        - Graduate Students
        - Research Fellows
        - Project Staff
      sort_by: Params.last_name
      sort_ascending: true
    design:
      show_interests: true
      show_role: true
      show_social: true

  - block: markdown
    content:
      title: Lab Alumni
      subtitle: Past members and where their journeys led
      text: "{{< alumni_table >}}"
    design:
      columns: '1'
---
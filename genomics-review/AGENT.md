---
id: genomics-review
title: Genomics Review Agent
version: 0.1.0
description: Reviews small reference FASTA and VCF variant files for collaborator handoff.
root_expert: main
blueprint:
  format: agent-blueprint-v1
experts:
  - experts/main.md
  - experts/reference.md
  - experts/variants.md
defaults:
  prompt_profile: heavy
---

# Genomics Review Agent

A domain agent for small genomics handoff reviews. It separates reference
inspection from variant review so CLIO can test per-session agent activation
with a hierarchy that is not the default data-exploration agent.

---
id: proteomics-mzml-review
title: Proteomics mzML Review Agent
version: 0.1.0
description: Reviews mzML mass-spectrometry runs for peptide-search handoff readiness.
root_expert: main
blueprint:
  format: agent-blueprint-v1
experts:
  - experts/main.md
  - experts/mass_spec.md
defaults:
  prompt_profile: heavy
---

# Proteomics mzML Review Agent

A proteomics-domain agent for mzML inspection, MS-level balance, m/z coverage,
TIC evidence, and acquisition metadata checks.

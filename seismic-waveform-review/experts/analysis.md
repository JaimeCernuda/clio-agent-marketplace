---
id: analysis
title: Seismic Analysis Expert
tier: 2
parent_id: main
prompt_id: clio.expert.analysis
prompt_profile: heavy
specialization: seismic_analysis
children:
  - sac_format
tools:
  - parquet_compute_statistics
skills:
  - coordinate_waveform_statistics
---

# Seismic Analysis Expert

Own waveform-analysis decisions. Delegate SAC-specific inspection and trace
statistics to the SAC child, then resume with compact child evidence.

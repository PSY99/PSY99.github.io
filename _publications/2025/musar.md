---
title:          "MuSAR: Multi-Step Attack Reconstruction from Lightweight Security Logs via Event-Level Semantic Association in Multi-Host Environments"
date:           2025-11-03 00:01:00 +0800
selected:       true
pub:            "The 28th International Symposium on Research in Attacks, Intrusions and Defenses (RAID 2025)"
pub_date:       "2025"

abstract: >-
  Multi-step attacks challenge security analysts in reconstructing attack sequences from extensive multi-host log data. Existing attack reconstruction approaches rely heavily on computationally intensive audit logs and provenance analysis, limiting their practicality in multi-host environments. We present MuSAR, a framework for real-time reconstruction of multi-step attacks in multi-host environments using lightweight security logs (network alarms and application logs). First, security logs are consolidated into inter-host and intra-host security events through semantic analysis, respectively. Then, these security events are mapped to unified attack lifecycle stages through MITRE ATT&CK framework integration. Finally, a heuristic algorithm is implemented to identify potential multi-step attacks and reconstruct complete attack sequences based on event-level semantic associations. Evaluation on the CPTC2018 dataset and a multi-step attack simulation dataset demonstrates MuSAR’s effectiveness in identifying attack-related traces and reconstructing multi-step attacks, achieving an average recall of 93.48% and F1-score of 94.39%, respectively, outperforming state-of-the-art methods in attack investigation and reconstruction in multi-host environments.
cover:          /assets/images/covers/musar.png
authors:
  - Yang Liu*
  - Zisen Xu*
  - Zian Luo#
  - Jin'ao Shang
  - Shilong Zhang
  - Haichuan Zhang
  - Ting Liu#
links:
  # Paper: https://www.sciencedirect.com/science/article/abs/pii/S0950705125017514
  Code: https://github.com/zisenXu/MuSAR
---

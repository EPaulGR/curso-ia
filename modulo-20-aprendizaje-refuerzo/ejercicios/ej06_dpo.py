"""Ejercicio 6 — Preferencias: Bradley-Terry y la pérdida DPO.

- `prob_bradley_terry(r_pref, r_rech)`: sigma(r_pref - r_rech).
- `perdida_modelo_recompensa(r_pref, r_rech)`: -mean log sigma(r_pref - r_rech).
- `perdida_dpo(logp_pol_pref, logp_pol_rech, logp_ref_pref, logp_ref_rech, beta)`:
  -mean log sigma(beta * ((logp_pol_pref - logp_ref_pref) - (logp_pol_rech - logp_ref_rech))).
Ouyang et al. 2022 (InstructGPT); Rafailov et al. 2023 (DPO).
"""
import numpy as np


def _logsig(x):
    return -np.logaddexp(0, -x)


def prob_bradley_terry(r_pref, r_rech):
    raise NotImplementedError  # TODO: implementa esta función


def perdida_modelo_recompensa(r_pref, r_rech):
    raise NotImplementedError  # TODO: implementa esta función


def perdida_dpo(logp_pol_pref, logp_pol_rech, logp_ref_pref, logp_ref_rech, beta=0.1):
    raise NotImplementedError  # TODO: implementa esta función

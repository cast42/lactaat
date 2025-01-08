# Lactate thresholds and zones

Repo to use python library [lactate-thresholds](https://github.com/bart6114/lactate-thresholds) to calculate thresholds and zones.

Adapt your measurements in file [lactaat.py](lactaat.py)

Run the python program lactaat.py:

```zsh
uv run python lactaat.py
```

Output:

```ascii
➜  lactaat git:(main) ✗ uv run python lactaat.py
                 Measurement input
┏━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━┳━━━━━━━━┓
┃ intensity ┃ heart_rate ┃ lactate ┃ step ┃ length ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━╇━━━━━━━━┩
│ 60.0      │ 89.0       │ 1.5     │ 1.0  │ 4.0    │
│ 100.0     │ 102.0      │ 1.7     │ 2.0  │ 4.0    │
│ 140.0     │ 109.0      │ 1.5     │ 3.0  │ 4.0    │
│ 180.0     │ 126.0      │ 4.2     │ 4.0  │ 4.0    │
│ 220.0     │ 142.0      │ 2.5     │ 5.0  │ 4.0    │
│ 260.0     │ 168.0      │ 6.1     │ 6.0  │ 4.0    │
│ 300.0     │ 175.0      │ 12.7    │ 7.0  │ 4.0    │
└───────────┴────────────┴─────────┴──────┴────────┘
lpt1
LactateTurningPoint(lactate=2.8882052600115173, intensity=207.64450825550853, heart_rate=139.54939912792284)
lpt2
LactateTurningPoint(lactate=6.170051370499422, intensity=257.4486031491451, heart_rate=161.45832009762398)
lt2_estimate
ThresholdEstimate(lactate=2.9, intensity=206.9, heart_rate=139.0)
lt2_estimate
ThresholdEstimate(lactate=5.2, intensity=246.9, heart_rate=157.0)

                                                         Seiler 3 zones
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ zone   ┃ intensity       ┃ heart_rate ┃ focus                                                                                 ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Zone 1 │ 0.00 - 206.90   │ up to 139  │ Recovery, building an aerobic foundation.                                             │
│ Zone 2 │ 206.90 - 246.90 │ 139 - 157  │ Moderate aerobic work; a gray zone with limited efficiency for endurance adaptations. │
│ Zone 3 │ 246.90 - max    │ 157 - max  │ Enhancing anaerobic threshold and lactate tolerance.                                  │
└────────┴─────────────────┴────────────┴───────────────────────────────────────────────────────────────────────────────────────┘

                                                         Seiler 5 zones
┏━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ zone   ┃ intensity       ┃ heart_rate ┃ focus                                                                                 ┃
┡━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Zone 1 │ 0.00 - 206.90   │ up to 139  │ Recovery, building an aerobic foundation.                                             │
│ Zone 2 │ 206.90 - 246.90 │ 139 - 157  │ Moderate aerobic work; a gray zone with limited efficiency for endurance adaptations. │
│ Zone 3 │ 246.90 - max    │ 157 - max  │ Enhancing anaerobic threshold and lactate tolerance.                                  │
└────────┴─────────────────┴────────────┴───────────────────────────────────────────────────────────────────────────────────────┘

                                         Friel 7 zones running
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ zone                        ┃ intensity        ┃ heart_rate ┃ focus                                  ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Zone 1. Recovery            │ up to 194.10     │ 0 - 133    │ Active recovery.                       │
│ Zone 2. Aerobic             │ 194.10 - 208.00  │ 133 - 140  │ Aerobic endurance.                     │
│ Zone 3. Tempo               │ 211.50 - 225.40  │ 141 - 148  │ Building aerobic capacity and stamina. │
│ Zone 4. SubThreshold        │ 228.90 - 243.10  │ 149 - 155  │ Threshold effort.                      │
│ Zone 5a. VO2 SuperThreshold │ 246.80 - 254.20  │ 157 - 160  │ Improving VO2 max.                     │
│ Zone 5b. Aerobic Capacity   │ 258.00 - 269.80  │ 162 - 166  │ Anaerobic capacity.                    │
│ Zone 5c. Anaerobic Capacity │ more than 269.80 │ 166 - max  │ Peak power output.                     │
└─────────────────────────────┴──────────────────┴────────────┴────────────────────────────────────────┘
```

Heart rate intensity plot:

![Heart rate intensity plot](images/chart_heart_rate_intensity.png)

Lactate intensity plot:

![Lactate intensity plot](images/chart_lactate_intensity.png)

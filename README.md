# Persistence-referenced benchmark of CA-ANN-Markov and CNN-Markov LULC models (Khatra, West Bengal)

Code accompanying: Dule, S. and Sharma, A. (2026). *Out-of-time benchmarking of CA-Markov and CNN-based land cover projection against persistence in a lateritic plateau fringe: Khatra subdivision, West Bengal, India*. *Environmental Modelling & Software* (submitted).

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.24584128.svg)](https://doi.org/10.5281/zenodo.24584128)
<!-- EDIT: replace XXXXXXX with the CODE DOI after your first GitHub release -->

## What this does
Calibrates on 2003→2013 and hindcasts 2023 for the Khatra sub-division, compares CA-ANN-Markov, CNN-Markov and CNN-argmax
**against a persistence (no-change) baseline** using overall accuracy, figure of merit, and quantity/allocation disagreement
with paired block bootstraps, then projects 2033 under three Markov-rate scenarios (T1, mean, T2).

## Repository layout
```
notebooks/
  V2_1_CA_ANN_Markov_r3.ipynb               CPU   CA-ANN-Markov: hindcast 2023 + 2033 scenarios
  V2_2_CNN_r3.ipynb                         GPU   Patch-CNN suitability: argmax and Markov-demand allocation
  V2_3_Compare_and_Report_r3.ipynb          CPU   comparison tables and report CSVs
  V2_4_Stats_Figures_Tables.ipynb           CPU   statistics, Figs 5-9 and 11, Tables 3-7 and S1-S4
  V2_5_Map_Figures_and_Flowchart_v5.ipynb   CPU   map figures 3, 4, 10 and flowchart (Fig. 2)
scripts/
  graphical_abstract.py                     graphical abstract (matplotlib)
  make_manifest.py                          file list with SHA-256 for the data archive
data/README.md                              what to download from Zenodo and where to put it
```

## How to reproduce (Google Colab + Google Drive)
1. Download the data archive from https://doi.org/10.5281/zenodo.24584128 and unzip it into `My Drive/Obj2_LULC_GWP/`.
2. Open each notebook in Colab (File → Open notebook → GitHub tab, or upload).
3. Run **in this order**; each notebook mounts Drive and reads/writes `PATH = /content/drive/MyDrive/Obj2_LULC_GWP/`:

| Step | Notebook | Runtime | Notes |
|---|---|---|---|
| 1 | V2_1 | CPU | Main run: `FEATURE_MODE='anomaly'; RUN_TAG=''; SEEDS=[0,1,2,3,4]`. Restart the session between different runs. |
| 2 | V2_2 | GPU (T4) | Same configuration cell. Resumes automatically; finished seeds are skipped. |
| 3 | V2_3 | CPU | Set `SEEDS` in the last cell to the seeds you ran. |
| 4 | V2_4 | CPU, ~1 min | Rebuilds every figure and table from the report CSVs. |
| 5 | V2_5 | CPU | Needs `Khatra_boundary.shp`; writes print-size maps. |

Ablation runs (global features, no climate, state-only) are listed at the top of the V2_1 and V2_2 configuration cells.
Seeds are fixed (`SEEDS`, `SPLIT_SEED = 42`), but GPU kernels can differ slightly between hardware, so small numeric differences
in the CNN results are possible.

## Requirements
Python 3, see `requirements.txt` (Colab provides most packages; the notebooks install the rest). `requirements-frozen.txt`
[add after your final run] records the exact versions used.

## Data and licences
- Code: MIT (see `LICENSE`).
- Data and model outputs: Zenodo, CC BY 4.0. Original imagery and climate data remain subject to the USGS Landsat, SRTM and CHIRPS terms.

## Citation
Please cite the article and the archived release (see `CITATION.cff`; GitHub shows a "Cite this repository" button).

## Contact
Dr. Arabinda Sharma, School of Geography, Gangadhar Meher University, Sambalpur 768004, Odisha, India. arbind_78@rediffmail.com

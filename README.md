# Out-of-Time Benchmarking of CA-Markov and CNN-Based Land Cover Projection Against Persistence

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)

Official analysis and visualization notebooks accompanying the manuscript:

> **Out-of-time benchmarking of CA-Markov and CNN-based land cover projection against persistence in a lateritic plateau fringe: Khatra, West Bengal, India**  
> Suraj Dule and Arabinda Sharma  
> *School of Geography, Gangadhar Meher University, Sambalpur, Odisha 768004, India*

---

## Overview

Decadal land use and land cover (LULC) projections frequently report overall accuracies exceeding 95%, largely because most pixels do not change over a ten-year interval. This repository provides a reproducible out-of-time benchmarking pipeline comparing three projection models against a no-change **persistence baseline** across the Khatra sub-division of Bankura district, West Bengal, India (2,410 km² valid analysis domain; 30 m spatial resolution):

1. **CA-ANN-Markov:** Pixel-level artificial neural network (64–32 units) suitability surface paired with Markov demand, cellular automata (CA) contiguity, and competitive allocation.
2. **CNN-Markov:** Patch-based convolutional neural network (5 × 5 dynamic patches + static terrain features, class-weighted cross-entropy) using the identical Markov demand, CA contiguity, and allocation rules.
3. **CNN-argmax:** Unconstrained allocation from the same CNN suitability probabilities without Markov demand control.

Models are calibrated on **T1 (2003 → 2013)** and evaluated out-of-time on **2023** across spatially held-out 64 × 64 pixel blocks (70% train / 15% validation / 15% test) using five-seed ensembles, paired spatial block bootstrapping (2,000 resamples), covariate/scaling ablations (within-year standardization vs. global min-max, no climate layers, state + static only), steep-slope (>10°) water plausibility checks, and **2033 scenario projections** calibrated on **T2 (2013 → 2023)** under three Markov rate scenarios (`T1`, `Mean`, and `T2`).

---

## Repository Contents & Execution Order

Run the five notebooks sequentially in Google Colab (GPU runtime recommended for Notebooks 1 and 2) or a local CUDA-enabled Python environment:

| Step | Notebook | Purpose |
| :---: | :--- | :--- |
| **1** | `notebooks/V2_1_CA_ANN_Markov_r3.ipynb` | Prepares the harmonized 30 m grid (2,399 × 2,424), applies 64-pixel spatial block splitting, trains the multi-seed CA-ANN-Markov models (primary configuration + ablations), and generates 2023 hindcasts and 2033 scenario projections. |
| **2** | `notebooks/V2_2_CNN_r3.ipynb` | Trains the patch-based CNN suitability learner across five primary seeds and three ablation seeds, and exports both `CNN-Markov` and unconstrained `CNN-argmax` 2023 hindcasts and 2033 projections. |
| **3** | `notebooks/V2_3_Compare_and_Report_r3.ipynb` | Runs model evaluation against the persistence baseline, computes OA, Kappa, FoM, quantity/allocation disagreement, Fallow → Forest hit precision, steep-slope water diagnostics, paired block-bootstrap intervals, and scenario variance decomposition ($\eta^2$). |
| **4** | `notebooks/V2_4_Stats_Figures_Tables.ipynb` | Generates publication-ready statistical plots (seed distributions, paired contrast forest plots, disagreement breakdowns, ablation plots, hit-precision intervals, and 2033 scenario/year-label confounding bar charts) and formatted summary tables. |
| **5** | `notebooks/V2_5_Map_Figures_and_Flowchart_v5.ipynb` | Renders high-resolution (300 DPI PNG, vector PDF, 600 DPI LZW-compressed TIFF) cartographic panels with latitude/longitude ticks, SI scale bars, study-area shapefile boundaries, and the methodological flowchart. |

---

## Data Requirements

Input rasters and large GeoTIFF outputs are excluded from this repository to stay within GitHub file limits. All primary input layers are co-registered to the 2023 WGS 84 UTM 30 m master grid (`2,399 × 2,424` pixels):

* **Classified LULC maps (5 classes):** `LULC_2003.tif`, `LULC_2013.tif`, `LULC_2023.tif` (`1` = Water, `2` = Forest, `3` = Agriculture, `4` = Settlement, `5` = Fallow), derived from pre-monsoon Landsat 7 ETM+, Landsat 8 OLI/TIRS, and Landsat 9 OLI-2/TIRS-2 scenes (USGS EarthExplorer) with Google Earth Pro refinement.
* **Dynamic covariates (per epoch):** NDVI, MNDWI, NDMI, Land Surface Temperature (LST), Euclidean Distance to Water, and annual CHIRPS rainfall.
* **Static terrain layers:** SRTM 30 m DEM, Slope, Drainage Density (DD), Lineament Density (Ld), and Topographic Wetness Index (TWI).
* **Vector boundary:** `Khatra_Boundary.shp` (with accompanying `.dbf`, `.prj`, `.shx` files).

**Data availability:** The processed GeoTIFF archive and summary CSVs are available at `[Zenodo Data DOI — or from the corresponding author upon reasonable request]`. Raw Landsat and SRTM data are openly available via [USGS EarthExplorer](https://earthexplorer.usgs.gov/), and CHIRPS rainfall data via the [Climate Hazards Center](https://www.chc.ucsb.edu/data/chirps).

---

## Quick Start

### Option 1: Google Colab (Recommended)
1. Upload the input raster folder to your Google Drive (e.g., `/content/drive/MyDrive/Khatra_LULC_Benchmark/`).
2. Open any notebook in [Google Colab](https://colab.research.google.com/) and select **Runtime → Change runtime type → T4 GPU** (for Notebooks 1 and 2).
3. Update the `PATH` variable in the setup cell to match your Drive directory and run cells top to bottom.

### Option 2: Local Environment
```bash
git clone [https://github.com/sdule1/Khatra-LULC-Projection-Benchmark.git](https://github.com/sdule1/Khatra-LULC-Projection-Benchmark.git)
cd Khatra-LULC-Projection-Benchmark
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab

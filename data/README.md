Data (not stored in this repository)

Rasters and result tables are too large for git. They are archived on Zenodo:
[10.5281/zenodo.24584128](https://doi.org/10.5281/zenodo.24584128)

Download all files from the Zenodo record, unzip any archives, and copy everything into My 'Drive/Obj2_LULC_GWP/'
(the `PATH` set at the top of every notebook). Expected contents:
File | Description
|---|---|
`LULC_2003.tif`, `LULC_2013.tif`, `LULC_2023.tif` | Classified land use / land cover maps (5 classes), master grid |
`NDVI_{y}.tif`, `MNDWI_{y}.tif`, `NDMI_{y}.tif`, `LST_{y}.tif`, `Rainfall_{y}.tif`, `Dist_Water_{y}.tif` | Dynamic covariates for y = 2003, 2013, 2023 |
`SRTM_DEM.tif`, `Slope.tif`, `DD.tif`, `Ld.tif`, `TWI.tif` | Static terrain and drainage covariates |
`Khatra_boundary.shp` (+ `.dbf .shx .prj .cpg`) | Study-area boundary |
`revised_outputs_v2_anomaly/` | Model maps per seed (hindcast 2023, forecast 2033) and run tables |
`revised_outputs_v2_REPORT/` | Comparison CSVs, `manuscript_figs_tables/` and `manuscript_maps/`

All rasters share one grid: EPSG:[code], 30 m.

Original sources: Landsat (USGS EarthExplorer), SRTM (Farr et al., 2007), CHIRPS (Funk et al., 2015).

Data: CC BY 4.0.

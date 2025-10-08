# Secondary Data Inventory

This folder stores the processed secondary datasets that back the optional map layers in the Streamlit application.  The raw CSV exports are kept in the project Drive (not in Git) because of size and licensing constraints.  Each subdirectory contains:

* the **raw inputs** you should download into the Drive before rerunning the notebook;
* a Jupyter notebook under `scripts/secondary_data_scripts/` that documents the cleaning steps; and
* the **GeoJSON boundary file** that is actually read by the app (a backup copy of the GeoJSON lives here, while the version used by Streamlit is synced to `streamlit-app/boundaries/`).

## Directory overview

```
secondary_data/
├── household_income/
│   └── household_income_boundary_copy.geojson
└── unemployment_data/
    └── unemployment_boundary_copy.geojson
```

> ℹ️  The working shapefile download from `tl_2024_25_tract/…` and the raw CSV exports are ignored by Git.  Keep those files in the shared Drive when you need to regenerate the GeoJSON outputs.

## Data inventory and CSV versions

| Layer | Raw CSV (Drive) | Source & release | Notebook | Output GeoJSON | Notes |
| --- | --- | --- | --- | --- | --- |
| Median Household Income | `household_income/median household income.csv` | U.S. Census Bureau, American Community Survey (ACS) **2019–2023 5-year Data Profile (DP03)**. Export filtered to Essex County, MA tracts. Downloaded 2025-09-08 for this project. | `scripts/secondary_data_scripts/household_income.ipynb` | `household_income_boundary_copy.geojson` → copy to `streamlit-app/boundaries/household_income_boundary.geojson` | Contains `Estimate` (median income in 2023 inflation-adjusted dollars) and `MoE` (margin of error). Requires the 2024 TIGER/Line tract shapefile in `household_income/tl_2024_25_tract/` when regenerating. |
| Unemployment Rate | `unemployment_data/unemployment.csv` | U.S. Census Bureau, ACS **2019–2023 5-year Data Profile (DP03)**. Export filtered to Essex County, MA tracts. Downloaded 2025-09-08 for this project. | `scripts/secondary_data_scripts/unemployment_data.ipynb` | `unemployment_boundary_copy.geojson` → copy to `streamlit-app/boundaries/unemployment_boundary.geojson` | Contains `Estimate` (percent unemployed, population 16+), and `MoE`. Uses the same 2024 TIGER/Line tract shapefile when regenerating. |

## Updating a layer

1. Download the latest ACS Data Profile (DP03) tables for Essex County census tracts from [data.census.gov](https://data.census.gov/). Save the export to the matching CSV path in the Drive (e.g., `household_income/median household income.csv`). Record the ACS release (e.g., 2018–2022 vs. 2019–2023) in the table above when you update it.
2. Download the census tract shapefile for Massachusetts (state FIPS 25) from the [Census TIGER/Line](https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html) site and place it in the appropriate subfolder. The notebooks expect the folder name `tl_YYYY_25_tract`.
3. Run the corresponding notebook in `scripts/secondary_data_scripts/` to clean the CSV, merge it with the tract geometry, and export a GeoJSON.
4. Copy the resulting GeoJSON to `streamlit-app/boundaries/` so the Streamlit app can pick up the new layer. Keep a backup copy in this directory.
5. Update the "Source & release" column above with the new ACS release and the download date so others know which version is in use.

## Column conventions

* **Geography** – Original ACS geography label (e.g., `Census Tract 2501; Essex County; Massachusetts`). The notebooks standardize this to comma-separated text and extract the tract identifier for joins.
* **Estimate** – Numeric value converted from the ACS percentage or dollar string. Stored as `float` in the exported GeoJSON.
* **MoE** – Margin of error stripped of symbols (±, %). Stored as `float` in the exported GeoJSON.

Maintaining these conventions ensures the Streamlit layers and legends render correctly.
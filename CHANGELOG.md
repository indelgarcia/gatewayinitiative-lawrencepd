# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.3.8] - 2025-07-31
### Added
- `liquor_retail.ipynb` to clean, transform and map the liquor retail locations in Lawrence, MA
- `liquor_license_map_by_type.html` to draft a visualization liquor retail locations by type

### Updated
- requirements.txt to include `geopy` and `folium` for geocoding and mapping functionality

## [0.3.7] - 2025-07-30
### Updated
- Updated `streamlit_app.py` to add toggle instead of checkbox for heatmap and poverty layer visibility.

## [0.3.6] - 2025-07-30
### Updated
- streamlit_app.py to fix the legend

## [0.3.5] - 2025-07-25
### Updated
- steamlit_app.py to add legend to povery choropleth map
## [0.3.4] - 2025-07-17
### Updated
- Updated `geopandas_poverty.ipynb` to include a new section that loads the poverty on below poverty line data from the US Census Bureau and merges it with the Lawrence boundary data.
- Replaced the resulting GeoDataFrame with the merged data in the `poverty_boundary.geojson` file.

### Added
- Added a prototype function to automate the cleaning of the lawrence boundary data in `geopandas_poverty.ipynb`. This function will be used to clean the boundary data in future iterations.

## [0.3.3] - 2025-07-11
### Added
- `geopandas_poverty.ipynb` notebook to use the US Census Bureau's poverty data to create a choropleth map of poverty levels in Lawrence, MA
- Organized a new folder structure for secondary data in the data directory
- Organized a new folder structure for boundaries in the streamlit app
- added the resulting GeoJSON file `poverty_boundary.geojson` to the `boundaries` directory

### Updated
- Updated `streamlit_app.py` 
  - to load existing lawrence boundary from the new boundaries directory
  - to load the poverty choropleth layer from the new boundaries directory
  - Making CP 10 publicly available via gitignore command


## [0.3.2] - 2025-07-08
### Updated
- plugged in the latest checkpoint file `checkpoint10_combined_data.csv` into the Streamlit app.

### Removed
- Removed checkpoint 9 from tracking.

## [0.3.1] - 2025-07-07
### Updated
- Bug fix in `date_check.ipynb` to ensure the date column concatenation works correctly.

## [0.3.0] - 2025-07-06
### Added
- New notebook, `date_check.ipynb`, to check for missing dates in the dataset.
- Manually downloaded the missing dates PDFs from the Lawrence PD website
- Added logic to combine the missing dates dataset with the main dataset in

- Added logic to `convert_pdfs.ipynb` to handle the the missing dates PDFs.\

### Updated/Changed
- Have the missing dates dataset go through the same processing as the rest of the dataset.

## [0.2.9] - 2025-06-26

### Added
- Added logic to filter out year 2025 from the dataset in `clean_csv.ipynb`
- Made most recent checkpoint visible/public via gitignore command

### Changed
- Updated and refactor `hash.ipynb` to work with the latest checkpoint files (cp9).

- Updated and refactored 'categorize_visualizations.ipynb' to work with the latest checkpoint files.

- Updated `geocode_merge.ipynb` to work with the latest checkpoint files and ensure compatibility with the new geocoding logic.

- made streamlit app compatible with the latest checkpoint file (cp9)
- updated tableau dashboard to reflect the latest checkpoint file (cp9)

## [0.2.8] - 2025-06-25
### Changed
- Changed `geocode_part2.ipynb` to `geocode_merge.ipynb` to better reflect its purpose of merging geocode data with checkpoints.

### Added
- Added a new section in `geocode_merge.ipynb` to handle merging geocoded latitude and longitude data with the existing `checkpoint2`

### Removed
- Removed the `Location` cleanup logic from `clean_csv.ipynb` as it is now handled in `geocode_merge.ipynb`.

## [0.2.7] - 2025-06-20
### Added
- Created new notebook `address_mapping.ipynb` to geocode addresses using OpenCage API and OpenStreetMap.
- Added full address cleaning logic to normalize address formats and handle variations
- Implemented multiple geocoding passes to overcome OpenCage daily free request limits. Final iteration includes optimized and cleaner geocoding code.
- Merged multiple geocode result files into one consolidated and deduplicated file.
- Added additional logic to fill missing latitude and longitude values after merging.
- Integrated `config.json` file for securely storing API keys and updated `.gitignore` to exclude this file.

### Notes
- Original code for `address_mapping.ipynb` was provided by Ritika Pandey with file directory adjustments and API key handling and optimizations added by Indel.

## [0.2.6] - 2025-06-19
### Changed
- Updated `clean_pdfs.ipynb` to handle retrieve new merged CSV file for 2018-2024 incident reports.
- Added code to handle any new transformations that wasn't in the previous csv file.
- Moved geocoding "Mass check" to geocode_part2.ipynb

## [0.2.5] - 2025-06-18  
### Changed
- Updated `convert_pdfs.ipynb` to handle retrieve years 2023 and 2024.  
- Updated `download_pdfs.ipynb` to download incident report PDFs for 2023 and 2024 using Tesseract and pdfplumber
- Updated both scripts to also scrape and download incident reports from 2018-2024

### Notes
- There was major data (incidents) missing from 2023-2024 due to the scanned pdfs not being read properly. This new approach uses Tesseract OCR and pdfplumber to extract text from the PDFs, which should improve data completeness and accuracy.
- 2018-2023 was included to be comprehensive

## [0.2.4] - 2025-06-12  
### Added  
- Introduced a new Streamlit page at `pages/TableauDashboard.py` to embed a Tableau public dashboard for visualizing Lawrence PD data.  
  - Custom HTML integration allows scaled rendering and improved layout control.  
  - Embedded URL: `https://public.tableau.com/views/LawrencePDPublicData/Dashboard4`. 

  - Added a new section in `convert_pdfs.ipynb` to parse and convert 2023–2024 PDF reports into a single structured CSV file.  
  - Calls `parse_all_pdfs_to_csv(PDF_DATA_DIR, parsed_csv_path)` with updated input/output paths.  
  - Dynamically constructs directory paths using `os.getcwd()` for compatibility across systems.

- Added a new section in `download_pdfs.ipynb` to include logic for downloading 2023 and 2024 incident report PDFs.  
  - Filters files using a regex pattern matching MM-DD-2023.pdf and MM-DD-2024.pdf.  
  - Automatically organizes PDFs into subfolders by year and month (e.g., 2023_january, 2024_march).  
  - Prints progress updates every 500 documents to track batch progress.  
  - Skips invalid or non-PDF files based on response headers and filename format. 

### Notes  
- The initial creation and configuration of the `streamlit_app.py` main app file was made by Ritika in a prior version at May 19, 2025 but was not tracked in earlier changelog entries.
  - It includes the app entry point, base layout configuration, and loading of geospatial boundaries for Lawrence.  

## [0.2.3] - 2025-06-04  
### Added  
- Created a new script section in `clean_csv.ipynb` to filter out rows with latitude and longitude coordinates not located within Massachusetts.  
  - Exported the filtered dataset to a new file: `checkpoint8_mass_filtered.csv`.  

### Changed  
- Updated `.gitignore` to exclude:  
  -  `cache`  

- Updated `requirements.txt` to include spatial analysis and mapping libraries:  
  - `geopandas`, `networkx`, `osmnx`, `pyogrio`, `pyproj`, `scipy`, and `shapely`.  

### Notes  
- This update improves data accuracy by ensuring that only incidents occurring within Massachusetts are retained.  
- Added geospatial validation to enhance trustworthiness of further visualizations and crime trend analysis.  

## [0.2.2] - 2025-04-27  
### Changed  
- Updated `categorize_visualizations.ipynb` to load from `checkpoint5_hashed.csv` instead of `checkpoint2_geocoded.csv` at the start of the notebook.
- Reorganized code to define the `notebook_dir` and read from the correct checkpoints (`checkpoint5_hashed.csv`, `checkpoint6_category_crime_year.csv`).
- Added export of the updated dataframe to `checkpoint6_category_crime_year.csv` before creating figures.
- Standardized figure output directory creation after saving data.

### Added  
- Introduced serious crime classification logic based on an expanded FBI-style `SERIOUS_TYPES` set.
- Created a new column `crime_severity` that labels incidents as 'Serious' or 'Non-Serious' based on incident `Type`.
- Printed distribution counts of serious vs. non-serious crimes for verification.
- Exported the updated dataframe with `crime_severity` to `checkpoint7_serious_crimes.csv` for downstream analysis.

### Notes  
- This update standardizes the dataset for crime severity classification, preparing it for focused analysis and improved visualizations.

## [0.2.1] - 2025-04-21  
### Added  
- Created `hash.ipynb` notebook to generate anonymized hashed identifiers for individuals.  
- Loaded `checkpoint4_geocoded.csv` and defined a SHA-256 hashing function based on `Name` and `DOB`.  
- Applied hashing function only to rows with valid `Charges` to create a new `person_id` column.  
- Ensured null-safe and whitespace-trimmed hashing to avoid mismatches.  
- Exported the updated dataset to `checkpoint5_hashed.csv` in the `../data/checkpoints` directory.

### Notes  
- This step enables secure tracking of individuals across datasets without exposing sensitive information.

## [0.2.0] - 2025-04-21  
### Added  
- Created `geocode_part2.ipynb` notebook to merge geocoded latitude and longitude data with the existing `checkpoint3_geocoded.csv` file.  
- Read `geocoded_addresses_final.csv` and `checkpoint3_geocoded.csv` using `pandas` and constructed a full address for merging by appending `, Lawrence, MA` to the `Location` column.  
- Merged datasets on the cleaned address to fill in missing latitude and longitude values in `checkpoint3`.  
- Prioritized geocoded latitude and longitude where available, using `.combine_first()` to preserve existing values when necessary.  
- Removed helper columns (`address`, `geo_lat`, `geo_lon`, and `cleaned_address`) after the merge.  
- Saved the resulting dataframe as `checkpoint4_geocoded.csv` in the `../data/checkpoints` directory.

### Notes  
- This notebook is part of the second phase of geocoding integration, ensuring that all available coordinates are included 

## [0.1.9] - 2025-04-01
### Added
- Created `categorize_visualize.ipynb` notebook to group incident types into higher-level FBI-style crime categories.
- Mapped `Type` values into broader categories (e.g., `MOTOR_VEHICLE_INCIDENTS`, `PROPERTY_CRIMES`, `VIOLENT_AND_WEAPON_OFFENSES`, etc.).
- Calculated and visualized distribution of incidents by category using bar charts and sunburst plots.
- Created a new column `category` in the dataset to reflect these groupings.
- Generated yearly breakdown of incident categories and subtypes using `data_by_year` dictionary for interactive visualization.

### Visualizations
- Implemented a clean and interactive web dashboard (`incident_dashboard.html`) using Plotly.js.
  - Features: Year selector, bar chart for top-level categories, and dynamic sunburst chart for subcategories.
  - Saved output to `../Figures/incident_dashboard.html`.

### Changed
- Updated `requirements.txt` significantly:
  - Added libraries like `matplotlib`, `numpy`, `pdfminer.six`, `jupyter_client`, and many more for plotting, notebook compatibility, and dashboard generation.

### Notes
- This marks the first version to integrate full data visualization and categorical organization of incidents, preparing the dataset for deeper trend analysis.

## [0.1.8] - 2025-04-15
### Added
- Added `clean_address` function to clean up the `Location` field by removing unwanted parts.
- Applied `clean_address` function to the `Location` column in `checkpoint2`.
- Introduced geocoding functionality using `geopy` to obtain latitude and longitude for addresses.
- Implemented caching for geocoding results to improve performance and avoid duplicate requests.
- Logged addresses that could not be geocoded and any errors encountered during the process.
- Saved geocoded results to `checkpoint2_geocoded.csv`.
- Logged not found addresses to `not_found_addresses.txt`.
- Logged geocoding errors to `geocode_errors.txt`.

## [0.1.7] - 2025-03-21
### Added
- Added logic to separate the `Location` column into `Original Location`, `Location Prefix`, and `Location` (address only).
- Saved separated location output to `location_separation.csv` for intermediate review.
- Introduced `checkpoint1.csv` to save a backup of the cleaned dataset.
- Counted total vs. unique `Incident #` values and printed basic dataset statistics.
- Removed duplicate rows based on `Incident #` and stored result in `checkpoint1_no_dupes`.
- Filtered rows with non-empty `Charges` into `charges_only.csv` for manual review.
- Implemented function to unnest multiple arrests and associated charges from a single row using regex.
  - Preserved the original row for the first person listed.
  - Created new rows for additional individuals extracted from the `Charges` field.
  - Saved unnested output to `charges_unnested.csv`.
- Merged unnested charge data back into the cleaned base dataset and saved result as `checkpoint2.csv`.

### Changed
- Replaced uses of `target_csv_backup` with deduplicated checkpoints (`checkpoint1`, `checkpoint1_no_dupes`) in print statements and analysis.
- Updated URL cleaning in `Charges` to use `checkpoint1_no_dupes` instead of raw data.

## [0.1.6] - 2025-02-26
### Added
- Added `clean_csv.ipynb` for processing and cleaning police report CSV data.
  - Drops empty rows based on key columns ('Incident #', 'Date', 'Type', 'Location').
  - Removes invalid single-letter entries in 'Type'.
  - Cleans up unwanted newline characters and invalid suffixes in 'Type'.
  - Standardizes 'Location' formatting and extracts prefix/address.
  - Removes URLs from the 'Charges' column.
  - Saves a modified CSV for further review.
- Updated `requirements.txt` with dependencies required for data processing.

## [0.1.5] - 2025-02-05
### Fixed
- Fixed an issue where the script was running indefinitely due to missing a check for standard separators (`=` or `-`).
- Implemented logic to detect alternative separators when the standard ones are missing, preventing infinite loops.

### Added
- A logging mechanism that records skipped files and their detected separators in `skipped_files.csv`.
- Extracted a preview of the first 500 characters of text from skipped PDFs for debugging purposes.
- Additional print statements for better tracking of the directory structure while processing files.
- A .gitignore to ignore *.csv and *.pdf, global repo scoped

## Removed
-.gitignore from the data directory (only hid pdfs in that directory)

## [0.1.4] - 2025-02-01
### Added
- Created a changelog. This changelog was created retroactively based on commit history

## [0.1.3] - 2025-02-01
### Removed
- Removing pdfs that are not in our target year range(2014, 2016, 2017), i.e 2018-2024 (kept 2025, unsure if using 2025 data)

## [0.1.2] - 2025-01-30
### Added
- Adding code to convert_pdf() to check that each folder follows the same format     yyyy_law_pd_data
- script for web scraping LAW PD publicly available data
- added gitignore for the thousands of pdfs downloaded as a by-product ('*.pdf')

## [0.1.1] - 2025-01-22 
### Added
- Script to convert pdfs to csv

### Removed
- text files that the previous student created that could have vital missing log data
- Sample CSV files that contained data of three days of PD log

## [0.0.1] - 2025-01-22 *(Initial Development)*
- Project initialized.
- Repository setup with folder structure and inital data from previous student worker.
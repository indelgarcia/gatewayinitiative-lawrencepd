# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
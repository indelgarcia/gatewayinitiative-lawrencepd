# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/), and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

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
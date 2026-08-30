# CSV Data Cleaner & Excel Reporter

A Python-based data cleaning and validation tool that processes raw CSV order data and generates a structured Excel report.

## Overview

This project takes raw order data from a CSV file, cleans and validates the records, calculates order totals, identifies problematic records with specific reasons, and generates a formatted Excel report.

The goal is to automate repetitive data-cleaning and reporting tasks that would otherwise require manual spreadsheet work.

## Features

- Read order data from CSV files
- Clean text fields by removing unnecessary whitespace
- Parse and validate order dates
- Calculate total order value
- Separate valid and flagged records
- Identify specific validation issues
- Generate reasons for flagged records
- Generate Excel reports automatically
- Create separate sheets for:
  - Cleaned Data
  - Flagged Data
  - Summary
- Automatically adjust Excel column widths
- Bold Excel headers
- Freeze the header row for easier navigation
- Prevent duplicate output filenames
- Support simple filenames without requiring `.csv` or `.xlsx`

## Validation Rules

A record is flagged when:

- Customer name is missing
- Email is missing
- Quantity is zero or negative
- Unit price is zero or negative
- Status is missing
- Order date is invalid or missing

Each flagged record receives a `Reasons` field explaining the problem.

## Technologies Used

- Python
- Pandas
- OpenPyXL
- CSV
- Excel
- Git & GitHub

## Project Structure

csv_data_cleaner/
├── data/
├── output/
├── main.py
├── cleaner.py
├── validator.py
├── reports.py
├── ui.py
├── readme.md
├── .gitignore
└── tests/

## How It Works

CSV File
↓
Load Data
↓
Clean Data
↓
Validate Records
↓
Separate Valid / Flagged Data
↓
Calculate Summary
↓
Generate Excel Report
↓
Format Excel Workbook

## How to Run

1. Place your CSV file inside the `data` folder.

2. Run the program:

python main.py

3. Enter the CSV filename without the `.csv` extension.

Example:

orders_1500

4. Enter the desired Excel report filename without the `.xlsx` extension.

Example:

orders_report

The generated report will be placed inside the `output` folder.

## Excel Output

The generated workbook contains three sheets.

### Cleaned Data

Contains records that passed all validation rules.

### Flagged Data

Contains records that failed validation, along with the reasons they were flagged.

### Summary

Contains:

- Total Orders
- Total Line Items
- Total Cleaned Records
- Total Flagged Records
- Total Valid Sales
- Flagged Potential Value

## Testing

The project was tested using a dataset containing 1,500+ records, including both valid and intentionally invalid data.

Testing covered:

- Missing values
- Invalid dates
- Zero and negative quantities
- Zero and negative prices
- Missing status values
- Excel report generation
- Automatic column sizing
- Freeze panes
- Filename handling
- Invalid filename handling

## Future Improvements

Possible future improvements include:

- Automated unit tests
- More advanced Excel formatting
- Additional validation rules
- Duplicate record detection
- Support for additional input formats
- More detailed reporting and analytics

## Author

Piyush Naik

B.Tech CSE (AIML)
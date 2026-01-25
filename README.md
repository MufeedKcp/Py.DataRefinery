**PyDataRefinery: Customer Data ETL Pipeline**

PyDataRefinery is a Python-based ETL (Extract, Transform, Load) utility designed to sanitize and validate raw customer data. It transforms inconsistent "dirty" datasets into structured, analysis-ready CSV files while providing a detailed audit trail of data quality issues.

 > Overview

This project simulates a real-world data engineering task: taking raw, unvalidated source data and transforming it into a "source of truth." It handles common data issues like improper casing, invalid email formats, out-of-range numerical values, and duplicate records.

> Key Features

Data Normalization: Trims whitespace and applies Title Case to names; converts emails to lowercase.

Email Validation: Uses Regular Expressions (Regex) to ensure valid email structures.

Boundary Checks: Validates that ages are integers between 1 and 100.

Deduplication: Implements set-based hashing to identify and remove duplicate records based on unique Customer IDs.

Automated QA Reporting: Generates a data_quality_report.txt providing metrics on dropped records and specific error types.

> Project Structure
PyDataRefinery/
├── customers_raw.csv        # Input: Raw landing zone
├── cleaned_data.csv         # Output: Sanitized data
├── data_quality_report.txt  # Audit: Quality metrics
├── refinery.py                  # Core ETL logic
└── README.md                    # Documentation

> Validation Rules

The pipeline filters out records that fail the following criteria:

Name: Field cannot be empty.

Email: Must follow standard format (containing @ and a domain).

Age: Must be a valid integer between 1 and 100.

Uniqueness: Customer ID must not have appeared previously in the dataset.


> Prerequisites

Python 3.x

Ensure your input file is located at data/customers_raw.csv.

> Installation

Clone the repository:

git clone https://github.com/MufeedKcp/Py.DataRefinery.git


Navigate to the project directory:

cd Py.DataRefinery

> Running the Pipeline

Simply run the Python script:

python refinery.py

> Milestone

This project represents Day 25 of my Python learning journey, focused on building robust, reusable data pipelines.

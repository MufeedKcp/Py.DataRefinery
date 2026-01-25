PyDataRefinery — Customer Data ETL Pipeline

PyDataRefinery is a Python-based ETL (Extract, Transform, Load) pipeline that cleans, validates, and standardizes raw customer data into analysis-ready datasets while generating a comprehensive data quality audit.

This project demonstrates real-world data engineering fundamentals, including data validation, deduplication, and quality reporting using Python.

> Project Overview

In real production environments, raw data is often inconsistent, incomplete, and unreliable.
PyDataRefinery simulates this challenge by transforming unvalidated CSV data into a clean, trustworthy dataset suitable for analytics and downstream processing.

The pipeline enforces strict validation rules, removes bad records, and produces a detailed data quality report to ensure transparency and traceability.

> Key Features

Data Cleaning & Normalization

Trims whitespace

Standardizes name casing

Converts emails to lowercase

Data Validation

Regex-based email format validation

Age validation with boundary checks (1–100)

Mandatory field enforcement

Deduplication Logic

Removes duplicate records using Customer ID hashing

Data Quality Reporting

Automatically generates a detailed audit report

Tracks dropped records and failure reasons

> Validation Rules

Records are retained only if all conditions pass:

Name must not be empty

Email must contain @ and a valid domain

Age must be an integer between 1 and 100

Customer ID must be unique

📁 Project Structure
PyDataRefinery/
│
├── customers_raw.csv        # Raw input data
├── cleaned_data.csv         # Cleaned output dataset
├── data_quality_report.txt  # Data quality audit
│
├── refinery.py                  # Core ETL pipeline
└── README.md                    # Documentation


> Prerequisites

Python 3.x

Input file located at data/customers_raw.csv

> Installation
git clone https://github.com/MufeedKcp/Py.DataRefinery.git
cd Py.DataRefinery

> Run the Pipeline
python refinery.py

 Sample Data Quality Report
DATA QUALITY REPORT
====================
Total processed: 16
Clean records:   8
Dropped records: 8

Issue Breakdown:
- Missing Names:     0
- Missing Emails:    1
- Invalid Emails:    1
- Missing Age:       1
- Invalid Age:       4
- Duplicate IDs:     1


> Concepts Used

Python (CSV processing, regex, file I/O)

Simple ETL pipeline design

Data validation & cleansing

Deduplication strategies

Data quality monitoring

Defensive programming

> Milestone

Built as Day 25 of my Python learning journey, focused on designing robust, reusable data pipelines aligned with real-world data engineering workflows.

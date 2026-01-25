![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-success) ![ETL](https://img.shields.io/badge/Project-ETL%20Pipeline-orange) ![License](https://img.shields.io/badge/License-MIT-lightgrey) ![Data Engineering](https://img.shields.io/badge/Focus-Data%20Engineering-purple)

# **PyDataRefinery — Customer Data ETL Pipeline**
PyDataRefinery is a Python-based ETL (Extract, Transform, Load) pipeline that cleans, validates, and standardizes raw customer data into analysis-ready datasets while generating a comprehensive data quality audit.

This project demonstrates real-world data engineering fundamentals, including data validation, deduplication, and quality reporting using Python.

🔍 Project Overview

In real production environments, raw data is often inconsistent, incomplete, and unreliable.
PyDataRefinery simulates this challenge by transforming unvalidated CSV data into a clean, trustworthy dataset suitable for analytics and downstream processing.

The pipeline enforces strict validation rules, removes bad records, and produces a detailed data quality report to ensure transparency and traceability.

✨ Key Features

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

🛠️ Validation Rules

Records are retained only if all conditions pass:

Name must not be empty

Email must contain @ and a valid domain

Age must be an integer between 1 and 100

Customer ID must be unique

📁 Project Structure
PyDataRefinery/
│
├── data/
│   ├── customers_raw.csv        # Raw input data
│   ├── cleaned_data.csv         # Cleaned output dataset
│   └── data_quality_report.txt  # Data quality audit
│
├── refinery.py                  # Core ETL pipeline
└── README.md                    # Documentation

🚀 Getting Started
Prerequisites

Python 3.x

Input file located at data/customers_raw.csv

Installation
git clone https://github.com/MufeedKcp/Py.DataRefinery.git
cd Py.DataRefinery

Run the Pipeline
python refinery.py

📊 Sample Data Quality PyDataRefinery — Customer Data ETL Pipeline Report
DATA QUALITY REPORT
====================
Total processed: 100
Clean records:   85
Dropped records: 15

Issue Breakdown:
- Missing Names:     2
- Invalid Emails:    5
- Invalid Age:       3
- Duplicate IDs:     5

🧠 Skills Demonstrated

Python (CSV processing, regex, file I/O)

ETL pipeline design

Data validation & cleansing

Deduplication strategies

Data quality monitoring

Defensive programming

🎯 Milestone

Built as Day 25 of my Python learning journey, focused on designing robust, reusable data pipelines aligned with real-world data engineering workflows.

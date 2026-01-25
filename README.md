![Python](https://img.shields.io/badge/Python-3.x-blue) ![Status](https://img.shields.io/badge/Status-Completed-success) ![ETL](https://img.shields.io/badge/Project-ETL%20Pipeline-orange) ![License](https://img.shields.io/badge/License-MIT-lightgrey) ![Data Engineering](https://img.shields.io/badge/Focus-Data%20Engineering-purple)

<h1 align="center"><b>PyDataRefinery — Customer Data ETL Pipeline</b></h1> <p align="center">Python-based data cleaning, validation & quality reporting</p>
📌 Project Snapshot

Project Type: Data Engineering / ETL
Language: Python
Input: Raw CSV customer data
Output: Cleaned CSV + Data Quality Audit Report

🚀 Overview

PyDataRefinery is a Python-based ETL (Extract, Transform, Load) utility designed to sanitize and validate raw customer data.
It transforms inconsistent and unvalidated datasets into structured, analysis-ready CSV files while generating a detailed audit trail of data quality issues.

This project simulates a real-world data engineering workflow where raw data must be converted into a reliable “source of truth.”

✨ Key Features

Data Normalization

Trims whitespace from names

Applies Title Case formatting

Converts emails to lowercase

Data Validation

Regex-based email format checks

Age validation with strict boundary enforcement

Mandatory field verification

Deduplication

Identifies duplicate records using Customer ID hashing

Retains only the first valid occurrence

Automated Quality Reporting

Generates a detailed data_quality_report.txt

Tracks dropped records and failure reasons

🛠️ Validation Rules

Records are retained only if all rules pass.

Name

Cannot be empty

Whitespace trimmed and standardized

Email

Converted to lowercase

Must contain @ and a valid domain

Age

Must be an integer

Valid range: 1–100

Customer ID

Must be unique across the dataset

📁 Project Structure
PyDataRefinery/
│
├── data/
│   ├── customers_raw.csv        # Raw input data
│   ├── cleaned_data.csv         # Cleaned output dataset
│   └── data_quality_report.txt  # Data quality audit
│
├── refinery.py                  # Core ETL pipeline logic
└── README.md                    # Project documentation

🚦 Getting Started
Prerequisites

Python 3.x

Input file located at data/customers_raw.csv

Installation
git clone https://github.com/MufeedKcp/Py.DataRefinery.git
cd Py.DataRefinery

▶️ Running the Pipeline

Execute the ETL process using:

python refinery.py


The script will:

Read raw customer data

Apply validation and cleaning rules

Write clean records to cleaned_data.csv

Generate a data quality audit report

📊 Sample Output Report
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

Python (CSV handling, regex, file I/O)

ETL pipeline design

Data validation and cleansing

Deduplication strategies

Data quality monitoring

Defensive programming

🎯 Milestone

This project represents Day 25 of my Python learning journey, focused on building robust, reusable ETL pipelines aligned with real-world data engineering practices.

PyDataRefinery: Customer Data ETL Pipeline
PyDataRefinery is a Python-based ETL (Extract, Transform, Load) utility designed to sanitize and validate raw customer data. It transforms inconsistent "dirty" datasets into structured, analysis-ready CSV files while providing a detailed audit trail of data quality issues.
 Features
Name Standardization: Automatically trims whitespace and applies Title Case to all entries.
Robust Email Validation: Uses Regular Expressions (Regex) to verify email syntax and domain existence.
Age Boundary Validation: Ensures age data is an integer within a logical range (1–99).
Deduplication Engine: Identifies and removes duplicate records based on unique Customer IDs.
Data Quality Reporting: Generates an automated .txt report summarizing "Clean" vs. "Dropped" records for audit purposes.
🛠️ How It Works
The script follows a strict validation logic:
Extract: Reads raw data from data/customers_raw.csv.
Transform:
Checks for missing or null values.
Validates formats (Regex for emails, Integer conversion for age).
Tracks unique IDs in a Python set() for O(1) deduplication.
Load: Writes clean records to data/cleaned_data.csv and logs errors to data_quality_report.txt.
📁 Project Structure
code
Text
PyDataRefinery/
│
├── data/
│   ├── customers_raw.csv        
│   ├── cleaned_data.csv        
│   └── data_quality_report.txt 
│
└── README.md      

🚦 Getting Started
Prerequisites
Python 3.x
A source file located at data/customers_raw.csv
Installation & Usage
Clone the repository:
code
Bash
git clone https://github.com/MufeedKcp/Py.DataRefinery.git
Navigate to the folder:
code
Bash
cd Py.DataRefinery
Run the pipeline:
code
Bash
python refinery.py
 Audit Report
After execution, the pipeline generates a report similar to this:
code
Text
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
🎓 About
This project was built on Day 25 of my Python learning journey, focusing on data integrity, file I/O operations, and functional programming.

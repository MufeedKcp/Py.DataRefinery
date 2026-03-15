# PyDataRefinery: Customer Data ETL Pipeline


**PyDataRefinery** is a simplest fform of Python-based ETL (Extract, Transform, Load) utility designed to sanitize and validate raw customer data. It transforms inconsistent "dirty" datasets into structured, analysis-ready CSV files while providing a detailed audit trail of data quality issues.

### Core Capbilities:
- **Data Normalization:** Trims whitespace and applies Title Case to names; converts emails to lowercase.
- **Email Validation:** Uses Regular Expressions (Regex) to ensure valid email structures.
- **Boundary Checks:** Validates that ages are integers between 1 and 100.
- **Deduplication:** Implements set-based hashing to identify and remove duplicate records based on unique Customer IDs.
- **Automated QA Reporting:** Generates a `data_quality_report.txt` providing metrics on dropped records and specific error types.

## 📁 Project Structure

```text
PyDataRefinery/
│
├── customers_raw.csv        # Input: Raw landing zone
├── cleaned_data.csv         # Output: Sanitized data
│── data_quality_report.txt  # Audit: Quality metrics
│
├── refinery.py                  # Core ETL logic
└── README.md                    # Documentation
```

### improvement maded:
- use pandas for better data cleaning
- use numpy to convert empty columns into numpy NaN
- use regular expression so it matches strings that are either empty or contain only whitespace 

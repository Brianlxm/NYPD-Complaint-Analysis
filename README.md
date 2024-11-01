# NYPD Complaint Analysis

Analysis of NYPD police misconduct records from the Civilian Complaint Review Board (CCRB), covering complaints, allegations, police officers, and penalties since 2000. This project uses an ETL pipeline and a relational database for streamlined data storage and analysis.

## Table of Contents

- [About the Dataset](#about-the-dataset)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)

---

### About the Dataset

The dataset, published by the Civilian Complaint Review Board (CCRB), includes all public records of complaints against New York Police Department members. It contains four tables:

1. **Police Officers** - Identifies officers and the number of complaints they’ve received.
2. **Complaints Against Police Officers** - Primary table with complaint details like dates, locations, and outcomes.
3. **Allegations Against Police Officers** - Details specific allegations, linking complainants to officers.
4. **Penalties** - Lists penalties and outcomes associated with complaints.

### Project Structure

```plaintext
NYPD-Complaint-Analysis/
├── data/                   # Raw data files (initial dataset files go here)
├── products/               # Folder for processed data outputs, reports, etc.
├── scripts/                # All ETL scripts (e.g., extract.py, transform.py)
├── database/
│   ├── schema.sql          # Database schema setup file
│   └── data_import.sql     # Script to import data into SQL Server
├── notebooks/              # Jupyter notebooks for data exploration and analysis
├── pipeline.yaml           # Pipeline configuration for ETL processes
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
└── .gitignore              # Files and folders to ignore in version control

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
```

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/brianlxm/NYPD-Complaint-Analysis.git
   cd NYPD-Complaint-Analysis
   ```

2. **Set up the Python Environment**
Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**

    - If using SQL Server locally, execute database/schema.sql to create tables.
    - Load data by running database/data_import.sql.
    - Alternatively, use .bak files if provided to restore the database.

### Setup
 - ETL Pipeline: Configure the pipeline in pipeline.yaml with paths and settings.
 - Jupyter Notebook: Run notebooks/ to explore and analyze the data.

### Usage
 - Run ETL: Execute the scripts in the scripts/ folder to load and transform data.
 - Analyze Data: Use Jupyter notebooks for exploring relationships and insights, such as:
    - Patterns in complaints by age, ethnicity, and background of officers.
    - Correlations between complaints and penalties or outcomes.

### Future Enhancements
Incorporate dashboards for visualizations.
Add machine learning models for predictive analysis.

### Contributors
 - Brian Lam: Initial setup and ETL pipeline.
 - [Collaborator Names]: Contributions welcome for analysis, dashboards, and other enhancements!
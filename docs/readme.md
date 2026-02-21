# **Python PySpark ETL Pipeline – Retail Sales Data**

This project is a backend data processing system designed using production best practices for retail sales. It automates ingestion, validation, enrichment, transformation, and analytics-ready data mart creation using Python, PySpark, AWS S3, and MySQL.

The pipeline is modular, secure, and optimized, supporting multiple environments (dev/QA/prod), Spark partitioning, business calculations like salesperson incentives, and automated cleanup for production-grade workflows.

---
## 🛠️ Tech Stack

* **Python 3.10** – Core programming language
* **PySpark** – Distributed data processing
* **MySQL** – Dimension tables & data marts
* **AWS S3** – Raw & processed data storage
* **Parquet** – Partitioned, analytics-ready storage
* **Faker** – Synthetic data generation
* **Docker** – Optional local Spark setup
* **Logging & Utilities** – Encryption,decryption, AWS clients, Spark session management, file handling

---
<h2 align="center">Data Architecture</h2>
<p align="center">
  <img src="architecture.png" width="600">
</p>

<h2 align="center">Data Model</h2>
<p align="center">
  <img src="database_schema.drawio.png" width="600">
</p>">
---

##  Key Features

* **Backend Data Processing:** Retrieves raw files from AWS S3, validates schemas, and prepares structured outputs for analytics.
* **Layered Architecture:** Modular Python packages separate file handling, database access, business transformations, and utilities for maintainability.
* **Secure AWS Integration:** Encrypted credentials with custom modules; controlled read/write operations.
* **Multiple Environments:** Separate configs for dev, QA, and prod with environment-specific credentials, S3 buckets, and database connections.
* **Schema Validation:** Detects missing mandatory columns; separates invalid files for auditing.
* **Data Enrichment:** Joins raw sales data with MySQL dimension tables — Customers, Stores, Products, Sales Team.
* **Customer Data Mart:** Aggregates total purchases per customer.
* **Sales Team Data Mart:** Calculates monthly sales, salesperson rankings, and incentives using Spark window functions.
* **Spark Optimization & Partitioning:**

  * Writes partitioned Parquet files by `sales_month` and `store_id` for analytics performance.
  * Uses window functions for ranking and aggregations.
* **Business Calculations:** Incentive calculation for top-ranked salespersons (1% of total sales).
* **Automated Cleanup & Staging Update:** Moves processed files to S3, deletes local temporary files, and updates MySQL staging table status.
* **Production-Ready Execution:** Docker-based Spark setup, centralized logging, and environment-specific configs ensure consistent behavior across systems.
* 
---

#  Project Structure
A modular **AWS + Spark + MySQL + S3 based data processing pipeline** supporting multiple environments (**dev, qa, prod**) with transformation jobs for staging, dimension, and mart tables.

```
my_project/
│
├── docs/                                  # Documentation and README
│   └── readme.md
│
├── resources/
│   ├── __init__.py
│   │
│   ├── dev/                               # AWS, MySQL, S3 configs (dev)
│   │   ├── config.py
│   │   └── requirement.txt
│   │
│   ├── qa/                                # AWS, MySQL, S3 configs (qa)
│   │   ├── config.py
│   │   └── requirement.txt
│   │
│   ├── prod/                              # AWS, MySQL, S3 configs (prod)
│   │   ├── config.py
│   │   └── requirement.txt
│   │
│   └── sql_scripts/                       # Dimension & staging table creation
│       └── table_scripts.sql
│
├── src/
│   ├── main/
│   │   ├── __init__.py
│   │
│   │   ├── delete/                        # Delete operations
│   │   │   ├── aws_delete.py
│   │   │   ├── database_delete.py
│   │   │   └── local_file_delete.py
│   │   │
│   │   ├── download/                      # Download from S3
│   │   │   └── aws_file_download.py
│   │   │
│   │   ├── move/                          # File movement logic
│   │   │   └── move_files.py
│   │   │
│   │   ├── read/                          # Read from AWS / Database
│   │   │   ├── aws_read.py
│   │   │   └── database_read.py
│   │   │
│   │   ├── transformations/               # Data transformation layer
│   │   │   └── jobs/
│   │   │       ├── customer_mart_sql_transform_write.py
│   │   │       ├── sales_mart_sql_transform_write.py
│   │   │       ├── dimension_tables_join.py
│   │   │       └── main.py
│   │   │
│   │   ├── upload/                        # Upload to S3
│   │   │   └── upload_to_s3.py
│   │   │
│   │   ├── utility/                       # Common utilities
│   │   │   ├── encrypt_decrypt.py
│   │   │   ├── logging_config.py
│   │   │   ├── s3_client_object.py
│   │   │   ├── spark_session.py
│   │   │   └── my_sql_session.py
│   │   │
│   │   └── write/                         # Write to DB / Parquet
│   │       ├── database_write.py
│   │       └── parquet_write.py
│   │
│   └── test/
│       ├── scratch_pad.py
│       └── generate_csv_data.py
```

---

# ⚙️ Environment Configuration

Each environment maintains separate


## Step-by-Step Implementation

* **Data Generation:** Customers, stores, products, salespersons, and transactions generated with Faker.
* **AWS S3 Integration:** Secure download of raw CSVs, upload of processed Parquet files.
* **Schema Validation:** Checks mandatory columns and separates invalid files.
* **Data Enrichment:** Joins raw data with MySQL dimension tables for analytics-ready facts.
* **Data Mart Creation:**

  * **Customer Data Mart:** Total purchases per customer.
  * **Sales Team Data Mart:** Monthly sales, rankings, incentives.
* **Partitioning & Spark Optimization:**

  * Writes partitioned Parquet by `sales_month` and `store_id`.
  * Uses window functions for ranking and aggregations.
* **Business Calculations:** Incentive for top-ranked salesperson (1% of total sales).
* **Cleanup & Staging Table Update:**

  * Moves processed files to S3.
  * Deletes local temporary files.
  * Updates MySQL staging table status.
* **Production Readiness:**

  * Docker-based Spark setup for local testing.
  * Centralized logging for audit and debugging.
  * Environment-specific configs ensure consistency across dev, QA, and production.
---
##  Performance Observations (Local Execution)

* **Dataset Size & Storage**
  * Tested with **~500,000** synthetic retail transactions.
  * Converting raw CSV files (**~1.9 GB** total) into Parquet reduced storage size to **~780 MB** (**~59% reduction**), making it easier to handle large datasets locally.

* **Query Performance**
  * A simple aggregation query (total sales per month) improved from **~14 seconds** to **~8 seconds** (**~43% faster**) after switching from CSV to Parquet.
  * Partitioning Parquet files by `sales_month` and `store_id` reduced query time for monthly analytics from **~11.5 seconds** to **~8 seconds** (**~31% improvement**), showing the benefit of Spark partitioning even on a local machine.

* **ETL Execution Time**
  * End-to-end ETL execution for **~500k records** finished in **~1–2 minutes** on an 8–16 GB RAM laptop.
  * This made it feasible to test the full pipeline without long waiting times.

---
 **Final Deliverables**

* Automated ETL pipeline: S3 → PySpark → MySQL → Parquet → S3
* Customer and Sales Team Data Marts with KPI calculations
* Partitioned and optimized Parquet storage
* Secure handling of AWS credentials
* Modular, layered architecture for maintainability and scalability
* Production-ready workflow with Docker, logging, and environment separation
* Synthetic dataset for testing and demos

---

 **How to Run the Project**

1. **Clone the repository**

   ```bash
   git clone <your_repo_url>
   cd Python-Pyspark-ETL
   ```

2. **Set up environment**

   * Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   * Configure AWS, MySQL, and environment settings in `resources/dev/config.py` (or QA/prod)

3. **Run locally with Docker Spark (optional)**

   * Start Spark session using Docker if needed for distributed execution

4. **Execute ETL pipeline**

   ```bash
   python src/main/transformations/jobs/main.py
   ```

5. **Check processed files**

   * Verify S3 for partitioned Parquet files and MySQL for updated data marts

---

**Author:** Utkarsh Reddy Nathala
**LinkedIn:** https://www.linkedin.com/in/utkarsh-reddy-nathala-b5b56728a/


________________________________________
                                   Python PySpark ETL Pipeline – Retail Sales Data

Project Overview
This project is a backend data processing system designed using production best practices for retail sales. It automates ingestion, validation, enrichment, transformation, and analytics-ready data mart creation using Python, PySpark, AWS S3, and MySQL.
The pipeline is modular, secure, and optimized, supporting multiple environments (dev/QA/prod), Spark partitioning, business calculations like salesperson incentives, and automated cleanup for production-grade workflows.
________________________________________
⚡ Tech Stack
•	Python 3.10 – Core programming language
•	PySpark – Distributed data processing and transformations
•	MySQL – Dimension tables and data mart storage
•	AWS S3 – Raw and processed data storage
•	Parquet – Partitioned analytics-ready storage
•	Faker – Synthetic data generation for testing
•	Docker – Optional local Spark setup
•	Logging & Utilities – Encryption/decryption, AWS clients, Spark session, file management
________________________________________
✅ Key Features
•	Backend Data Processing: Retrieves raw files from AWS S3, validates schemas, and prepares structured outputs for analytics.
•	Layered Architecture: Modular Python packages separate file handling, database access, business transformations, and utilities for maintainability.
•	Secure AWS Integration: Encrypted credentials with custom modules; controlled read/write operations.
•	Multiple Environments: Separate configs for dev, QA, and prod with environment-specific credentials, S3 buckets, and database connections.
•	Schema Validation: Detects missing mandatory columns; separates invalid files for auditing.
•	Data Enrichment: Joins raw sales data with MySQL dimension tables: Customers, Stores, Products, Sales Team.
•	Customer Data Mart: Aggregates total purchases per customer.
•	Sales Team Data Mart: Calculates monthly sales, salesperson rankings, and incentives; optimized with Spark window functions.
•	Spark Optimization & Partitioning:
o	Writes partitioned Parquet files by sales_month and store_id for analytics performance
o	Uses window functions for ranking and aggregations
•	Business Calculations: Incentive calculation for top-ranked salespersons (1% of total sales).
•	Automated Cleanup & Staging Update: Moves processed files to S3, deletes local temporary files, and updates MySQL staging table status.
•	Production-Ready Execution: Docker-based Spark setup, centralized logging, and environment-specific configs ensure consistent behavior across systems.
________________________________________
📂 Project Structure
Python-Pyspark-ETL/
├── docs/ # Documentation and README
├── resources/
│ ├── dev/
│ │ ├── config.py # AWS, MySQL, S3 configs (dev)
│ │ └── requirements.txt
│ ├── qa/
│ │ ├── config.py # AWS, MySQL, S3 configs (qa)
│ │ └── requirements.txt
│ ├── prod/
│ │ ├── config.py # AWS, MySQL, S3 configs (prod)
│ │ └── requirements.txt
│ └── sql_scripts/
│ └── table_scripts.sql # Dimension & staging table creation
├── src/
│ ├── main/
│ │ ├── delete/
│ │ │ ├── aws_delete.py
│ │ │ ├── database_delete.py
│ │ │ └── local_file_delete.py
│ │ ├── download/
│ │ │ └── aws_file_download.py
│ │ ├── move/
│ │ │ └── move_files.py
│ │ ├── read/
│ │ │ ├── aws_read.py
│ │ │ └── database_read.py
│ │ ├── transformations/jobs/
│ │ │ ├── customer_mart_sql_transform_write.py
│ │ │ ├── dimension_tables_join.py
│ │ │ ├── main.py
│ │ │ └── sales_mart_sql_transform_write.py
│ │ ├── upload/
│ │ │ └── upload_to_s3.py
│ │ ├── utility/
│ │ │ ├── encrypt_decrypt.py
│ │ │ ├── logging_config.py
│ │ │ ├── s3_client_object.py
│ │ │ ├── spark_session.py
│ │ │ └── mysql_connection.py
│ │ └── write/
│ │ ├── database_write.py
│ │ └── parquet_write.py
│ └── test/
│ ├── scratch_pad.py
│ └── generate_csv_data.py
├── .gitignore
├── requirements.txt
└── README.md
________________________________________
⚙️ Step-by-Step Implementation
1.	Synthetic Data Generation
o	Customers, stores, products, salespersons, and transactions generated with Faker.
2.	AWS S3 Integration
o	Secure download of raw CSVs, upload of processed Parquet files.
3.	Schema Validation
o	Checks mandatory columns and separates invalid files.
4.	Data Enrichment
o	Joins raw data with MySQL dimension tables for analytics-ready facts.
5.	Data Mart Creation
o	Customer Data Mart: Total purchases per customer
o	Sales Team Data Mart: Monthly sales, rankings, incentives
6.	Partitioning & Spark Optimization
o	Writes partitioned Parquet by sales_month and store_id
o	Uses window functions for ranking and aggregations
7.	Business Calculations
o	Incentive for top-ranked salesperson (1% of total sales)
8.	Cleanup & Staging Table Update
o	Moves processed files to S3
o	Deletes local temporary files
o	Updates MySQL staging table status
9.	Production Readiness
o	Docker-based Spark setup for local testing
o	Centralized logging for audit and debugging
o	Environment-specific configs ensure consistency across dev, QA, and production
📈 Performance Observations (Local Execution)
•	Tested with ~500,000 synthetic retail transactions.
•	Converting CSV to Parquet reduced storage by 55–65%.
•	Reading Parquet improved query performance by 35–45%.
•	Partitioning by sales_month and store_id reduced scan time by 30–40% for monthly analytics.
•	End-to-end ETL execution completed in 1–2 minutes on local dev environment (8–16 GB RAM).
________________________________________
📊 Final Deliverables
•	Automated ETL pipeline: S3 → PySpark → MySQL → Parquet → S3
•	Customer and Sales Team Data Marts with KPI calculations
•	Partitioned and optimized Parquet storage
•	Secure handling of AWS credentials
•	Modular, layered architecture for maintainability and scalability
•	Production-ready workflow with Docker, logging, and environment separation
•	Synthetic dataset for testing and demos
________________________________________
Author: Utkarsh Reddy Nathala
LinkedIn: https://www.linkedin.com/in/utkarsh-reddy-nathala
________________________________________


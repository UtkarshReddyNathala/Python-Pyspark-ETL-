import os

# Encryption settings
key = "retail_sales_key"
iv = "retail_sales_iv"
salt = "retail_sales_salt"

# AWS Credentials (store encrypted in real projects)
aws_access_key = "AWS_ENCRYPTED_ACCESS_KEY"
aws_secret_key = "AWS_ENCRYPTED_SECRET_KEY"

bucket_name = "retail-sales-data-bucket"

s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"

# -------------------------------
# Database Configuration
# -------------------------------

database_name = "retail_sales_db"

url = f"jdbc:mysql://localhost:3306/{database_name}"

properties = {
    "user": "MYSQL_USER",
    "password": "MYSQL_PASSWORD",
    "driver": "com.mysql.cj.jdbc.Driver"
}

# -------------------------------
# Table Names
# -------------------------------

customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

# Data Mart Tables
customer_data_mart_table = "customer_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = [
    "customer_id",
    "store_id",
    "product_name",
    "sales_date",
    "sales_person_id",
    "price",
    "quantity",
    "total_cost"
]

# -------------------------------
# Local File Paths
# -------------------------------

base_local_path = "C:\\data_engineering\\spark_data\\"

local_directory = os.path.join(base_local_path, "file_from_s3")
customer_data_mart_local_file = os.path.join(base_local_path, "customer_data_mart")
sales_team_data_mart_local_file = os.path.join(base_local_path, "sales_team_data_mart")
sales_team_data_mart_partitioned_local_file = os.path.join(base_local_path, "sales_partition_data")
error_folder_path_local = os.path.join(base_local_path, "error_files")

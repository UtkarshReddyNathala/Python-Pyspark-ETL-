import os
from resources.dev import config
from src.main.utility.s3_client_object import *
from src.main.utility.encrypt_decrypt import *
from src.main.utility.logging_config import logger

# Initialize S3 client
s3_client_provider = S3ClientProvider(
    decrypt(config.aws_access_key),
    decrypt(config.aws_secret_key)
)
s3_client = s3_client_provider.get_client()

local_base_path = "C:\\Users\\Utkarsh\\Documents\\data_engineering\\spark_data\\sales_data_to_s3\\"

def upload_to_s3(s3_directory, s3_bucket, local_base_path):
    """
    Upload all files from local_base_path to the given S3 bucket and directory.
    """
    s3_prefix = s3_directory.rstrip("/")  # remove trailing slash if any
    try:
        for root, dirs, files in os.walk(local_base_path):
            for file in files:
                file_full_path = os.path.join(root, file)
                s3_key = f"{s3_prefix}/{file}"
                s3_client.upload_file(file_full_path, s3_bucket, s3_key)
                logger.info(f"Uploaded {file_full_path} → {s3_bucket}/{s3_key}")
        return f"Files uploaded successfully to {s3_bucket}/{s3_prefix}"
    except Exception as e:
        logger.error(f"Error uploading files: {str(e)}")
        raise e

# Usage
s3_directory = "sales_data"
s3_bucket = "retail-sales-data-bucket"
upload_to_s3(s3_directory, s3_bucket, local_base_path)

from src.main.utility.logging_config import *
import traceback
import datetime
import os

class UploadToS3:
    def __init__(self, s3_client):
        self.s3_client = s3_client

    def upload_to_s3(self, s3_directory, s3_bucket, local_file_path):
        current_epoch = int(datetime.datetime.now().timestamp()) * 1000
        s3_prefix = f"{s3_directory}/{current_epoch}/"

        try:
            for root, dirs, files in os.walk(local_file_path):
                for file in files:
                    file_full_path = os.path.join(root, file)  # fixed: don't overwrite parameter
                    s3_key = f"{s3_prefix}/{file}"
                    self.s3_client.upload_file(file_full_path, s3_bucket, s3_key)
                    logger.info(f"Uploaded file: {file_full_path} → s3://{s3_bucket}/{s3_key}")

            return f"Data successfully uploaded to {s3_directory} data mart."

        except Exception as e:
            logger.error(f"Error uploading file: {str(e)}")
            print(traceback.format_exc())
            raise e

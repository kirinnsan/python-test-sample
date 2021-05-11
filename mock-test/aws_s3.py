import boto3
from botocore.errorfactory import ClientError


class S3_Class:
    def download(self, file_name, file_path):
        try:
            s3_client = boto3.client("s3")
            obj = s3_client.download_file(
                "moto-example", "data/" + file_name, file_path)
        except ClientError:
            return False
        return True

    def upload(self, file_path, file_name) -> bool:
        try:
            s3_client = boto3.client("s3")
            _ = s3_client.upload_file(
                file_path, "moto-example", "data/" + file_name)
        except ClientError:
            return False
        return True

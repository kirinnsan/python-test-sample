from moto import mock_s3
import boto3
import pytest
import aws_s3


class TestS3Methods():
    bucket = "moto-example"

    @mock_s3
    def test_upload_succeed(self):
        # バケットの生成
        s3 = boto3.client("s3")
        s3.create_bucket(Bucket=TestS3Methods.bucket)

        s3_class = aws_s3.S3_Class()
        assert s3_class.upload("./data/example.txt", "example.txt")

        # アップロードされたファイルをGet
        # body = s3.Object(TestS3Methods.bucket,
        #                  "data/example.txt").get()["Body"].read().decode("utf-8")

        assert body == "Hello, world!"

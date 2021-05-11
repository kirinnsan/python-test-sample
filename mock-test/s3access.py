# -*- coding:utf-8 -*-
import boto3
import os.path


class S3Access:
    s3 = None

    def __init__(self):
        self.s3 = boto3.client('s3')

    def upload(self, bucketname, uploadfilepath, s3folder):
        """
        S3へアップロード
        @param bucketname S3バケット名
        @param uploadfilepath アップロードするファイルのパス
        @param s3folder S3バケットの下のフォルダパス（ファイル名は含まない）
        """
        basefilename = os.path.basename(uploadfilepath)
        s3filepath = s3folder + '/' + basefilename
        self.s3.upload_file(uploadfilepath, bucketname, s3filepath)


class MyClass:

    def get_partition_values(self, bucket_str: str, prefix: str, partition_column: str) -> set([str]):
        print(
            f"get all values for {partition_column} in s3://{bucket_str}/{prefix}")
        s3 = boto3.client('s3')
        common_prefix = prefix.strip("/") + "/" + partition_column + "="
        objs = s3.list_objects_v2(
            Bucket=bucket_str, Prefix=prefix, Delimiter='/')
        print(objs)
        if objs["KeyCount"] > 0:
            partition_values = {obj['Prefix'].replace(common_prefix, "").strip(
                "/") for obj in objs["CommonPrefixes"]}
            return partition_values
        else:
            return set()

    def get_partition_values2(self, bucket_str: str, prefix: str, partition_column: str) -> set([str]):
        print(
            f"get all values for {partition_column} in s3://{bucket_str}/{prefix}")
        s3 = boto3.client('s3')
        s3.list_objects_v2(
            Bucket=bucket_str, Prefix=prefix, Delimiter='/')

    def get_partition_values3(self, bucket_str: str, prefix: str, partition_column: str) -> set([str]):
        print(
            f"get all values for {partition_column} in s3://{bucket_str}/{prefix}")
        s3 = boto3.client('s3')
        result = s3.list_objects_v2(
            Bucket=bucket_str, Prefix=prefix, Delimiter='/')
        s3.upload_file(
            Bucket=bucket_str, Prefix=result, Delimiter='/')
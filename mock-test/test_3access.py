# -*- coding:utf-8 -*-
from unittest import TestCase, mock
from s3access import S3Access
from s3access import MyClass
import boto3

# from moto import mock_s3

import sys
import os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')


class TestS3Access():

    # @mock_s3
    def test_s3_upload(self):
        # 初期化
        bucketname = 'testbucket001'
        prefix = 'firstfolder'

        # テスト準備(バケット、オブジェクト作成）
        s3test = boto3.client('s3')
        s3test.create_bucket(Bucket=bucketname)
        s3test.put_object(Bucket=bucketname, Key=prefix)

        # テスト対象のオブジェクト生成
        s3 = S3Access()
        # 対象メソッド実行
        s3.upload('./test.md', bucketname, prefix)

        # 実行結果確認
        # アップロード済みの情報をS3から読み込む
        keyname = prefix + '/test.md'
        response = s3test.get_object(Bucket=bucketname, Key=keyname)
        body = response['Body'].read().decode('utf-8').encode('utf-8')
        # アップロードしたファイルを読み込む
        fp = open(keyname, 'r')
        readStr = fp.read()
        fp.close
        # 結果確認
        assert body == readStr


class MyTest(TestCase):

    def test_s3(self):
        object_result_dict = {'ResponseMetadata': {}, 'IsTruncated': False, 'Name': 'mybucket', 'Prefix': 'foo/bar/', 'Delimiter': '/',
                              'CommonPrefixes': [{'Prefix': 'foo/bar/partition_column=2019-01-01/'},
                                                 {'Prefix': 'foo/bar/partition_column=2019-01-02/'},
                                                 {'Prefix': 'foo/bar/partition_column=2019-10-10/'}],
                              'KeyCount': 3}
        with mock.patch('s3access.boto3.client') as mocked_boto3:
            mocked_boto3.return_value.list_objects_v2.return_value = object_result_dict
            days = MyClass().get_partition_values(bucket_str="mybucket",
                                                  prefix="foo/bar/",
                                                  partition_column="partition_column")
            assert (days == {'2019-01-01', '2019-01-02', '2019-10-10'})

    def test_s3_list_objects_v2(self):
        """s3のlist_objects_v2メソッドをモック化
        Note:
        s3モックの参考
        https://gist.github.com/mirkoprescha/32e109b0a9f790f04f9ddac337691379
        複雑なモックオブジェクトの作成
        mock.connection.cursor().execute("SELECT 1") のような複雑なケースでモックを使いたい場合
        https://docs.python.org/ja/3.7/library/unittest.mock-examples.html
        """
        list_mock = mock.Mock()
        # boto3.clientをモック化
        with mock.patch('s3access.boto3.client') as mocked_boto3:
            # list_objects_v2をただのモックオブジェクトに入れ替え
            mocked_boto3.return_value.list_objects_v2 = list_mock
            MyClass().get_partition_values2(bucket_str="mybucket",
                                            prefix="foo/bar/",
                                            partition_column="partition_column")
            # 呼び出しと引数チェック
            list_mock.assert_called_with(
                Bucket="mybucket", Prefix="foo/bar/", Delimiter='/')

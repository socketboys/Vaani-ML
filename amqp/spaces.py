import boto3
from boto3.s3.transfer import S3Transfer
from botocore.client import BaseClient


class Spaces:
    transfer: boto3.s3.transfer.S3Transfer

    def __init__(self):
        session = boto3.session.Session()
        client = session.client(
            's3',
            region_name='blr1',
            endpoint_url='https://backned.blr1.cdn.digitaloceanspaces.com/',
            aws_access_key_id="DO00Q89RLRRGNK7AZAUH",
            aws_secret_access_key="oaVwJJOlMlWwVTDJArVrahWsAVFbtmTxFriF7DNTLUY",
        )
        self.transfer = S3Transfer(client)

    def upload(self, filepath, bucket_path):
        self.transfer.upload_file(filepath, 'backned', bucket_path)
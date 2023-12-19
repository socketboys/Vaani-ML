import boto3
from botocore.client import BaseClient


class Spaces:
    session: boto3.session.Session
    client: BaseClient

    def __init__(self):
        self.session = boto3.session.Session()
        self.client = self.session.client(
            's3',
            region_name='blr1',
            endpoint_url='https://backned.blr1.cdn.digitaloceanspaces.com/',
            aws_access_key_id="DO00Q89RLRRGNK7AZAUH",
            aws_secret_access_key="oaVwJJOlMlWwVTDJArVrahWsAVFbtmTxFriF7DNTLUY",
        )

    def upload(self):
        self.session

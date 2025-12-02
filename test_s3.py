import os
if os.path.isfile("env.py"):
    import env

import boto3

bucket_name = os.environ.get("AWS_STORAGE_BUCKET_NAME")
print("Bucket name:", bucket_name)  # must print 'sjcibucket6942'

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"),
    region_name="eu-north-1"
)

response = s3.list_objects_v2(Bucket=bucket_name)
print(response)

import boto3 
import random
"""
   Description: 
        This function  generates a name with random numbers for the s3 bucket name.

    
   Arguements: 
        bucket_prefix, random.random and bucket location "us-east-2"

    Returns:
        It returns the unique name created
    

"""
bucket_prefix = "pythonboto-1" # bucket name variable

s3_client = boto3.client('s3') # boto3 cleint variable

def bucket_indentifier(bucket_prefix):
    return ''.join([bucket_prefix, str(random.random())])

response = s3_client.create_bucket(
    Bucket= bucket_indentifier(bucket_prefix),
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2',
    },
)

print(response)

#random.seed(10)
#print(random.random())
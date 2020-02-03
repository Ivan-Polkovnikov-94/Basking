import os
import boto3
import botocore
from botocore.config import Config

os.environ['COGNITO_USERNAME'] = 'ivan.polkovnikov.94@gmail.com'
os.environ['COGNITO_USER_PASSWORD'] = 'P@ssw0rd'
os.environ['COGNITO_CLIENT_ID'] = '7o5vqv7ukt9onolq1nvjt7m40e'

config = Config(signature_version=botocore.UNSIGNED)
cognito_client = boto3.client('cognito-idp', 'eu-central-1', config=config)
user_id = 'c3a388fb-db1a-409b-8065-de847482d432'


def get_token():
    response = cognito_client.initiate_auth(
        AuthFlow='USER_PASSWORD_AUTH',
        AuthParameters={
            'USERNAME': os.environ['COGNITO_USERNAME'],
            'PASSWORD': os.environ['COGNITO_USER_PASSWORD']
        },
        ClientId=os.environ['COGNITO_CLIENT_ID']
    )
    return response['AuthenticationResult']['IdToken']

# a = get_token()
# print(a)

import boto3
import random
import os

ses_client = boto3.client('ses', region_name="ap-northeast-1")


def lambda_handler(event, context):
    otp = generate_otp()
    send_otp_to_user(event['request']['userAttributes']['email'], otp)
    event['response']['publicChallengeParameters'] = {
        'EMAIL': event['request']['userAttributes']['email']}
    event['response']['privateChallengeParameters'] = {'answer': otp}
    event['response']['challengeMetadata'] = 'CUSTOM_CHALLENGE'
    return event


def generate_otp():
    return str(random.randint(100000, 999999))


def send_otp_to_user(email, otp):
    ses_client.send_email(
        Source=os.environ['SENDER_EMAIL'],
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': 'Your OTP'},
            'Body': {'Text': {'Data': 'Your OTP is ' + otp}}
        }
    )

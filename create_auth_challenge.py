import secrets
import boto3

# Create a new SES resource and specify a region.
client = boto3.client('ses', region_name="us-west-2")


def lambda_handler(event, context):
    if event['request']['session']:
        for sess in reversed(event['request']['session']):
            if sess['challengeResult']:
                event['response']['issueTokens'] = True
            else:
                event['response']['issueTokens'] = False
        return event

    # For the new authentication attempt, generate a new secret login code and mail it to the user
    # and setup the returned parameters to include the code parameter that the user will have to input
    secret_login_code = secrets.token_hex(20)
    event['response']['privateChallengeParameters'] = {
        'secretLoginCode': secret_login_code}
    event['response']['challengeMetadata'] = 'CUSTOM_CHALLENGE'

    # Your registered user's email
    user_email = 'USER_EMAIL'
    response = client.send_email(
        Destination={
            'ToAddresses': [
                user_email,
            ],
        },
        Message={
            'Body': {
                'Text': {
                    'Charset': 'UTF-8',
                    'Data': 'Your secret login code is ' + secret_login_code,
                },
            },
            'Subject': {'Charset': 'UTF-8', 'Data': 'Secret Login Code'},
        },
        Source='SENDER_EMAIL@DOMAIN.COM',  # Replace with your SES verified email
    )

    return event

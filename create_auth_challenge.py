import secrets

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
    event['response']['privateChallengeParameters'] = {'secretLoginCode': secret_login_code}
    event['response']['challengeMetadata'] = 'CUSTOM_CHALLENGE'

    # TODO: Add code to send the secret login code to the user's registered email

    return event

def lambda_handler(event, context):
    if event['request']['session']:
        # get the last challenge result
        for sess in reversed(event['request']['session']):
            challenge_result = sess['challengeResult']
            if challenge_result:
                event['response']['issueTokens'] = True
                event['response']['failAuthentication'] = False
            else:
                event['response']['issueTokens'] = False
                event['response']['failAuthentication'] = True
            return event

    # In this sample code, a single custom challenge is being used
    # If multiple custom challenges are needed, they can be sequenced here
    event['response']['issueTokens'] = False
    event['response']['failAuthentication'] = False
    event['response']['challengeName'] = 'CUSTOM_CHALLENGE'
    event['response']['challengeMetadata'] = 'CUSTOM_CHALLENGE'

    return event

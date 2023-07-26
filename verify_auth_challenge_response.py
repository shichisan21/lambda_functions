def lambda_handler(event, context):
    # Check the answer provided by the user
    if event['request']['privateChallengeParameters']['secretLoginCode'] == event['request']['challengeAnswer']:
        event['response']['answerCorrect'] = True
    else:
        event['response']['answerCorrect'] = False

    return event

def lambda_handler(event, context):
    is_correct = False
    if event['request']['privateChallengeParameters']['answer'] == event['request']['challengeAnswer']:
        is_correct = True
    event['response']['answerCorrect'] = is_correct
    return event

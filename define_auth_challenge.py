def lambda_handler(event, context):
    if "session" in event and event["session"]:
        for session in event["session"]:
            if session["challengeName"] == "CUSTOM_CHALLENGE" and session["challengeResult"]:
                event["response"]["issueTokens"] = True
                event["response"]["failAuthentication"] = False
            elif session["challengeName"] == "CUSTOM_CHALLENGE" and not session["challengeResult"]:
                event["response"]["issueTokens"] = False
                event["response"]["failAuthentication"] = True
    else:
        event["response"]["issueTokens"] = False
        event["response"]["failAuthentication"] = False
        event["response"]["challengeName"] = "CUSTOM_CHALLENGE"
    return event

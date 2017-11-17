import os, slackclient

JOHNSON_SLACK_NAME = os.environ.get('JOHNSON_SLACK_NAME')
JOHNSON_SLACK_TOKEN = os.environ.get('JOHNSON_SLACK_TOKEN')

# initialize slack client
johnson_slack_client = slackclient.SlackClient(JOHNSON_SLACK_TOKEN)

# check if everything is alright
print(JOHNSON_SLACK_NAME)
print(JOHNSON_SLACK_TOKEN)
is_ok = johnson_slack_client.api_call("users.list").get('ok')
print(is_ok)

# find the id of our slack bot
if(is_ok):
    for user in johnson_slack_client.api_call("users.list").get('members'):
        if user.get('name') == JOHNSON_SLACK_NAME:
            print(user.get('id'))

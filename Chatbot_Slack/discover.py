import os, slackclient

JOHNSONCB1_SLACK_NAME = os.environ.get('JOHNSONCB1_SLACK_NAME')
JOHNSONCB1_SLACK_TOKEN = os.environ.get('JOHNSONCB1_SLACK_TOKEN')

# initialize slack client
johnsoncb1_slack_client = slackclient.SlackClient(JOHNSONCB1_SLACK_TOKEN)

# check if everything is alright
print(JOHNSONCB1_SLACK_NAME)
print(JOHNSONCB1_SLACK_TOKEN)
is_ok = johnsoncb1_slack_client.api_call("users.list").get('ok')
print(is_ok)

# find the id of our slack bot
if(is_ok):
    for user in johnsoncb1_slack_client.api_call("users.list").get('members'):
        if user.get('name') == JOHNSONCB1_SLACK_NAME:
            print(user.get('id'))

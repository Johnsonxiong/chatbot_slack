########    read me   #############
#    Doing nothing, and pattern for chatbot johnsoncb1

# if want to change the chatbot, have to change the source.sh file
# and change the name 'Johnsoncb1' into your chatbot's name

##################################


import os, slackclient, time
import random

# delay in seconds before checking for new events 
SOCKET_DELAY = 1
# slackbot environment variables
JOHNSONCB1_SLACK_NAME = os.environ.get(' JOHNSONCB1_SLACK_NAME')
JOHNSONCB1_SLACK_TOKEN = os.environ.get(' JOHNSONCB1_SLACK_TOKEN')
JOHNSONCB1_SLACK_ID = os.environ.get(' JOHNSONCB1_SLACK_ID')
johnsoncb1_slack_client = slackclient.SlackClient(JOHNSONCB1_SLACK_TOKEN)
def is_for_me(event):
    # TODO Implement later
    return True
def handle_message(message, user, channel):
    # TODO Implement later
    post_message(message='Hello', channel=channel)
def post_message(message, channel):
    johnsoncb1_slack_client.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)
def run():
    if johnsoncb1_slack_client.rtm_connect():
        print('[.] Valet de Machin is ON...')
        while True:
            event_list = johnsoncb1_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    if is_for_me(event):
                        handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()

    

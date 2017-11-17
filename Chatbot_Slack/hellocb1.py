########    read me   #############
#   Can say hi and see you for chatbot johnsoncb1, but keep saying see you , still need to fix this bug

# if want to change the chatbot, have to change the source.sh file
# and change the name 'Johnsoncb1' into your chatbot's name

##################################


import os, slackclient, time
import random

# delay in seconds before checking for new events 
SOCKET_DELAY = 1
# slackbot environment variables
JOHNSONCB1_SLACK_NAME = os.environ.get('JOHNSONCB1_SLACK_NAME')
JOHNSONCB1_SLACK_TOKEN = os.environ.get('JOHNSONCB1_SLACK_TOKEN')
JOHNSONCB1_SLACK_ID = os.environ.get('JOHNSONCB1_SLACK_ID')
johnsoncb1_slack_client = slackclient.SlackClient(JOHNSONCB1_SLACK_TOKEN)

# check if everything is alright
print(JOHNSONCB1_SLACK_NAME)
print(JOHNSONCB1_SLACK_TOKEN)

def is_for_me(event):
    # TODO Implement later
    if event.get('text'):
        if "hi" in event.get('text') or "hello" in event.get('text') or "hey" in event.get('text') or "whatsup" in event.get('text'):
            return 1
        elif "bye" in event.get('text') or "cu" in event.get('text') or "see you" in event.get('text') or "See you" in event.get('text'):
            return 2
        
# how the bot is mentioned on slack
def get_mention(user):
    return '<@{user}>'.format(user=user)

johnsoncb1_slack_mention = get_mention(JOHNSONCB1_SLACK_ID)


def handle_message(message, user, channel, choice):
    # TODO Implement later
    if choice == 1:
        post_message(message='Hello, my friend', channel=channel)
    elif choice == 2:
        post_message(message='See you, my friend', channel=channel)
    else:
        c =1
def post_message(message, channel):
    johnsoncb1_slack_client.api_call('chat.postMessage', channel=channel,
                          text=message, as_user=True)
def run():
    print(JOHNSONCB1_SLACK_NAME)   # test use
    print(JOHNSONCB1_SLACK_TOKEN)  #test use
    if johnsoncb1_slack_client.rtm_connect():
        print("[.] Johnson's chatbot is ON...")
        while True:
            event_list = johnsoncb1_slack_client.rtm_read()
            if len(event_list) > 0:
                for event in event_list:
                    print(event)
                    handle_message(message=event.get('text'), user=event.get('user'), channel=event.get('channel'),choice =is_for_me(event))
 #                   elif is_for_me(event) == 0:
 #                       post_message(message='See you, my friend', channel=event.get('channel'))
                       # break
                    #else:
 #                       post_message(message='I dont understand what you are talking', channel=event.get('channel'))
            time.sleep(SOCKET_DELAY)
    else:
        print('[!] Connection to Slack failed.')

if __name__=='__main__':
    run()

    

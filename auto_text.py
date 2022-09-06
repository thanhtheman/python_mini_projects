from dotenv import load_dotenv
import os
import random
from twilio.rest import Client

load_dotenv()

motivation_quotes = ['Believe in yourself! Just do it. Yes, You can.', 
                    'Stand guard your mind! Thought will become words, words will become actions, actions will become habits, habits will become characters, characters will become your destiny ',
                    'Only quality people!',
                    'Find out what things are, not what you think they are.',
                    'Income makes you a living, Profit makes you a fortune.',
                    'You can achieve anything, but not everything!',
                    'Result = Attitude x Effort x Ability.',
                    'Fear is the disease, Hustle is the antidote.',
                    'Chart your own path, that is powerful.',
                    'Re-think your process and your goals...',
                    'Be stingy with your most valuable resource: time.',
                    'Nothing really matters in a few months or years.',
                    'Discipline & Consistency is more important than motivation and talent.']

account = os.getenv('TWILIO_ACCOUNT_SID')
token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone_number = os.getenv('TWILIO_PHONE_NUMBER')
target_phone_number = os.getenv('PHONE_NUMBER')

client = Client(account, token)


def send_message():
    index = random.randint(0, len(motivation_quotes)-1)
    message = client.messages.create(
    to= target_phone_number, 
    from_= twilio_phone_number,
    body= motivation_quotes[index])

    print(message.sid)

send_message()

# schedule.every(1).minutes.do(send_message)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


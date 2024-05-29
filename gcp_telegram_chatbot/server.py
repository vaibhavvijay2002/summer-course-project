import os

from google.cloud import texttospeech_v1
from google.cloud import translate_v2
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "vaibhav-gcp-2022-7be4e251ac90.json"

import logging
from telegram.ext import *
import responses

API_KEY = '5467706554:AAEmmB9pcSSXjeGH21phO5B2Qi7RPhEKMUc'

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)

'''
def predict_command(update, context):
    update.message.reply_text('This is a predict command')
    update.message.reply_text('enter id(1-1004)')
    #id = str(update.message.text)
    id = handle_message()
    update.message.reply_text('enter gender(Male/Female)')
    #gender = str(update.message.text)
    handle_message()
    update.message.reply_text('enter age(15-70)')
    #age = str(update.message.text)
    handle_message()
    update.message.reply_text('enter income(15-150)')
    #income = str(update.message.text)
    handle_message()
    predict()

def predict():
    url = "https://us-central1-aiplatform.googleapis.com/v1/projects/vaibhav-gcp-2022/locations/us-central1/endpoints/6836525806999568384:predict"
    content = {
        "instances": [{
    "mimeType": "multipart/form-data",
     "ID" : id,
    "Gender" : gender,
    "Age" : age,
    "income" : income
  }]
    }
    headers={
        'Authorization' : "Bearer ya29.c.b0AXv0zTNEdMu2j6PiyxZXkdQ8MI7qrM93DG7RFwdMZZHhiKM7_RT3pD5WsPY5tn8ztWKKtgrgNKfxKMelv2QXrTj_JXpU1_PzEzteG8QqcKQa38xY1ULkWMW4nCaiTPD8TBrmKvPtZuyJGYJWpwuX93pvA6efRXEWDkOXdNG4HJ4lhLG-tqcXdu2x5-me_opPU0AT1wlIWuxf8eUknx1X1-5W4HCcCRM",
        'content-type' : 'application/json'
    }

    #API CALL:
    response = requests.post(url,data=json.dumps(content),headers=headers)
    jsonres = json.loads(response.content)
    conf = jsonres["spendings"][2]

'''

def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
if __name__ == '__main__':
    updater = Updater(API_KEY, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('custom', custom_command))
  
    #dp.add_handler(CommandHandler('predict', predict_command))
    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(2.0)
    updater.idle()
import os
from dotenv import load_dotenv
import telebot

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

# print(BOT_TOKEN)
bot = telebot.TeleBot(BOT_TOKEN)

def main():
    try:
        
        @bot.message_handler(commands=['start', 'hello'])
        def send_welcome(message):
            bot.reply_to(message, "Hi, how can i help You!")

        @bot.message_handler(func=lambda msg: True)
        def echo_all(message):
            bot.reply_to(message, message.text)

        bot.infinity_polling()

    except:
        print("Something went Wrong!")

if __name__ == '__main__':
    main()
    

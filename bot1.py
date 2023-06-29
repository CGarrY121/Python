from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import Settings

logging.basicConfig(format = "%(asctime)s - %(levelname)s - %(message)s",
                    level = logging.INFO,
                    filename = "bot.log")

def greet_user(update,bot):
    text = "Вызван/start"
    logging.info(text)
    print(text)
    update.message.reply_text(text)

def talk_to_me(update,bot):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name,update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                update.message.chat.id, update.message.text )  
    print (update.message)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(Settings.API_KEY)

    logging.info("Bot started") 

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()



main()    
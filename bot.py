from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


def greet_user(bot, update):
    #print (update)
	#print('Вызван /start')
	bot.sendMessage(update.message.chat_id, text='Давай общаться!')

def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)

def main():
	updater = Updater("340001409:AAFcwZOplG1_o8pkJPrP4Xd4Q60gQcEu9Wk")

	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))

	dp.add_error_handler(show_error)

	updater.start_polling()
	updater.idle()


def show_error(bot, update, error):
    print(error)

main()

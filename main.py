from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("5154297631:AAGnyJ8FyWKyA0UYpfYuaXSEoivcYyDevS4",use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello sir, Welcome to the Bot.Please write /help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/github - To get the github URL
	/website - To get the website URL
         more function on the way....""")

def github_url(update: Update, context: CallbackContext):
	update.message.reply_text("GitHub URL :- https://github.com/mrpriyanshu")

def website_url(update: Update, context: CallbackContext):
	update.message.reply_text("Website Link :- https://mrpriyanshu.github.io/")

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()

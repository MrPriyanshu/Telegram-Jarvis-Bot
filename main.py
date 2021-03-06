import requests
from urllib.request import urlopen
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters

updater = Updater("Bot Api Token",use_context=True)

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello sir, Welcome to the Bot.Please write /help to see the commands available.")

def help(update: Update, context: CallbackContext):
	update.message.reply_text("""Available Commands :-
	/github - To get the github URL
	/website - To get the website URL
/programmingbooks - To get the URL to programming books website 
/quickfonts - To get the URL to QuickFonts website
/logs - To get the text in  log file (not working)
/linkshort1 - Link shortner (under development)
/linkshort2 - Link shortner (under development)
         more function on the way....""")

def github_url(update: Update, context: CallbackContext):
	update.message.reply_text("GitHub URL :- https://github.com/mrpriyanshu")

def website_url(update: Update, context: CallbackContext):
	update.message.reply_text("Website Link :- https://mrpriyanshu.github.io/")

#def log(update: Update, context: CallbackContext):
#url = "https://mrpriyanshu.github.io/resources/log.txt"
#file = urllib.request.urlopen(url)
#for line in file:
#decoded_line = line.decode("utf-8")
#update.message.reply_text(decoded_line)

def pbooks_url(update: Update, context: CallbackContext):
	update.message.reply_text("Programming Books Link :- https://mrpriyanshu.github.io/programmingbooks/")

def qf_url(update: Update, context: CallbackContext):
	update.message.reply_text("QuickFonts Link :- https://mrpriyanshu.github.io/QuickFonts/")

def short1(update: Update, context: CallbackContext):
  response = requests.get('https://linkshortify.com/api?api=fc200dd111632800cfe1abef39edb48b3cdb9051&url=yourdestinationlink.com')
  update.message.reply_text(response.text)

def short2(update: Update, context: CallbackContext):
  response = requests.get('https://linkbnao.com/api?api=8a9bc11b1b71ad2bbca524248dab5e4a4f56988f&url=yourdestinationlink.com')
  update.message.reply_text(response.text)

def unknown(update: Update, context: CallbackContext):
	update.message.reply_text("Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('github', github_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('website', website_url))
updater.dispatcher.add_handler(CommandHandler('programmingbooks', pbooks_url))
updater.dispatcher.add_handler(CommandHandler('quickfonts', qf_url))
#updater.dispatcher.add_handler(CommandHandler('logs', log))
updater.dispatcher.add_handler(CommandHandler('linkshort1', short1))
updater.dispatcher.add_handler(CommandHandler('linkshort2', short2))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))

updater.start_polling()

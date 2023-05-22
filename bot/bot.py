import telegram.ext
import mytoken

token = mytoken.creds.get('token')

def start(update, cotext):
    update.message.reply_text("سلام")

def help(update, context):
    update.message.reply_text("""
/start : to start intracting with bot,
/help  : for help,
/content : for information
""")
    
def content(update, context):
    update.message.reply_text("you can use our content for free.")
    
def handle_message(update, context):
    update.message.reply_text(f"{update.message.text}")
    
def stock(update, context):
    ticker  = context.args[0]
    update.message.reply_text(ticker)
    #so on...

updater = telegram.ext.Updater(token, use_context=True)
disp = updater.dispatcher


disp.add_handler(telegram.ext.CommandHandler("start", start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
disp.add_handler(telegram.ext.CommandHandler("stock", stock))

updater.start_polling()
updater.idle()
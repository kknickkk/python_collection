import telegram
from subprocess import call

TOKEN = ''
bot = telegram.Bot(TOKEN)


def main():
   
    update_id = 0
    
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None 

    while True :
            try:
                    update_id = broadcast(bot, update_id)
            except NetworkError:
                    print("Network error!")
                    sleep(1)
            except Unauthorized:
                    # The user has removed or blocked the bot.
                    print("Error: user unauthorized")
                    update_id += 1

def broadcast(bot, update_id):
	for update in bot.getUpdates(offset=update_id, timeout=10):
			# chat_id is required to reply to any message
			chat_id = update.message.chat_id
			update_id = update.update_id + 1
			firstname = update.message.from_user.first_name
			message = update.message.text
			if message:
				call(['/home/pi/python_scripts/morning_text.py'])

			return update_id
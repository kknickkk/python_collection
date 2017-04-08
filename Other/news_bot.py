import telegram
import datetime
from telegram.error import NetworkError, Unauthorized
from time import sleep

bot = telegram.Bot('250008562:AAEZvprHPvtDQrV0IDkRSPc6peqXYUdLsjg')
    
def main():
   
    update_id = 0
    
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None 

    while True :
            try:
                    update_id = news(bot, update_id)
            except NetworkError:
                    print("Network error!")
                    sleep(1)
            except Unauthorized:
                    # The user has removed or blocked the bot.
                    print("Error: user unauthorized")
                    update_id += 1

        

def news(bot, update_id):
	message = 0
	for update in bot.getUpdates(offset=update_id, timeout=10):
			# chat_id is required to reply to any message
			chat_id = update.message.chat_id
			update_id = update.update_id + 1
			firstname = update.message.from_user.first_name
			message = update.message.text

			if message == '/start':
					welcome = "Welcome " + firstname + "!\nEnter a website:"
					bot.sendMessage(chat_id=chat_id, text = welcome )
					return update_id

			url = 'u' + message


			website = newspaper.build(url)
			i = 0
			for article in website.articles:

				article = la_stampa_rss.articles[i]
				article.download()
				article.parse()
				message = article.title + '\n\n' + article.url + '\n'
				bot.sendMessage(chat_id=chat_id,text = message)                        
				i += 1



			return update_id

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    

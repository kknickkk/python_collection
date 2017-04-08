import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep



bot = telegram.Bot('250008562:AAEZvprHPvtDQrV0IDkRSPc6peqXYUdLsjg')
users = []

def main():
   
    update_id = 0
    
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None 

    while True :
            try:
                    update_id = create_database(bot, update_id)
            except NetworkError:
                    print("Network error!")
                    sleep(1)
            except Unauthorized:
                    print("Error: user unauthorized")
                    update_id += 1

        	
			
def create_database(bot, update_id):
		
		log = open('log.txt', 'a')
		
			for update in bot.getUpdates(offset=update_id, timeout=10):
				chat_id = update.message.chat_id
        update_id = update.update_id + 1
        message = update.message.text
				firstname = update.message.from_user.first_name
        lastname = update.message.from_user.last_name
        iduser = str(update.message.from_user.id)
				info = chat_id + firstname + lastname 
				if message == '/start':
					welcome_message(firstname)
					log.write( info + ' started the bot\n')
				
				if message == '/subscribe':
					if chat_id not in users:
						users.append(chat_id)
						database = open('database.db', 'a')
						database.write(chat_id + '\n')
						database.close()
						log.write(info + ' subscribed\n')
					else:
						bot.sendMessage(chat_id, 'Already subscribed!\n')
						log.write(info + 'has already subscribed\n')
				
				if message == '/unsubscribe':
					try:
						users.remove(chat_id)
						database = open('database.db', 'w')
						log.write(info + ' unsubscribed\n')
						for item in users:
							database.write("%d\n" % item)
							database.close()

					except:
						bot.sendMessage(chat_id, 'Not subscribed!\n')
						log.write(info + ' has already unsubscribed\n')
			
			log.close()			
			return update_id
			

def welcome_message(name):
	welcome = 'Welcome ' + name +'\nPrompt /subscribe to receive news daily\n'
	bot.sendMessage(chat_id=chat_id, text = welcome )

			
			
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    

import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep

# fra mi ricordo che tu usavi telebot, io uso la libreria ufficiale di telegram, su pip si chiama python-telegram-bot


bot = telegram.Bot('TOKEN')

# questo main è quello standard, function gestisce il messaggio
def main():
   
    update_id = 0
    
    try:
        update_id = bot.getUpdates()[0].update_id
    except IndexError:
        update_id = None 

    while True :
            try:
                    update_id = function(bot, update_id)
            except NetworkError:
                    print("Network error!")
                    sleep(1)
            except Unauthorized:
                    print("Error: user unauthorized")
                    update_id += 1

        	
			
def function(bot, update_id):
	
	#nella gestione del messaggio chiama questo ciclo, tutto avviene qui dentro
			for update in bot.getUpdates(offset=update_id, timeout=10):
				chat_id = update.message.chat_id
        		update_id = update.update_id + 1
        		message = update.message.text
				
				#
				#			qua metti quello che ti serve per elaborare la risposta
				#
				#
				# così mandi i messeggi
				bot.sendMessage(chat_id=chat_id, text = text )
				
			#importante è ritonare update_id che è stato aumentato alla fine della funzione
			return update_id
			

if __name__ == '__main__':
    main()
    
    
    
    
    
    
    

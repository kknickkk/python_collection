#!/usr/bin/env python
import newspaper
import telegram

bot = telegram.Bot('250008562:AAEZvprHPvtDQrV0IDkRSPc6peqXYUdLsjg')
users = []

def main():

	flipboard = newspaper.build(u'https://flipboard.com/@flipboarditalia/edizione-del-giorno-ts3tf1gpz', memoize_articles=False)
	
	with open('database.db', 'r') as database:
		for chat_id in database:
			users.append(chat_id)
	
	
	i = 0
	for article in flipboard.articles:
		if i == 10:
			break
		article = flipboard.articles[i]
		article.download()
		article.parse()
		message = article.title + '\n\n' + article.url + '\n'
		
		for chat_id in users:
			bot.sendMessage(chat_id, message)
		i += 1



if __name__ == '__main__':
    main()

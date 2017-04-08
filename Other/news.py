#!/usr/bin/env python
import newspaper
import telegram

bot = telegram.Bot('250008562:AAEZvprHPvtDQrV0IDkRSPc6peqXYUdLsjg')

def main():

	flipboard = newspaper.build(u'https://flipboard.com/@flipboarditalia/edizione-del-giorno-ts3tf1gpz')
	i = 0
	for article in flipboard.articles:
		
		article = flipboard.articles[i]
		article.download()
		article.parse()
		message = article.title + '\n\n' + article.url + '\n'
		bot.sendMessage(85048573, message)
		i += 1



if __name__ == '__main__':
    main()










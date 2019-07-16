from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer #importing libraries
import os                                   #importing operating system

bot=ChatBot("NEHA")                         #defining the name
bot.set_trainer(ListTrainer)                #definig the trainer

for files in os.listdir('F:/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'): #replace all \ with / to avaoid end of line and end the path with/
    data=open('F:/Downloads/chatterbot-corpus-master/chatterbot-corpus-master/chatterbot_corpus/data/english/'+files,'r').readlines()#open file in read mode
    bot.train(data)#train the bot

while True:
    message=input('you:')
    if message.strip!='Bye' or message.strip!='bye':#if not the end of conversation
        reply=bot.get_response(message)
        print('ChatBot:',reply)
    if message.strip=='Bye' or message.strip=='bye':
        print('ChatBot:It was nice talking to you')
        break


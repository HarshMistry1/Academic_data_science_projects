from django.shortcuts import render
from .models import chat, chatdata
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# Create your views here.
def home(self):

    data=chatdata.objects.all()
    return render(self,'index.html')

fetch_data=[]
def getvalue(self):
    if self.POST:

       
        bot=ChatBot('jay')
        conversation = [
            
        ]
        c=chat.objects.all().values_list()
        for i in c:
            conversation.append(i[1])
    

        trainer = ListTrainer(bot)

        trainer.train(conversation)
        
        
        msg=self.POST.get('msg')
        response = bot.get_response(msg)
        data={}
        data['msg']=msg
        data['reply']=response

        print(response)

        return render(self,'index.html',data)

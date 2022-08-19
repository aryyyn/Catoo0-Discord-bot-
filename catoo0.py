import requests
import os
import discord
from dotenv import load_dotenv
import random
import time



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client(intents=discord.Intents.all())

test_list = ['aryn#5511',
'ok and?',
'random message here'.





 ]
 

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="./help"))
    print('We have logged in as {0.user}'.format(client))
   

@client.event
async def on_message(message):
  

    msg = str(message.content)
    user = str(message.author).split('#')[0]
    send = message.channel.send
    mention = f'<@!{client.user.id}>'
    if message.author == client.user:
        return

    if message.content.startswith('!catf'):
        data = requests.get('https://catfact.ninja/fact').text

        txt = str(data).split(':')

        rate = (txt[1]).replace(('"'), '').replace('length', '').replace(',', '')


        await message.channel.send("Here is a random cat fact: " + rate)
        return
        print("message sent")



    elif msg.lower() == 'samosa dai':
         await message.channel.send('gayo samosa khana')
         return
         print("message sent")
   
   
    
  

     
   

    random_num = random.choice(test_list)
    a = random.randint(0, 1)
    
       
    
    if msg.lower() == 'amigay' and a == 1:
      
      await message.channel.send(f'{user} is gay')
    if msg.lower() == 'amigay' and a == 0:
        await message.channel.send(f'{user} is straight')
    
    
    
    
    if client.user.mentioned_in(message):

      
      await message.channel.send(random_num)

    if msg.lower() == 'gn':
         await message.channel.send(f"GoodNight {message.author.mention}")
         

     
   
    if message.content.startswith('!dog'):
        data = requests.get('https://random.dog/woof.json').text

        txt1 = str(data).split(':')

        doggo = (txt1[3]).replace(('"'), '').replace('}', '')

        await message.channel.send('https:'+doggo)
       
        return

    elif message.content.startswith('!meme'):
         data3 = requests.get('https://meme-api.herokuapp.com/gimme').text
       

         txt3 = str(data3).split(':')
         await message.channel.send(txt3)
         rate3 = (txt3[6]).replace(('","nsfw"'), '')


         await message.channel.send('https:'+rate3)

         
         emoji = '\N{THUMBS UP SIGN}'
         emoji2 = '\N{THUMBS DOWN SIGN}'
         time.sleep(2)
         await message.add_reaction(emoji)
         await message.add_reaction(emoji2)
         return
         

    
     
    if message.content.startswith('./help'):
      await message.channel.send("Tag the bot to roast someone [@catoo0] \n !dog - dog img/gif \n !cat - cat img/gif \n !catf - random cat fact \n gn - sends a good night test \n !amigay - checks if the user is gay \n !meme - sends a random meme")
      print('sent')
      return
   
     

   
    




            

client.run(TOKEN)

import requests
import os
import discord
from dotenv import load_dotenv
import random
import time
import string
global mama76



load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client(intents=discord.Intents.all())

test_list = ['pocky',
':evil:',
'when nitro, ako?',





 ]
members = 0
for guild in client.guilds:
    members += guild.member_count - 1

@client.event
async def on_ready():
   
    print('We have logged in as {0.user}'.format(client))
    servers = len(client.guilds)
    members = 0
    for guild in client.guilds:
        members += guild.member_count - 1

    await client.change_presence(activity = discord.Activity(
        type = discord.ActivityType.playing,
        name = f'playing roblox with {members} members'
    ))
   

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



   
  
    ch = client.get_channel(905343313547259945)
   
    random_num = random.choice(test_list)
    a = random.randint(0, 1)
    b = random.choices(string.ascii_lowercase, k=5)
    
       
    


    if msg.lower() == 'gn':
         await message.channel.send(f"GoodNight {message.author.mention}")
         await message.channel.send("https://tenor.com/view/hila-lund-hilakesoja-muth-muthi-gif-21187080")

     
   
    if message.content.startswith('!dog'):
        data = requests.get('https://random.dog/woof.json').text

        txt1 = str(data).split(':')

        doggo = (txt1[3]).replace(('"'), '').replace('}', '')

        await message.channel.send('https:'+doggo)
    

    if message.content.startswith('!meme'):
         data10 = requests.get('https://meme-api.herokuapp.com/gimme').text
       

         txt10 = str(data10).split(':')
        
         rate10 = (txt10[6]).replace(('","nsfw"'), '')


         await message.channel.send('https:'+rate10)

         
         emoji = '\N{THUMBS UP SIGN}'
         emoji2 = '\N{THUMBS DOWN SIGN}'
         time.sleep(2)
         await message.add_reaction(emoji)
         await message.add_reaction(emoji2)
         

     
    if message.content.startswith('./help' or './HELP' or './Help'):
      await message.delete()
      await message.channel.send("``` Tag the bot to roast someone [@catoo0] \n !dog - dog img/gif \n !cat - cat img/gif \n !catf - random cat fact \n gn - sends a good night test \n !amigay - checks if the user is gay \n !meme - sends a random meme \n !joke - sends a random joke \n !age - bot age \n !fact - sends a random interesting fact \n !cboy - catboy pictures for ako \n !yomama - sends a yommama joke \n !waifu or !2waifu - waifus ofc lol \n !kill - use this to kill someone \n !bully -  use this to bully someone \n !kiss - only for ako <3  \n !roast - roast someone \n !food - random images of food \n !weather - displays the weather \n !cry - cry, nobody cares about you anyway \n !genshin genshim images ig \n !bonk - bonk someone \n !nom - nom nom nom \n !talk! - talk with someone \n !fight! - challenge someone to a fight \n !rolldice! - challenge someone to a dice battle ``` \n  ``` ./memehelp for meme maker commands``` \n \n - ``aryn#5511``")
      print('sent')
      return

    if message.content.startswith('./memehelp' or './MEMEHELP' or './Memehelp'):
     await message.delete()
     await message.channel.send("``` !gordon! \n !drake! \n !peter! \n !meeting! \n !skeleton! \n !tys! \n !2buttons! ``` ")
     return
   

    if message.content.startswith('!joke'):
        data7 = requests.get('https://geek-jokes.sameerkumar.website/api').text

        txt7 = str(data7)

        boredd = (txt7).replace(('"'), '')

        await message.channel.send(boredd)
       
        return

 
    
    if message.content.startswith('!age'):
        channel = message.channel
        await channel.send('My age is 14')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {author}!'.format(msg))

    
    if message.content.startswith('!fact'):
        data5 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en').text

        txt5 = str(data5).split(':')

        fact = (txt5[2]).replace(('"'), '').replace('.,source', '')

        await message.channel.send(fact)


    if message.content.startswith('!cat'):
        data5 = requests.get(' https://api.thecatapi.com/v1/images/search?limit=1').text

        txt5 = str(data5).split(':')

        fact = (txt5[3]).replace(('"'), '').replace(',width', '')

        await message.channel.send('https:' + fact)

    if message.content.startswith('!fox'):
        data8 = requests.get('https://randomfox.ca/floof/?ref=apilist.fun').text

        txt8 = str(data8).split(':')

        foxed = (txt8[2]).replace(('"'), '').replace(',link', '')

        links = 'https:' + foxed

        await message.channel.send(links)

  
#https://api.catboys.com/img
   

    if message.content.startswith('!cboy'):
        data22 = requests.get('https://api.catboys.com/img').text

        txt22 = str(data22).split(':')

        

        cat22 = (txt22[2]).replace(('"'), '').replace(',artist', '')

        await message.channel.send('https:'+cat22)
       
        return


  #https://place.dog/300/200
    if message.content.startswith('!dog'):
        data23 = requests.get('https://place.dog/300/200g').text

        

        await message.channel.send(data23)
       
        return

#https://yomomma-api.herokuapp.com/jokes

    if message.content.startswith('!yomama'):
        data24 = requests.get('https://yomomma-api.herokuapp.com/jokes').text

        txt24 = str(data24).split(':')

        

        mama22 = (txt24[1]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send(mama22)
       
        return
          
#https://api.waifu.pics/sfw/waifu
    if message.content.startswith('!waifu'):
        data24 = requests.get('https://api.waifu.pics/sfw/waifu').text

        txt24 = str(data24).split(':')

        

        mama22 = (txt24[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama22)
       
        return

    if message.content.startswith('!bully'):
        data24 = requests.get('https://api.waifu.pics/sfw/bully').text

        txt24 = str(data24).split(':')

        

        mama22 = (txt24[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama22)
       
        return

    if message.content.startswith('!kiss'):
        data30 = requests.get('https://api.waifu.pics/sfw/kiss').text

        txt30 = str(data30).split(':')

        

        mama30 = (txt30[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama30)   

  

         
   
    
    
  

#https://api.waifu.pics/sfw/kill
    
    if message.content.startswith('!kill'):
        data30 = requests.get('https://api.waifu.pics/sfw/kill').text

        txt30 = str(data30).split(':')

        

        mama30 = (txt30[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama30)
        return
       
    #https://dicks-api.herokuapp.com/dicks/1

    if message.content.startswith('!ppsize'):
        data1050 = requests.get('https://dicks-api.herokuapp.com/dicks/1').text

        text1050 = str(data1050).split(':')

        pp = (text1050[1]).replace('["', "").replace('"]}', '')
        await message.channel.send(user+"'s pp \n " + pp)
        return
   
#https://insult.mattbas.org/api/insult

    if message.content.startswith('!roast'):
        data1150 = requests.get('https://insult.mattbas.org/api/insult').text
        await message.channel.send(data1150)
        
        return


   #https://foodish-api.herokuapp.com/api/

    if message.content.startswith('!food'):
        data1052 = requests.get('https://foodish-api.herokuapp.com/api/').text

        text1052 = str(data1052).split(':')

        fud = (text1052[2]).replace('["', "").replace('"}', '')
        await message.channel.send('https:' + fud)
        return


 #https://goweather.herokuapp.com/weather/lalitpur
    if message.content.startswith('!weather lalitpur'):
        data1059 = requests.get('https://goweather.herokuapp.com/weather/lalitpur').text

        text1055 = str(data1059).split(':')
        text1056 = str(data1059).split(':')
        text1057 = str(data1059).split(':')

        weathertemp = (text1055[1]).replace('","wind"', '').replace('"', '')
        weatherwind = (text1056[2]).replace('","description"', '').replace('"', '')
        weatherd = (text1057[3]).replace('","forecast"', '').replace('"', '')
        await message.channel.send('WEATHER IN LALITPUR \n \n Temperature - ' + weathertemp + '\n Wind - ' + weatherwind + '\n ' + weatherd)
        return

        #https://goweather.herokuapp.com/weather/lalitpur
    if message.content.startswith('!weather kathmandu'):
        data1059 = requests.get('https://goweather.herokuapp.com/weather/kathmandu').text

        text1055 = str(data1059).split(':')
        text1056 = str(data1059).split(':')
        text1057 = str(data1059).split(':')

        weathertemp = (text1055[1]).replace('","wind"', '').replace('"', '')
        weatherwind = (text1056[2]).replace('","description"', '').replace('"', '')
        weatherd = (text1057[3]).replace('","forecast"', '').replace('"', '')
        await message.channel.send('WEATHER IN KATHMANDU \n \n Temperature - ' + weathertemp + '\n Wind - ' + weatherwind + '\n ' + weatherd)
        return


#https://api.waifu.pics/sfw/cry

    if message.content.startswith('!cry'):
        data3011 = requests.get('https://api.waifu.pics/sfw/cry').text

        txt3011 = str(data3011).split(':')

        

        mama3011 = (txt3011[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama3011)
        return

   #https://api.waifu.im/random/?selected_tags=raiden-shogun
    if message.content.startswith('!genshin'):
        data30112 = requests.get('https://api.waifu.im/random/?selected_tags=raiden-shogun').text

        txt30112 = str(data30112).split(':')

        

        mama30112 = (txt30112[17]).replace('","preview_url', '').replace('"', '')

        await message.channel.send('https:' + mama30112)
        return
    
#https://api.waifu.im/random/?selected_tags=selfies
    if message.content.startswith('!2waifu'):
        data301122 = requests.get('https://api.waifu.im/random/?selected_tags=selfies').text

        txt301122 = str(data301122).split(':')

        

        mama301122 = (txt301122[17]).replace('","preview_url', '').replace('"', '')

        await message.channel.send('https:' + mama301122)
        return
       
       if message.content.startswith('!flirt'):
        data777 = requests.get('http://getpickuplines.herokuapp.com/lines/random').text

        txt777 = str(data777).split(':')

        

        mama777 = (txt777[2]).replace('"', '').replace('"}', '').replace('}', '')

        await message.channel.send(mama777)
        return

      #https://c.tenor.com/dLjTriTF5p0AAAAd/call-an.gif
    if message.content.startswith('!rebibe'):
     await message.channel.send('https://c.tenor.com/dLjTriTF5p0AAAAd/call-an.gif')


     #https://api.waifu.pics/sfw/nom

    if message.content.startswith('!nom'):
        data3011 = requests.get('https://api.waifu.pics/sfw/nom').text

        txt3011 = str(data3011).split(':')

      

        

        mama3011 = (txt3011[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama3011)
        return


    if message.content.startswith('!kick'):
        data3011 = requests.get('https://api.waifu.pics/sfw/kick').text

        txt3011 = str(data3011).split(':')

      
  
        

        mama3011 = (txt3011[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama3011)
        return

      #https://api.waifu.pics/sfw/slap
    if message.content.startswith('!slap'):
        data3011 = requests.get('https://api.waifu.pics/sfw/slap').text

        txt3011 = str(data3011).split(':')

      
  
        

        mama3011 = (txt3011[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama3011)
        return


        #https://api.waifu.pics/sfw/bonk

    if message.content.startswith('!bonk'):
        data3011 = requests.get('https://api.waifu.pics/sfw/bonk').text

        txt3011 = str(data3011).split(':')

        

        mama3011 = (txt3011[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama3011)
        return


    if msg.lower() == 'gm':
         await message.channel.send(f"GoodMorning {message.author.mention}")

      #https://api.waifu.pics/sfw/pat 
  
    if message.content.startswith('!pat'):
        data3011 = requests.get('https://api.waifu.pics/sfw/pat').text

        txt3011 = str(data3011).split(':')

        

        mama3011 = (txt3011[2]).replace('"', '').replace('}"', '').replace('}', '')

        await message.channel.send('https:' + mama3011)
        return

    
      
    if message.content.startswith('!join'):
      
            channel = message.author.voice.channel
            await channel.connect()
            return
        
      



    
   
   
    if message.content.startswith("lado" or "test"):
             if message.author != client.user:
              await message.delete()
              await message.channel.send( message.author.mention + " You cant use that here buddy!")
             
             return

       
    if message.content.startswith("!say!"):
        try:
            await message.delete()
            rl = message.content.split('!')[2]
           
            
            await message.channel.send(rl)
           

        except Exception as err:
            print(err)
            return  


    if message.content.startswith('!fight!'):
        try:
            r2 = message.content.split('!')[2]
            coaa = random.randint(0, 1)
            if coaa == 1:
               await message.channel.send("You have won the fight!")
            if coaa == 0:
               await  message.channel.send(r2 + " has won the fight!")
                  
            
        except:
            await message.channel.send("Enter the name of the user you want to fight first")
            return   

          #https://api.catboys.com/dice
    if message.content.startswith('!rolldice!'):

     try:
        r2 = message.content.split('!')[2]
        data3011 = requests.get('https://api.catboys.com/dice').text

        txt3011 = str(data3011).split(':')

        

        mama3011 = (txt3011[3]).replace('","error', '').replace('"', '').replace('none}', 'your dice dead lol, try again')

        data30111 = requests.get('https://api.catboys.com/dice').text

        txt30111 = str(data30111).split(':')

        

        mama30111 = (txt30111[3]).replace('","error', '').replace('"', '').replace('none}', 'your dice dead lol, try again')
        await message.channel.send('Your dice')
        await message.channel.send('https:' + mama3011)
        await message.channel.send(r2 + "'s dice")
        await message.channel.send('https:' + mama30111)
        if data3011 == data30111:
            await message.channel.send("draw")

        return

     except:
        await message.channel.send(f"{message.author.mention}, \n !rolledice! is the syntax for this command \n Enter the command first and then the name of the person")
        
    if message.content.startswith('!baka'):

  
        
        data3011 = requests.get('https://api.catboys.com/baka').text

        txt3011 = str(data3011).split(':')
        mama3011 = (txt3011[2]).replace('","error', '').replace('"', '')
        await message.channel.send('https:' + mama3011)
        return

    if message.content.startswith('!gordon!'):
     try:
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=Chef-Gordon-Ramsay&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !gordon!(topmessage)!(bottomessage)")


    

     
        #http://apimeme.com/meme?meme=Drake-Bad-Good&top=Top+text&bottom=Bottom+text

    if message.content.startswith('!drake!'):
     try:
       
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=Drake-Bad-Good&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !drake!(topmessage)!(bottomessage)")


    if message.content.startswith('!peter!'):
     try:
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=Family-Guy-Peter&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !peter!(topmessage)!(bottomessage)")


    if message.content.startswith('!meeting!'):
     try:
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=Alien-Meeting-Suggestion&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !meeting!(topmessage)!(bottomessage)")



    if message.content.startswith('!skeleton!'):
     try:
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=Waiting-Skeleton&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !skeleton!(topmessage)!(bottomessage)")


    if message.content.startswith('!tys!'):
     try:
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=X-Everywhere&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !tys!(topmessage)!(bottomessage)")


    if message.content.startswith('!2buttons!'):
     try:
        await message.delete()
        w1 = message.content.split('!')[2]
        w2 = message.content.split('!')[3]
        await message.channel.send('https://apimeme.com/meme?meme=Two-Buttons&top='+w1+'&bottom='+w2)
     
     except:
        await message.channel.send("The command syntax is !2buttons!(topmessage)!(bottomessage)")


    if message.content.startswith("!play"):
        try:
            voice_client = await message.author.voice.channel.connect()
            voice_clients[voice_client.guild.id] = voice_client
        except:
            print("error")

        try:
            url = message.content.split()[1]

            loop = asyncio.get_event_loop()
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=False))

            song = data['url']
            player = discord.FFmpegPCMAudio(song, **ffmpeg_options)
            await message.channel.send("Joined")
            voice_clients[message.guild.id].play(player)

        except Exception as err:
            print(err)


    if message.content.startswith("!stop"):
        try:
            voice_clients[message.guild.id].stop()
            await voice_clients[message.guild.id].disconnect()
            await message.channel.send("Bot has been disconnected.")
        except Exception as err:
            print(err)


client.run(TOKEN)

import discord
import os

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):

  # if send message to self, do nothing
  if message.author == client.user:
    return
    
  # botto receives -command and returns message
  if message.content.startswith('-hello'):
    await message.channel.send('( ´ ▽ `)ﾉ  heyo!')
  if message.content.startswith('-how are you?'):
    await message.channel.send('(´﹃ ` ) hungry for some sandwiches... :sandwich:')
  if message.content.startswith('-pizza'):
    await message.channel.send('( ⋋_⋌ ):anger: how offensive 。。。')

# it's a secret... :x
client.run(os.environ['TOKEN'])

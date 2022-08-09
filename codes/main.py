import discord
import random
import os

# ---------------------------------------------------------------------------------------

bread_count = 0
meat_count = 0
cheese_count = 0
veggie_count = 0
spread_count = 0
reactions = ['🍞', '🥩', '🧀', '🥬', '🍅']

client = discord.Client()

# ---------------------------------------------------------------------------------------

bread = []
with open('bread.txt') as b:
  bread = [line.rstrip() for line in b]
  
meat = []
with open('meat.txt') as m:
  meat = [line.rstrip() for line in m]
  
cheese = []
with open('cheese.txt') as c:
  cheese = [line.rstrip() for line in c]

veggie = []
with open('veggie.txt') as v:
  veggie = [line.rstrip() for line in v]

spreads = []
with open('spreads.txt') as s:
  spreads = [line.rstrip() for line in s]

sweet = []
with open('sweet.txt') as sw:
  sweet = [line.rstrip() for line in sw]

# ---------------------------------------------------------------------------------------

def choose_bread():
  return (':bread: **bread:** ' + random.choice(bread))

def choose_meat():
  return (':cut_of_meat: **meat:** ' + random.choice(meat))

def choose_cheese():
  return (':cheese: **cheese:** ' + random.choice(cheese))

def choose_veggie():
  return (':leafy_green: **veggie:** ' + random.choice(veggie))

def choose_spread():
    return (':tomato: **spread:** ' + random.choice(spreads))
          
def make_sandwich():
  return (choose_bread() + '\n' \
          + choose_meat() + '\n' \
          + choose_cheese() + '\n' \
          + choose_veggie() + '\n' \
          + choose_spread())

def make_sweet():
  return (random.choice(sweet))
  
# ---------------------------------------------------------------------------------------

@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is now up and running! ヾ(^ ∇ ^)ノ') 

# ---------------------------------------------------------------------------------------

@client.event
async def on_message(message):
  global bread_count, meat_count, cheese_count, veggie_count, spread_count
  
  if message.author == client.user:
    return
    
# ---------------------------------------------------------------------------------------
    
  if message.content.startswith('>hello'):
    await message.channel.send('( ´ ▽ `)ﾉ  heyo!')
    
  if message.content.startswith('>how are you?'):
    await message.channel.send('(´﹃ ` ) hungry for some sandwiches。。。 :sandwich:')
    
  if message.content.startswith('>friend'):
    await message.channel.send('( ˶ᵔ ᵕ ᵔ˶):cherry_blossom: we are already great friends!')
    
  if message.content.startswith('>pizza'):
    await message.channel.send('( ⋋_⋌ ):anger: how offensive 。。。')
    
  if message.content.startswith('>burger'):
    await message.channel.send("( ⋋_⋌ ):anger: we're healhier ya know 。。。")

# ---------------------------------------------------------------------------------------
    
  order_count = 0
  if message.content.startswith('>sandwich'):
    order_count = order_count + 1
    reaction_msg = await message.channel.send('sandwich botto at your service! ( ´ ▽ `)7 \
    \nplease react to select your preferred type of fillings & quantity.')
    if order_count > 0:
      bread_count = 0
      meat_count = 0
      cheese_count = 0
      veggie_count = 0
      spread_count = 0
    for emoji in reactions: 
      await reaction_msg.add_reaction(emoji)

  if message.content.startswith('>randomize'):
    await message.channel.send(":sandwich: here's your ``random`` sandwich!\n \n" + make_sandwich())
    
  if message.content.startswith('>sweet'):
    await message.channel.send(":sandwich: here's your ``sweet`` sandwich!\n \n" + make_sweet())

  if message.content.startswith('>inputbread'):
    await message.channel.send(":memo: please input your :bread: ``breads`` separated by ``commas``.")
    
  if message.content.startswith('>inputmeat'):
    await message.channel.send(":memo: please input your :cut_of_meat: ``meats`` separated by ``commas``")
    
  if message.content.startswith('>inputcheese'):
    await message.channel.send(":memo: please input your :cheese: ``cheeses`` separated by ``commas``.")
    
  if message.content.startswith('>inputveggie'):
    await message.channel.send(":memo: please input your :leafy_green: ``veggies`` separated by ``commas``.")
    
  if message.content.startswith('>inputspread'):
    await message.channel.send(":memo: please input your :tomato: ``spreads`` separated by ``commas``.")

# ---------------------------------------------------------------------------------------

@client.event
async def on_reaction_add(reaction, user):
  global bread_count, meat_count, cheese_count, veggie_count, spread_count
  channel = reaction.message.channel    
  
  if 'react to select' in reaction.message.content and reaction.emoji == '🍞':
    if bread_count == 0:
      bread_count = 1
    else:
      await channel.send(choose_bread())
  if 'react to select' in reaction.message.content and reaction.emoji == '🥩': 
    if meat_count == 0:
      meat_count = 1
    else:
      await channel.send(choose_meat())
  if 'react to select' in reaction.message.content and reaction.emoji == '🧀':
    if cheese_count == 0:
      cheese_count = 1
    else:
      await channel.send(choose_cheese())
  if 'react to select' in reaction.message.content and reaction.emoji == '🥬':
    if veggie_count == 0:
      veggie_count = 1
    else:
      await channel.send(choose_veggie())
  if 'react to select' in reaction.message.content and reaction.emoji == '🍅':
    if spread_count == 0:
      spread_count = 1
    else:
      await channel.send(choose_spread())

# ---------------------------------------------------------------------------------------

user_bread = []
user_meat = []
user_cheese = []
user_veggie = []
user_spread = []

# ---------------------------------------------------------------------------------------

client.run(os.environ['TOKEN'])

# ---------------------------------------------------------------------------------------

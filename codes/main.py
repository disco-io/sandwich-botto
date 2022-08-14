import discord
import random
import os
from replit import db

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
spread = []
with open('spreads.txt') as s:
  spread = [line.rstrip() for line in s]
sweet = []
with open('sweet.txt') as sw:
  sweet = [line.rstrip() for line in sw]

# ---------------------------------------------------------------------------------------
  
def update_bread(input_bread):
  if "bread" in db.keys():
    bread = db["bread"]
    bread.append(input_bread)
    db["bread"] = bread
  else:
    db["bread"] = [input_bread]
def update_meat(input_meat):
  if "meat" in db.keys():
    meat = db["meat"]
    meat.append(input_meat)
    db["meat"] = meat
  else:
    db["meat"] = [input_meat]
def update_cheese(input_cheese):
  if "cheese" in db.keys():
    cheese = db["cheese"]
    cheese.append(input_cheese)
    db["cheese"] = cheese
  else:
    db["cheese"] = [input_cheese]
def update_veggie(input_veggie):
  if "veggie" in db.keys():
    veggie = db["veggie"]
    veggie.append(input_veggie)
    db["veggie"] = veggie
  else:
    db["veggie"] = [input_veggie]
def update_spread(input_spread):
  if "spread" in db.keys():
    spread = db["spread"]
    spread.append(input_spread)
    db["spread"] = spread
  else:
    db["spread"] = [input_spread]
    
def delete_bread(index):
  bread = db["bread"]
  if len(bread) > index:
    del bread[index]
  db["bread"] = bread
  
# ---------------------------------------------------------------------------------------

def choose_bread():
  boptions = bread
  if "bread" in db.keys():
    boptions = boptions + db["bread"]
  return (':bread: **bread:** ' + random.choice(boptions))
def choose_meat():
  moptions = meat
  if "meat" in db.keys():
    moptions = moptions + db["meat"]
  return (':cut_of_meat: **meat:** ' + random.choice(moptions))
def choose_cheese():
  coptions = cheese
  if "cheese" in db.keys():
    coptions = coptions + list(db["cheese"])
  return (':cheese: **cheese:** ' + random.choice(coptions))
def choose_veggie():
  voptions = veggie
  if "veggie" in db.keys():
    voptions = voptions + db["veggie"]
  return (':leafy_green: **veggie:** ' + random.choice(voptions))
def choose_spread():
  soptions = spread
  if "spread" in db.keys():
    soptions = soptions + db["spread"]
  return (':tomato: **spread:** ' + random.choice(soptions))
  
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
  msg = message.content
  
  if message.author == client.user:
    return
    
# ---------------------------------------------------------------------------------------
    
  if msg.startswith('>hello'):
    await message.channel.send('( ´ ▽ `)ﾉ  heyo!')
    
  if msg.startswith('>how are you?'):
    await message.channel.send('(´﹃ ` ) hungry for some sandwiches。。。 :sandwich:')
    
  if msg.startswith('>friend'):
    await message.channel.send('( ˶ᵔ ᵕ ᵔ˶):cherry_blossom: we are already great friends!')
    
  if msg.startswith('>pizza'):
    await message.channel.send('( ⋋_⋌ ):anger: how offensive 。。。')
    
  if msg.startswith('>burger'):
    await message.channel.send("( ⋋_⋌ ):anger: we're healhier ya know 。。。")

# ---------------------------------------------------------------------------------------
    
  order_count = 0
  if msg.startswith('>sandwich'):
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

  if msg.startswith('>random'):
    await message.channel.send(":sandwich: here's your ``random`` sandwich!\n \n" + make_sandwich())
    
  if msg.startswith('>sweet'):
    await message.channel.send(":sandwich: here's your ``sweet`` sandwich!\n \n" + make_sweet())

  if msg.startswith('>addbread'):
    await message.channel.send('( ´ ᵕ `)" :warning: please **behave** with this function! if you are fooling around, please ``>delbread`` your input!')
    input_bread = message.content.split('>addbread ', 1)[1]
    update_bread(input_bread)
    await message.channel.send(input_bread + ' has been added to the bread database!')

  if msg.startswith('>addmeat'):
    await message.channel.send('( ´ ᵕ `)" :warning: please **behave** with this function! if you are fooling around, please ``>delmeat`` your input!')
    input_meat = message.content.split('>addmeat ', 1)[1]
    update_meat(input_meat)
    await message.channel.send(input_meat + ' has been added to the meat database!')

  if msg.startswith('>addcheese'):
    await message.channel.send('( ´ ᵕ `)" :warning: please **behave** with this function! if you are fooling around, please ``>delcheese`` your input!')
    input_cheese = message.content.split('>addcheese ', 1)[1]
    update_cheese(input_cheese)
    await message.channel.send(input_cheese + ' has been added to the cheese database!')

  if msg.startswith('>addveggie'):
    await message.channel.send('( ´ ᵕ `)" :warning: please **behave** with this function! if you are fooling around, please ``>delveggie`` your input!')
    input_veggie = message.content.split('>addveggie ', 1)[1]
    update_veggie(input_veggie)
    await message.channel.send(input_veggie + ' has been added to the veggie database!')

  if msg.startswith('>addspread'):
    await message.channel.send('( ´ ᵕ `)" :warning: please **behave** with this function! if you are fooling around, please ``>delspread`` your input!')
    input_spread = message.content.split('>addspread ', 1)[1]
    update_spread(input_spread)
    await message.channel.send(input_spread + ' has been added to the spread database!')

  if msg.startswith('>breadlist'):
    bread = []
    if "bread" in db.keys():
      bread = db["bread"]
    await message.channel.send(bread)
    
  if msg.startswith('>delbread'):
    bread = []
    if "bread" in db.keys():
      index = int(message.content.split('>delbread',1)[1])
      delete_bread(index)
      bread = db["bread"]
    await message.channel.send(bread)

# ----------------------------UNDER CONSTRUCTION-----------------------------------------
    
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

client.run(os.environ['TOKEN'])

# ---------------------------------------------------------------------------------------

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

sweet = ['**peanut butter & jelly sandwich**:\n\
:bread: white bread\n:grapes: grape jelly\n:peanuts: peanut butter',
        '**strawberry sando**:\n\
:bread: shokupan (japanese milk bread), no crust\n:icecream: whipped cream\n:strawberry: strawberries\n:dagger: slice diagonally', 
        '**fruit sando**:\n\
:bread: shokupan (japanese milk bread), no crust\n:icecream: whipped cream\n:kiwi: strawberry, orange, kiwi\n:dagger: slice diagonally',
        '**the elvis**:\n\
:bread: white bread\n:banana: toasted banana slices\n:peanuts: peanut butter\n:bacon: bacon\n:dagger: slice diagonally',
        '**raspberry marshmallow**:\n\
:bread: toasted sourdough bread\n:strawberry: raspberries\n:lollipop: melted white chocolate & marshmallow\n:coconut: coconut oil',       
        '**peanut butter-nutella**:\n\
:bread: white bread\n:strawberry: strawberries, banana slices\n:chocolate_bar: nutella\n:peanuts: peanut butter',
        '**chocolate french toast**:\n\
:bread: cinnamon french toast\n:banana: banana slices\n:chocolate_bar: nutella\n:honey_pot: maple syrup\n:salt: powdered sugar']

#sweet = []
#with open('sweet.txt') as sw:
#  sweet = [line.rstrip() for line in sw]

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

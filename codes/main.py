import discord
import random
import os

bread_count = 0
meat_count = 0
cheese_count = 0
veggies_count = 0
spread_count = 0

client = discord.Client()

#fillings menu
bread = [ 'bagel', 'baguette', 'biscuit', 'brioche', 'brown bread', 'challah', 'ciabatta', 'cornbread', 'croissant', 'english muffin', 'focaccia', 'grissini', 'hawaiian roll', 'potato bread', 'rye bread', 'multi-grain bread', 'pumpernickel', 'smoked salmon', 'sourdough bread', 'white bread', 'whole wheat bread']

meat = ['bacon', 'black forest ham', 'bologna sausage', 'buffalo chicken', 'grilled chicken breast', 'honey ham', 'meatballs', 'pepperoni', 'pulled pork' 'roast beef', 'shredded chicken''steak', 'tuna', 'tuna', 'turkey salami','turkey breast']

cheese = ['american cheese', 'brie', 'cheddar', 'gouda', 'havarti', 'parmesan', 'pepper jack', 'provolone', 'swiss', 'mozzarella']

veggies = ['basil', 'coleslaw', 'diced celery', 'jalepeno' 'pickles', 'lettuce', 'olives', 'red onions', 'red peppers', 'sauteéd mushrooms', 'shredded carrots', 'sliced cucmbers', 'spinach', 'white onions','tomatoes']

spreads = ['blue cheese dressing', 'guacamole', 'honey mustard', 'hot sauce', 'hummus', 'mayonnaise', 'mustard', 'ranch', 'smoky bbq', 'spicy mayo', 'sweet onion dip', 'ketchup']

#in the kitchen
def choose_bread():
  return (':bread: **bread:** ' + random.choice(bread))

def choose_meat():
  return (':cut_of_meat: **meat:** ' + random.choice(meat))

def choose_cheese():
  return (':cheese: **cheese:** ' + random.choice(cheese))

def choose_veggies():
  return (':leafy_green: **veggie:** ' + random.choice(veggies))

def choose_spreads():
    return (':tomato: **spread:** ' + random.choice(spreads))
          
def make_sandwich():
  return (choose_bread() + '\n' \
          + choose_meat() + '\n' \
          + choose_cheese() + '\n' \
          + choose_veggies() + '\n' \
          + choose_spreads())
  
#online message
@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is now up and running! ヾ(^ ∇ ^)ノ') 

@client.event
async def on_message(message):
  global bread_count, meat_count, cheese_count, veggies_count, spread_count
  
  #if send message by bot, do nothing
  if message.author == client.user:
    return
    
  # user-botto conversations
  if message.content.startswith('>hello'):
    await message.channel.send('( ´ ▽ `)ﾉ  heyo!')
  if message.content.startswith('>how are you?'):
    await message.channel.send('(´﹃ ` ) hungry for some sandwiches。。。 :sandwich:')
  if message.content.startswith('>friend'):
    await message.channel.send('( ˶ᵔ ᵕ ᵔ˶):cherry_blossom: we are already great friends!')

  #sandwich commands
  order_count = 0
  if message.content.startswith('>sandwich'):
    order_count = order_count + 1
    reaction_msg = await message.channel.send('sandwich botto at your service! ( ´ ▽ `)7 \nplease react to select your preferred type of fillings & quantity.')
    if order_count > 0:
      bread_count = 0
      meat_count = 0
      cheese_count = 0
      veggies_count = 0
      spread_count = 0
    await message.channel.send(bread_count+meat_count+cheese_count+veggies_count+spread_count)
    await reaction_msg.add_reaction('🍞')
    bread_count = 1
    await reaction_msg.add_reaction('🥩')
    meat_count = 1
    await reaction_msg.add_reaction('🧀')
    cheese_count = 1
    await reaction_msg.add_reaction('🥬')
    veggies_count = 1
    await reaction_msg.add_reaction('🍅')
    spread_count = 1
    await message.channel.send(bread_count+meat_count+cheese_count+veggies_count+spread_count)

  if message.content.startswith('>randomize'):
    await message.channel.send(":sandwich: here's your random sandwich!\n \n" + make_sandwich())

  #angry sandwich
  if message.content.startswith('>pizza'):
    await message.channel.send('( ⋋_⋌ ):anger: how offensive 。。。')
  if message.content.startswith('>burger'):
    await message.channel.send("( ⋋_⋌ ):anger: we're healhier ya know 。。。")
      
@client.event
async def on_reaction_add(reaction, user):
  channel = reaction.message.channel    
  if 'react' in reaction.message.content and reaction.emoji == '🍞' and bread_count != 0:
    await channel.send(choose_bread())
  if 'react' in reaction.message.content and reaction.emoji == '🥩' and meat_count != 0:
    await channel.send(choose_meat())
  if 'react' in reaction.message.content and reaction.emoji == '🧀' and cheese_count != 0:
    await channel.send(choose_cheese())
  if 'react' in reaction.message.content and reaction.emoji == '🥬' and veggies_count != 0:
    await channel.send(choose_veggies())
  if 'react' in reaction.message.content and reaction.emoji == '🍅' and spread_count != 0:
    await channel.send(choose_spreads())
    
client.run(os.environ['TOKEN'])

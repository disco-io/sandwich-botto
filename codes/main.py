import discord
import random
import os

client = discord.Client()

#fillings menu
bread = [ 'bagel', 'baguette', 'biscuit', 'brioche', 'brown bread', 'challah', 'ciabatta', 'cornbread', 'croissant', 'english muffin', 'focaccia', 'grissini', 'hawaiian roll', 'potato bread', 'rye bread', 'multi-grain bread', 'pumpernickel', 'smoked salmon', 'sourdough bread', 'white bread', 'whole wheat bread']

meat = ['bacon', 'black forest ham', 'bologna sausage', 'buffalo chicken', 'grilled chicken breast', 'honey ham', 'meatballs', 'pepperoni', 'pulled pork' 'roast beef', 'shredded chicken''steak', 'tuna', 'tuna', 'turkey salami','turkey breast']

cheese = ['american cheese', 'brie', 'cheddar', 'gouda', 'havarti', 'parmesan', 'pepper jack', 'provolone', 'swiss', 'mozzarella']

veggies = ['basil', 'coleslaw', 'diced celery', 'jalepeno' 'pickles', 'lettuce', 'olives', 'red onions', 'red peppers', 'sauteéd mushrooms', 'shredded carrots', 'sliced cucmbers', 'spinach', 'white onions','tomatoes']

spreads = ['blue cheese dressing', 'guacamole', 'honey mustard', 'hot sauce', 'mayonnaise', 'mustard', 'ranch', 'smoky bbq', 'spicy mayo', 'sweet onion dip', 'ketchup']

#in the kitchen
def make_sandwich():
 return (':bread: **bread:** ' + random.choice(bread) \
         + '\n:cut_of_meat: **meat:** ' + random.choice(meat) \
         + '\n:cheese: **cheese:** ' + random.choice(cheese) \
         + '\n:leafy_green: **veggie:** ' + random.choice(veggies) \
         + '\n:salt: **spread/sauce:** ' + random.choice(spreads))
  
#online message
@client.event
async def on_ready():
  print('{0.user}'.format(client) + ' is now up and running! ヾ(^ ∇ ^)ノ') 

@client.event
async def on_message(message):

  # if send message to self, do nothing
  if message.author == client.user:
    return
    
  # user-botto conversations
  if message.content.startswith('>hello'):
    await message.channel.send('( ´ ▽ `)ﾉ  heyo!')
    
  if message.content.startswith('>how are you?'):
    await message.channel.send('(´﹃ ` ) hungry for some sandwiches。。。 :sandwich:')

  #sandwich commands
  if message.content.startswith('>sandwich'):
    await message.channel.send(":sandwich: here's your sandwich!\n \n" + make_sandwich())

  #angry sandwich
  if message.content.startswith('>pizza'):
    await message.channel.send('( ⋋_⋌ ):anger: how offensive 。。。')
  if message.content.startswith('>burger'):
    await message.channel.send("( ⋋_⋌ ):anger: we're healhier ya know 。。。")

client.run(os.environ['TOKEN'])

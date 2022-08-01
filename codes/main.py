import discord
import random
import os

client = discord.Client()

#fillings menu
bread = [ 'bagel', 'baguette', 'biscuit', 'brioche', 'brown bread', 'challah', 'ciabatta', 'cornbread', 'croissant', 'english muffin', 'focaccia', 'grissini', 'hawaiian roll' 'potato bread' 'rye bread', 'multi-grain bread', 'pumpernickel', 'smoked salmon', 'sourdough bread', 'white bread', 'whole wheat bread']

meat = ['bacon', 'black forest ham', 'bologna sausage', 'buffalo chicken', 'grilled chicken breast', 'honey ham', 'meatballs', 'pepperoni', 'pulled pork' 'roast beef', 'shredded chicken''steak', 'tuna', 'tuna' , 'turkey salami','turkey breast']

cheese = ['american cheese', 'brie', 'cheddar', 'gouda', 'havarti', 'parmesan', 'pepper jack', 'provolone', 'swiss', 'mozzarella']

veggies = ['coleslaw', 'diced celery', 'jalepeno' 'pickles', 'lettuce', 'olives', 'red onions', 'red peppers', 'sauteéd mushrooms', 'shredded carrots', 'sliced cucmbers', 'spinach', 'white onions','tomatoes']

spreads = ['blue cheese dressing', 'guacamole', 'honey mustard', 'hot sauce', 'mayonnaise', 'mustard', 'ranch', 'smoky bbq', 'spicy mayo', 'sweet onion dip', 'ketchup']

#in the kitchen
def make_sandwich():
 return 

#online message
@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) 

@client.event
async def on_message(message):

  # if send message to self, do nothing
  if message.author == client.user:
    return
    
  # botto receives >command and returns message
  if message.content.startswith('>hello'):
    await message.channel.send('( ´ ▽ `)ﾉ  heyo!')
    
  if message.content.startswith('>how are you?'):
    await message.channel.send('(´﹃ ` ) hungry for some sandwiches。。。 :sandwich:')

  if message.content.startswith(''):
    await message.channel.send('')

  #angry sandwich
  if message.content.startswith('>pizza'):
    await message.channel.send('( ⋋_⋌ ):anger: how offensive 。。。')

# it's a secret... :x
client.run(os.environ['TOKEN'])

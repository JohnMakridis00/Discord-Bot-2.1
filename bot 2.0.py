# Work with Python 3.6
import random
import discord
import asyncio
import aiohttp
import json
import os
from discord import Game
from discord.ext import commands
from discord.ext.commands import bot, Bot
import discord.ext.commands

BOT_PREFIX = "?"
client = commands.Bot(command_prefix=BOT_PREFIX)


TOKEN = " "  # Get at discordapp.com/developers/applications/me



#8BALL
@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#FORTUNE.COOKIES
@client.command(name='fortune',
                description="Tells you your fortune",
                brief="Answers from your chinese master.",
                aliases=['4tune', 'for', 'fortune_cookie'],
                pass_context=True)
async def fortune_cookie(context):
    possible_responses = [
        'The early bird gets the worm, but the second mouse gets the cheese.',
        'Be on the alert to recognize your prime at whatever time of your life it may occur.',
        'Your road to glory will be rocky, but fulfilling.',
        'Courage is not simply one of the virtues, but the form of every virtue at the testing point.',
        'Nothing is impossible to a willing heart.',
        'Don’t worry about money. The best things in life are free.',
        'Don’t pursue happiness – create it.',
        'Courage is not the absence of fear; it is the conquest of it.',
        'Nothing is so much to be feared as fear.',
        'All things are difficult before they are easy.',
        'The real kindness comes from within you.',
        'A ship in harbor is safe, but that’s not why ships are built.',
        'You don’t need strength to let go of something. What you really need is understanding.',
        'If you want the rainbow, you have to tolerate the rain.',
        'Fear is interest paid on a debt you may not owe.',
        'Hardly anyone knows how much is gained by ignoring the future.',
        'The wise man is the one that makes you think that he is dumb.',
        'The usefulness of a cup is in its emptiness.',
        'He who throws mud loses ground.',
        'Success lies in the hands of those who wants it.',
        'To avoid criticism, do nothing, say nothing, be nothing.',
        'One that would have the fruit must climb the tree.',
        'It takes less time to do a thing right than it does to explain why you did it wrong.',
        'Big journeys begin with a single step.',
        'Of all our human resources, the most precious is the desire to improve.',
        'Do the thing you fear and the death of fear is certain.',
        'You never show your vulnerability, you are always self assured and confident.',
        'People learn little from success, but much from failure.',
        'Be not afraid of growing slowly, be afraid only of standing still.',
        'We must always have old memories and young hopes.',
        'A person who won’t read has no advantage over a person who can’t read.',
        'He who expects no gratitude shall never be disappointed.',
        'I hear and I forget. I see and I remember. I do and I understand.',
        'The best way to get rid of an enemy is to make a friend.',
        'It’s amazing how much good you can do if you don’t care who gets the credit.',
        'Never forget that a half truth is a whole lie.',
        'Happiness isn’t an outside job, it’s an inside job.',
        'If you do no run your subconscious mind yourself, someone else will.',
        'Yes by calling full, you created emptiness.',
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)

#BOT LOGS
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with faggots"))
    print("Logged in as " + client.user.name)

#COIN.FLIP
@client.command(name='cf',
                description="Flips a coin",
                brief="Just random bullshit.",
                aliases=['coin', 'flip', 'coinf'],
                pass_context=True)
async def coinflip(context):
    msg = ['Heads',
            'Tails',
            'side']
    await client.say(random.choice(msg) + ", " + context.message.author.mention)

#BITCOIN.PRICE
@client.command()
async def bitcoin():
    url = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    async with aiohttp.ClientSession() as session:  # Async HTTP request
        raw_response = await session.get(url)
        response = await raw_response.text()
        response = json.loads(response)
        await client.say("Bitcoin price is: $" + response['bpi']['USD']['rate'])

#SPECIFIC.MESSAGES
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('?hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
    elif message.content.startswith('?bot'):
        await client.send_message(message.channel, "Ti 8es re malaka uwu?")
    elif message.content.startswith('?league'):
        await client.send_message(message.channel, "Karkinopaixnido")
    elif message.content.startswith('?developer'):
        await client.send_message(message.channel, "My developer is John M.")
    elif message.content.startswith('?$'):
        await client.send_message(message.channel, data[ctx.message.author.id]['level'])

    await client.process_commands(message) #important so it still reads commands


#CLEAR.MESSAGES
@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount) + 1):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say(limit, 'messages deleted')

#JOIN.VOICE
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice_channel
    await client.join_voice_channel(channel)

#LEAVE.VOICE
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    if voice_client:
        await voice_client.disconnect()
        print("Bot left the voice channel")
    else:
        print("Bot was not in channel")



#SERVERS
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(60000)



@client.event
async def on_member_join(member):
    with open('users.jason', 'r') as f:
        users = json.load(f)

    await update_data(users, member)

    with open('users.json', 'w') as f:
        json.dump(users, f)


client.loop.create_task(list_servers())
client.run(TOKEN)

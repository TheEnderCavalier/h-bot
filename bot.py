import discord
import asyncio
client = discord.Client()
@client.event
async def on_ready():
    print('Logged in')
    print('Bot name:', client.user.name)
    print('ID:', client.user.id)
    await client.send_message(client.get_channel('335412994139881473'), 'h')
@client.event
async def on_message(message):
    if message.channel==client.get_channel('335412994139881473'):
        await client.send_message(message.channel, 'h')
    if message.channel==client.get_channel('335423665896292362'):
        countupH=str(int(message.content[0:len(message.content)-1])+1)
        await client.send_message(message.channel, countupH+'h')
    if message.channel==client.get_channel('335430931638779906'):
        countdownH=str(int(message.content[0:len(message.content)-1])-1)
        await client.send_message(message.channel, countdownH+'h')
    if message.channel==client.get_channel('335432096443269120'):
        # Blame ricelord7
        await client.send_message(message.channel, str(format(int(message.content[:-1],16)+1,'x')).upper()+'h')
    if message.channel==client.get_channel('335433358530052096'):
        await client.send_message(message.channel, message.content+'h')
client.run('your-token')


import discord
import asyncio

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    channel = discord.Object(id='270749653975302144')
    while not client.is_closed:
        await asyncio.sleep(60) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.loop.create_task(my_background_task())
client.run('NDA1MTEzMDc3NzkzODE2NTg2.DUf8pA.xHvVVJZIfVf8qGvrSbZ0CXfOl0o')

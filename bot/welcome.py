import discord
import asyncio

client = discord.Client()

@client.event
async def on_member_join(member):
    server = member.server
    fmt = 'Welcome {0.mention} to {1.name}!'
    await client.send_message(server, fmt.format(member, server))

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run('NDA1MTEzMDc3NzkzODE2NTg2.DUf8pA.xHvVVJZIfVf8qGvrSbZ0CXfOl0o')

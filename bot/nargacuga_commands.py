from datetime import datetime

import discord
from discord.ext import commands
import random
import pytz

from config import constants

description = ''
bot = commands.Bot(command_prefix='!', description=description)
monster = ["great-jaggi", "great-baggi", "great-wroggi", "arzuros", "lagombi", "volvidon", 
"qurupeco", "crimson-qurupeco", "barroth", "jade-barroth", "uragaan", "steel-uragaan", 
"duramboros", "rust-duramboros", "rathian", "pink-rathian", "gold-rathian", "rathalos", 
"azure-rathalos", "silver-rathalos", "diablos", "black-diablos", "gigginox", "baleful-gigginox", 
"barioth", "sand-barioth", "royal-ludroth", "purple-ludroth", "gobul", "nibelsnarf", "lagiacrus",
"ivory-lagiacrus", "abyssal-lagiacrus", "agnaktor", "glacial-agnaktor", "nargacuga", 
"green-nargacuga", "lucent-nargacuga", "zinogre", "stygian-zinogre", "plesioth", "green-plesioth",
"brachydios", "ceadeus", "goldbeard-ceadeus", "deviljho", "savage-deviljho", "jhen-mohran", 
"hallowed-jhen-mohran", "alatreon", "dire-miralis"]

@bot.command(description='For when you want to know who is the very best')
async def best():
    """Who is the best Monster?"""
    await bot.say('Nargacuga is the best Monster.  Are you casual?')

@bot.command(description='Show time until upcoming Monster Hunter World releases')
async def countdown():
    """Time till next MHW release"""
    await bot.say('Monster Hunter World will release on January 26, 2018')

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await bot.say('{0.name} joined in {0.joined_at}'.format(member))

@bot.command()
async def wherearemypants():
    """Will determine who the pants thief is"""
    await bot.say('justin is a known pants thief. Not saying he took them but he totally probably took them')

@bot.command()
async def monster(member : monster):
    """Get info on a monster from Kiranico's site"""
    await bot.say (result)

@bot.command()
async def fairest():
    """Who is the fairest in all the land?"""
    await bot.say('Mayguns')

bot.run('NDA1MTEzMDc3NzkzODE2NTg2.DUf8pA.xHvVVJZIfVf8qGvrSbZ0CXfOl0o')

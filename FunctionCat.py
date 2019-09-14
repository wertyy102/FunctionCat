# These are the dependencies. The bot depends on these to function, hence the name. Please do not change these unless you're adding to them, because they can break the bot.
import logging
from logging.handlers import RotatingFileHandler
import random
import sqlite3
import traceback
import time
import datetime
import sys
import os
import hashlib
import asyncio
import aiohttp
from collections import Counter
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import platform

# Here you can modify the bot's prefix and description and whether it sends help in direct messages or not.
client = Bot(description="A useful bot to help with servers", command_prefix="~", pm_help = True)

# This is what happens every time the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Current Discord.py Version: {} | Current Python Version: {}'.format(discord.__version__, platform.python_version()))
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')
	return await client.change_presence(game=discord.Game(name='~help'))

#pingpong command
@client.command()
async def ping(*args):
	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	
client.run("BOTKEYGOESHERE")

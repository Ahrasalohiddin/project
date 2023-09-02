import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def ecosort(ctx):
  random_fact = random.choice(['Каждый шестой житель нашей планеты существует в неблагоприятных и опасных для его здоровья и жизни условиях', 'Примерно 650-720 миллионов жителей Китая пьют не чистую, а загрязненную питьевую воду', 'Ежегодно на Земле вырубается около 11-12 миллионов тропических лесов, а насаживается в 10 раз меньше'])
  await ctx.send(random_fact)
bot.run('MTE0NDI1NDMwMTk3NjQwODA2NQ.GVcGWZ.wgrikgmGMWnWXt16il0t-EBy0EE6VITyfmh9ko')

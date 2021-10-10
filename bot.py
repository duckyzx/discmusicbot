import discord
from discord.ext import commands

#import all of the cogs
from music_cog import music_cog

Bot = commands.Bot(command_prefix='/')
Bot.add_cog(music_cog(Bot))
@Bot.command()
async def echo(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)

token = ""
with open("token.txt") as file:
    token = file.read()
Bot.run(token)
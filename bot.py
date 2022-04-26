BOT_PREFIX = "PREFIX"
BOT_TOKEN = "TOKEN"
import nextcord
from nextcord.ext import commands
from keep_alive import keep_alive
bot = commands.Bot(command_prefix=BOT_PREFIX, intents=nextcord.Intents.all())
@bot.event
async def on_ready():
    print("Logged in as", bot.user.name)
    bot.remove_command('help')
@commands.guild_only()
@bot.command()
async def join(ctx):
    if ctx.message.author.guild_permissions.administrator:
        channel = ctx.author.voice.channel
        await channel.connect()
@commands.guild_only()
@bot.command()
async def leave(ctx):
    if ctx.message.author.guild_permissions.administrator:
        await ctx.voice_client.disconnect()

keep_alive()
bot.run(BOT_TOKEN)

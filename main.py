import discord
import pyautogui
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="=")
TOKEN = "put discord token here"


@client.event
async def on_ready():
    game = discord.Game("with lights")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Bot is online!")



@client.command(name= "info")
async def info(ctx, member: discord.Member =None):
    embed = discord.Embed(color=0x9999df, timestamp=ctx.message.created_at, title="Commands")
    embed.set_footer(text=f"Whats good, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="```Red LED```", value="**=redon, =redoff**")
    embed.add_field(name="```Green LED```", value="**=greenon, =greenoff**")
    embed.add_field(name="```Blue LED```", value="**=blueon, =blueoff**")

    await ctx.send(embed=embed)

@client.command(name= "redon")
async def redon(ctx, member: discord.Member =None):
    pyautogui.typewrite("1")
    pyautogui.press("enter")
    embed = discord.Embed(color=0x0000df, timestamp=ctx.message.created_at, title="Red LED has been turned ```ON```" )
    embed.set_footer(text=f"Stop playing with lights, {ctx.author}", icon_url=ctx.author.avatar_url)
    print("REDON")

    await ctx.send(embed=embed)

@client.command(name= "redoff")
async def redoff(ctx, member: discord.Member =None):
    pyautogui.typewrite("2")
    pyautogui.press("enter")
    embed = discord.Embed(color=0x8080df, timestamp=ctx.message.created_at, title="Red LED has been turned ```OFF```" )
    embed.set_footer(text=f"Stop playing with lights, {ctx.author}", icon_url=ctx.author.avatar_url)
    print("REDOFF")

    await ctx.send(embed=embed)

@client.command(name= "greenon")
async def greenon(ctx, member: discord.Member =None):
    pyautogui.typewrite("3")
    pyautogui.press("enter")
    embed = discord.Embed(color=0x8080df, timestamp=ctx.message.created_at, title="Green LED has been turned ```ON```" )
    embed.set_footer(text=f"Stop playing with lights, {ctx.author}", icon_url=ctx.author.avatar_url)
    print("GREENON")

    await ctx.send(embed=embed)

@client.command(name= "greenoff")
async def greenoff(ctx, member: discord.Member =None):
    pyautogui.typewrite("4")
    pyautogui.press("enter")
    embed = discord.Embed(color=0x8080df, timestamp=ctx.message.created_at, title="Green LED has been turned ```OFF```" )
    embed.set_footer(text=f"Stop playing with lights, {ctx.author}", icon_url=ctx.author.avatar_url)
    print("GREENOFF")

    await ctx.send(embed=embed)

@client.command(name= "blueon")
async def blueon(ctx, member: discord.Member =None):
    pyautogui.typewrite("5")
    pyautogui.press("enter")
    embed = discord.Embed(color=0x8080df, timestamp=ctx.message.created_at, title="Blue LED has been turned ```ON```" )
    embed.set_footer(text=f"Stop playing with lights, {ctx.author}", icon_url=ctx.author.avatar_url)
    print("BLUEON")

    await ctx.send(embed=embed)

@client.command(name= "blueoff")
async def blueoff(ctx, member: discord.Member =None):
    pyautogui.typewrite("6")
    pyautogui.press("enter")
    embed = discord.Embed(color=0x8080df, timestamp=ctx.message.created_at, title="Blue LED has been turned ```OFF```" )
    embed.set_footer(text=f"Stop playing with lights, {ctx.author}", icon_url=ctx.author.avatar_url)
    print("BLUEOFF")

    await ctx.send(embed=embed)

client.run(TOKEN)



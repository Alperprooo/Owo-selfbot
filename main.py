import discord
from discord.ext import commands, tasks
import time
import asyncio
from webserver import keep_alive
import os
import random
import traceback
version = 'v2.7.4'

keep_alive()

#Fill up these values to use the selfbot
self_bot_prefix="."
token = os.environ["TOKEN"]
channelid= 1071656675850854510
ownerid = 866186448309583903



bot = commands.Bot(command_prefix=self_bot_prefix)
owoid=408785106942164992
intervals = [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6]
flip = [9.0,10.0,11.0,12.0,13.0,14.0]
owoh = [14.0,15.0,16.0,17.0,18.0,19.0,20.0]
channelid=int(channelid)
ownerid=int(ownerid)
@tasks.loop(seconds=random.choice(intervals))
async def spam():
    channel = bot.get_channel(int(channelid))
    await asyncio.sleep(random.choice(owoh))
    await channel.send('owoh')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully owoh")
    await asyncio.sleep(random.choice(owoh))
    await channel.send('owo sell all')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully sell")
    await channel.send('owo flip 500')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully owo flip 500")
    await asyncio.sleep(random.choice(flip))
    await channel.send('owo cash')
    def check(message):
        return message.author.id==owoid and message.channel==channel
    try:
        reply=await bot.wait_for('message', check=check, timeout=30.0)
    except asyncio.TimeoutError:
        print("Owo didn't reply")
        user=bot.get_user(ownerid)
        await user.send(f"Owo bot didn't replied. Turning off myself. Use {self_bot_prefix}grind to wake me up")
        spam.cancel()
        return
    print(f"succefully cash")
    await asyncio.sleep(random.choice(flip))


@spam.before_loop
async def before_spam():
    await bot.wait_until_ready()

spam.start()
@bot.event
async def on_ready():
    print(f"{bot.user.name} is online")

@bot.command()
async def say(ctx, *, args):
    if ctx.author.id==owner:
        await ctx.send(args)



@bot.event
async def on_message(message):
    user=bot.get_user(bot.user.id)
    if message.guild:
        if f"{bot.user.name}! Please complete your captcha" in message.content:
            if message.author.id==owoid:
                member = message.guild.get_member(bot.user.id)
                if f"{member.display_name}! Please complete your captcha" in message.content:
                    spam.cancel()
                
    elif message.channel==user.dm_channel:
        if message.author.id==owoid:
            if "Are you a real human?" in message.content:
                spam.cancel()
                image = message.attachments[0]
                user=bot.get_user(ownerid)
                await user.send(image)
            elif "I have verified that you are human! Thank you!" in message.content:
                msg = message.content
                user=bot.get_user(ownerid)
                await user.send(msg)
                spam.start()
                
        elif message.author.id==ownerid:
            text = message.content.strip()
            if "captcha" in text.lower():
                captcha=text.split(" ",1)[1]
                user=bot.get_user(owoid)
                await user.send(captcha)
            
        
@bot.command()
async def hold(ctx, *, args:str = None):
    await ctx.message.delete()
    await ctx.send('Got it bro!')
    spam.cancel()
    
@bot.command()
async def grind(ctx, *, args:str = None):
    await ctx.message.delete()
    await ctx.send("Ok, let's go")
    spam.start()

try:
    bot.run(f"{token}")
except discord.HTTPException:
    while True:
        time.sleep(10)
        os.system("kill 1")
except:
    traceback.print_exc()
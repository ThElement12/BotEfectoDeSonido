import asyncio
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


GUILD_VC_TIMER = {}


# COMMANDS

@bot.command(name='tiku')
async def join(ctx):
    # grab the user who sent the command
    voice_channel = ctx.author.voice.channel
    # only play music if user is in a voice channel
    if voice_channel is not None:
        await voice_channel.connect()
        await ctx.send("Llegue yo, klk")
    else:
        await bot.say('User is not in a channel.')


@bot.command(name="notiku")
async def leave(ctx):
    await ctx.send("Se me cuida, hablamo' el martes")
    await ctx.voice_client.disconnect()


@bot.command(name="stop")
async def stop_talking(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
    vc.stop()


@bot.command(name="effect")
async def effect(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_connected():
            vc = await voice_channel.connect()

        vc.play(discord.FFmpegPCMAudio('Sounds/Tiku tiku tikuuu.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.send('User is not in a channel.')


@bot.command(name="tiradera")
async def tiradera(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_connected():
            vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Sounds/Tiradera.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.send('User is not in a channel.')


@bot.command(name="desorden")
async def tiradera(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_connected():
            vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Sounds/Desorden.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.send('User is not in a channel.')


@bot.command(name="babaji")
async def tiradera(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_connected():
            vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Sounds/Babaji.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.send('User is not in a channel.')


@bot.command(name="quehuevo")
async def quehuevo(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_connected():
            vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Sounds/QueWevo.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.send('User is not in a channel.')


@bot.command(name="burro")
async def quehuevo(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        vc = discord.utils.get(ctx.bot.voice_clients, guild=ctx.guild)
        if not vc or not vc.is_connected():
            vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Sounds/Burro.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.send('User is not in a channel.')


# EVENTS
@bot.listen('on_message')
async def on_message(message):
    if "que jablador" in message.content.lower():
        await message.channel.send("Hmmm que bajo a gaveta")
    elif "a tu edad" in message.content.lower():
        await message.channel.send("Va seguiii'")
    elif "mr.worldwide" in message.content.lower().replace(" ", ""):
        user_id = "<@381106739174440962>"
        await message.channel.send(f'{user_id} dale, a mi me gusta la pepsi')
    elif "hacks" in message.content.lower():
        user_id = "<@213129423728279554>"
        await message.channel.send(f'{user_id} loco te llaman')
    elif "klk" == message.content.lower() or "hola" == message.content.lower() or "hello" == message.content.lower():
        await message.channel.send("Klk dame lu' de lo mio, pa' donde la vuelta?")
    elif "rata" in message.content.lower() or "raton" in message.content.lower():
        user_id = "<@463892349806706691>"
        await message.channel.send(f'{user_id} loco te llaman')


@bot.event
async def on_voice_state_update(member, before, after):
    # if event is triggered by the bot? return
    if member.id == bot.user.id:
        return

    if not before.channel and after.channel:
        voice = discord.utils.get(bot.voice_clients, channel__guild__id=after.channel.guild.id)
        voice.play(discord.FFmpegPCMAudio('Sounds/Tiku tiku tikuuu.mp3'), after=lambda e: print('done', e))
        while voice.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        voice.stop()
    # when before.channel != None that means user has left a channel
    if before.channel is not None:
        voice = discord.utils.get(bot.voice_clients, channel__guild__id=before.channel.guild.id)
        # voice is voiceClient and if it's none? that means the bot is not in an y VC of the Guild that triggerd this
        # event
        if voice is None:
            return
        # if VC left by the user is not equal to the VC that bot is in? then return
        if voice.channel.id != before.channel.id:
            return
        # if VC has only 1 member (including the bot)
        if len(voice.channel.members) <= 1:
            GUILD_VC_TIMER[before.channel.guild.id] = 0
            while True:
                print("Time", str(GUILD_VC_TIMER[before.channel.guild.id]), "Total Members",
                      str(len(voice.channel.members)))
                await asyncio.sleep(1)
                GUILD_VC_TIMER[before.channel.guild.id] += 1
                # if vc has more than 1 member or bot is already disconnectd ? break
                if len(voice.channel.members) >= 2 or not voice.is_connected():
                    break
                # if bot has been alone in the VC for more than 60 seconds ? disconnect
                if GUILD_VC_TIMER[before.channel.guild.id] >= 5:
                    await voice.disconnect()
                    return


bot.run(TOKEN)

# TODO
# Sonido de aldeano
# Sonido cuando alguien se desmutea
# Sonido vas a seguirrr

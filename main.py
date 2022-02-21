import os
import asyncio
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

# this event runs when user leave / join / defen / mute
@bot.event
async def on_voice_state_update(member, before, after):
    # if event is triggered by the bot? return
    if member.id == bot.user.id:
        return

    if after.channel is not None:
        voice = discord.utils.get(bot.voice_clients, channel__guild__id=after.channel.guild.id)
        print("Kedyavlos")
        voice.play(discord.FFmpegPCMAudio('Tiku tiku tikuuu.mp3'), after=lambda e: print('done', e))
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


@bot.command(name='tiku')
async def join(ctx):
    # grab the user who sent the command
    voice_channel = ctx.author.voice.channel
    # only play music if user is in a voice channel
    if voice_channel is not None:
        await voice_channel.connect()
    else:
        await bot.say('User is not in a channel.')


@bot.command(name="notiku")
async def leave(ctx):
    await ctx.send("byee")
    await ctx.voice_client.disconnect()


@bot.command(name="effect")
async def effect(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Tiku tiku tikuuu.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.say('User is not in a channel.')

@bot.command(name="tiradera")
async def tiradera(ctx):
    voice_channel = ctx.author.voice.channel
    if voice_channel is not None:
        # grab user's voice channel
        # create StreamPlayer
        vc = await voice_channel.connect()
        vc.play(discord.FFmpegPCMAudio('Tiradera.mp3'), after=lambda e: print('done', e))
        while vc.is_playing():
            await asyncio.sleep(1)
        # disconnect after the player has finished
        vc.stop()
    else:
        await bot.say('User is not in a channel.')

bot.run(TOKEN)

import discord
import os
# load our local env so we dont have the token in public
from playsound import playsound
from dotenv import load_dotenv
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
import json
import vlc
import requests
load_dotenv()
client = commands.Bot(command_prefix='`')  # prefix our commands with '.'

players = {}


@client.event  # check if bot is ready
async def on_ready():
    print('Bot online')


# command for bot to join the channel of the user, if the bot has already joined and is in a different channel, it will move to the channel the user is in
@client.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@client.command()
async def leave(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

# command to play sound from a youtube URL
@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'default_search': 'auto'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    channel = ctx.message.author.voice.channel
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        print(info)
        entries = info['entries']
        entries = (entries)[0]
        URL = entries['url']
        print(URL)
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return

@client.command()
async def maybe(ctx):
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    channel = ctx.message.author.voice.channel
    try:
        voice = await channel.connect()
    except:
        pass
    voice.play(FFmpegPCMAudio('https://tunein.com/todays-hits', **FFMPEG_OPTIONS))

@client.command()
async def maybe3(ctx):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    I_URL = 'http://stream.revma.ihrhls.com/zc185/hls.m3u8'#'https://stream.revma.ihrhls.com/zc4429/hls.m3u8'
    
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    print(I_URL)
    source = discord.FFmpegPCMAudio(I_URL, **FFMPEG_OPTIONS)
    p = vlc.MediaPlayer(I_URL)
    p.audio_set_volume(35)
    p.play()
    voice.play(source)
    voice.is_playing()


@client.command()
async def maybe2(ctx, arg):
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    YDL_OPTIONS = {'format': 'bestaudio/best', 'noplaylist':'True'}

    url1 = arg.split(" ")
    url2 = url1[0].replace("[","")
    url = url2.replace("]","")
    
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    ydl = YoutubeDL(YDL_OPTIONS)
    with ydl:
        info = ydl.extract_info(url, download=False)
        I_URL = info['formats'][0]['url']
        print(I_URL)
        source = discord.FFmpegPCMAudio(I_URL, **FFMPEG_OPTIONS)
        voice.play(source)
        voice.is_playing()

# command to resume voice if it is paused
@client.command()
async def resume(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Bot is resuming')


# command to pause voice if it is playing
@client.command()
async def pause(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('Bot has been paused')


# command to stop voice
@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Stopping...')



# command to clear channel messages
@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Messages have been cleared")


client.run('Njc4NzU4NjgyMjc1NjEwNjI3.XkndSA.vc1IIpGRDdfptGj7CL1kerBdlMo')
import discord
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext import tasks
from discord.player import FFmpegAudio
import youtube_dl


queue = []
loop = False

class Music(commands.Cog):
    def __init__(self, client):
        self.client = client


    # -----------| Join |-----------

    @commands.command()
    async def join(self, ctx):
        if ctx.author.voice is None:
            await ctx.send("Masuk voice channel dulu blok!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)


    # -----------| Disconnect |-----------

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()
    
    @commands.command()
    async def dc(self, ctx):
        await ctx.voice_client.disconnect()

    
    # -----------| Play |-----------

    @commands.command()
    async def play(self, ctx, url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def p(self, ctx, url):
        # Join

        if ctx.author.voice is None:
            await ctx.send("Masuk voice channel dulu blok!")
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

        # Play

        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options':'-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options':'-vn'}
        YDL_OPTIONS = {'format':"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)
        

    # -----------| Pause |-----------    

    @commands.command()
    async def pause(self, ctx):
        await ctx.send ("Paused ⏸")
        await ctx.voice_client.pause()


    # -----------| Resume |-----------
    
    @commands.command()
    async def resume(self, ctx):
        await ctx.send("Resume ⏯")
        await ctx.voice_client.resume()

    
    # -----------| Loop |-----------
    
    @commands.command()
    async def loop(self, ctx):
        global loop

        if loop:
            await ctx.send('Loop mode is now `False!`')
            loop = False
        
        else: 
            await ctx.send('Loop mode is now `True!`')
            loop = True
        
        # tasks.loop()


    # -----------| Queue |-----------
    
    # @commands.command()
    # async def queue(self, ctx):
    #     global queue

    #     queue.append()
    #     await ctx.send(f'`{url}` added to queue!')



def setup(client):
    client.add_cog(Music(client))





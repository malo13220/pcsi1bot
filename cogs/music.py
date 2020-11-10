import os
import shutil
from os import system
import asyncio
import discord
import youtube_dl
import datetime
from datetime import datetime
from discord.ext import commands
from discord.utils import get

youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

'''
DESACTIVEE
'''

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume = 0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.thumbnail = data.get('thumbnail')
        self.description = data.get('description')
        self.duration = self.parse_duration(int(data.get('duration')))
        self.url = data.get('webpage_url')


    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

    @staticmethod
    def parse_duration(duration: int):
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)

        duration = []
        if days > 0:
            duration.append('{} days'.format(days))
        if hours > 0:
            duration.append('{} hours'.format(hours))
        if minutes > 0:
            duration.append('{} minutes'.format(minutes))
        if seconds > 0:
            duration.append('{} secondes'.format(seconds))

        return ', '.join(duration)

class Music(commands.Cog, name = 'Music Player'):
    def __init__(self, bot):
        self.bot = bot

    pass

    def good_channel(ctx):
        if ctx.channel.name == 'commandes-musique':
            return True
        else : return False

    @commands.command()
    @commands.check(good_channel)
    async def start(self, ctx):
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
            embed  =  discord.Embed(
                    title = "Connection réussie",
                    description = "Pour commencer la lecture d'une musique taper !play suivi de l'url ou du titre de la musique \n \n :warning: : Vous devez faire !pause avant de refaire !play \n \n Avertissement : certaines musique sont plus fort que d'autres au lancement mais vous pouvez choisir le volume avec !volume XX% \n \n Vous pouvez faire :play_pause: avec !pause et !resume ",
                    color =  16711929
                )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            embed.set_author(name ='Music player')
            await ctx.channel.purge(limit = None)
            global msg1
            msg1 = await ctx.send(embed = embed)



        else:
            embed  =  discord.Embed(
                    title = "Vous n'êtes pas connecté au salon audio",
                    description = 'Pour commencer connectez vous au salon audio puis faite !start pour faire venir le bot',
                    color =  16711929
                )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            embed.set_author(name ='Music player')
            await ctx.send(embed = embed)
            return
            global vc

        try:
            vc=await channel.connect()

        except:
            TimeoutError


    @commands.command()
    @commands.check(good_channel)
    async def play(self, ctx, *, url):
        """Lis une vidéo en la télechargent"""
        if ctx.author.voice and ctx.author.voice.channel:
            channel = ctx.author.voice.channel
        async with ctx.typing():
            global player

            global name


            nplayer = await YTDLSource.from_url(url, loop=self.bot.loop)
            try :
                vc.play(nplayer, after=lambda e: print('Player error: %s' % e) if e else None)
            except Exception as e:
                await ctx.channel.purge(limit =1)
                embedE = discord.Embed(
                    description = 'Erreur : veuillez attendre la fin de la chanson ou faire !stop puis redémarer le player',
                    color =  16711929
                )
                embedE.set_footer(text='PCSI Bot by @Malo Tiriau')
                await asyncio.sleep(2)
                await ctx.send(embed = embedE)
                await ctx.channel.purge(limit =1)
            else :
                name = ctx.author.mention
                ctx.voice_client.source.volume = 25 / 100
                player = nplayer
                embed  =  discord.Embed(
                    title = ':arrow_forward: Lecture en cours : ',
                    description = f'{player.title} \n {player.duration} \n \n',
                    color =  16711929
                )
                embed.set_thumbnail(url=player.thumbnail)
                embed.set_footer(text='PCSI Bot by @Malo Tiriau')
                embed.set_author(name ='Music player')
                embed.add_field(name = 'Proposé par : ', value = f'{name}')
                embed.add_field(name = 'Volume :', value = f'{ctx.voice_client.source.volume*100} %')
                embed.add_field(name = 'Liste de lecture', value = "WIP")
                def not_msg1(m):
                        return m.id != msg1.id
                await ctx.channel.purge(limit = None, check=not_msg1)
                await ctx.send(embed = embed)



    @commands.command()
    @commands.check(good_channel)
    async def volume(self, ctx, volume: int):
        """Changer le volume du player (réservé aux admins)"""

        if ctx.voice_client is None:
            return await ctx.send("Non connecté au salon vocal")

        ctx.voice_client.source.volume = volume / 100

        def not_msg1(m):
            return m.id != msg1.id
        await ctx.channel.purge(limit = None, check=not_msg1)
        embed  =  discord.Embed(
            title = ':arrow_forward: Lecture en cours : ',
            description = f'{player.title} \n {player.duration} \n \n',
            color =  16711929
        )
        embed.set_thumbnail(url=player.thumbnail)
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        embed.set_author(name ='Music player')
        embed.add_field(name = 'Proposé par : ', value = f'{name}')
        embed.add_field(name = 'Volume :', value = f'{ctx.voice_client.source.volume*100} %')
        embed.add_field(name = 'Liste de lecture', value = "WIP")
        await ctx.send(embed = embed)





    @commands.command()
    @commands.check(good_channel)
    async def pause(self, ctx):

        voice = ctx.voice_client

        if voice and voice.is_playing():
            voice.pause()
            def not_msg1(m):
                return m.id != msg1.id
            await ctx.channel.purge(limit = None, check=not_msg1)
            embed  =  discord.Embed(
                title = ':pause_button:  Pause : ',
                description = f'Lecture en pause pour reprendre : !resume \n\n{player.title} \n {player.duration} \n \n',
                color =  16711929
            )
            embed.set_thumbnail(url=player.thumbnail)
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            embed.set_author(name ='Music player')
            embed.add_field(name = 'Proposé par : ', value = f'{name}')
            embed.add_field(name = 'Volume :', value = f'{ctx.voice_client.source.volume*100} %')
            embed.add_field(name = 'Liste de lecture', value = "WIP")
            await ctx.send(embed = embed)


        else:
            print("Music not playing failed pause")


    @commands.command()
    @commands.check(good_channel)
    async def resume(self, ctx):

        voice = ctx.voice_client

        if voice and voice.is_paused():
            voice.resume()
            def not_msg1(m):
                return m.id != msg1.id
            await ctx.channel.purge(limit = None, check=not_msg1)
            embed  =  discord.Embed(
                title = ':arrow_forward: Lecture en cours : ',
                description = f'{player.title} \n {player.duration} \n \n',
                color =  16711929
            )
            embed.set_thumbnail(url=player.thumbnail)
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            embed.set_author(name ='Music player')
            embed.add_field(name = 'Proposé par : ', value = f'{name}')
            embed.add_field(name = 'Volume :', value = f'{ctx.voice_client.source.volume*100} %')
            embed.add_field(name = 'Liste de lecture', value = "WIP")
            await ctx.send(embed = embed)

        else:
            print("Music is not paused")



    @commands.command()
    @commands.check(good_channel)
    async def stop(self, ctx):
        """Arrêter la lecture"""

        await ctx.voice_client.disconnect()
        embed  =  discord.Embed(
            title = 'Arrêt',
            description = 'Player musique arrêté',
            color =  16711929
        )
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        embed.set_author(name ='Music Player')
        await ctx.send(embed = embed)
        await asyncio.sleep(1)
        await ctx.channel.purge(limit = None)

def setup(bot):
    bot.add_cog(Music(bot))

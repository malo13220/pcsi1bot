#!/usr/bin/python

#Création Malo Tiriau 2020
#Version 1.1

import discord
import random
import os
import asyncio
import youtube_dl
import datetime
from datetime import date
from discord.ext import commands


bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'))

bot.load_extension('cogs.matière')
bot.load_extension('cogs.moderation')
#bot.load_extension('cogs.explorer')  désactivé
bot.load_extension('cogs.fun')
#bot.load_extension('cogs.music')      désactivé

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('!aide pour les commandes'))
    print('Bot is ready')

@bot.event
async def on_member_join(member):
    print(f'{member} a rejoint le serveur')

@bot.event
async def  on_member_remove(member):
    print(f'{member} a quitté le serveur')


"""
fun loading
"""
#commande fun automatiquement activées

@bot.command()
@commands.has_permissions(manage_guild=True)
async def load_fun(ctx):

    try :
        bot.load_extension('cogs.fun')
    except Exception as e:
        await ctx.send('Erreur commandes fun non chargées')
        traceback.print_exc()
    else :
        await ctx.send('Commandes fun activées')

@bot.command()
@commands.has_permissions(manage_guild=True)
async def unload_fun(ctx):

    try :
        bot.unload_extension('cogs.fun')
    except Exception as e:
        await ctx.send('Impossible les commandes ne sont pas chargées')
    else :
        await ctx.send('Commandes fun désactivées')

"""
Music loading
"""



#FONCTIONALITE DESACTIVEE
#@bot.command()
#@commands.has_permissions(manage_guild=True)
#async def load_music(ctx):

#    try :
#        bot.load_extension('cogs.music')
#     except Exception as e:
#        await ctx.send('Erreur commandes musique non chargées')
#        traceback.print_exc()
#    else :
#        await ctx.send('Commandes musique activées')

#@bot.command()
#@commands.has_permissions(manage_guild=True)
#async def unload_music(ctx):

#    try :
#        bot.unload_extension('cogs.music')
#    except Exception as e:
#        await ctx.send('Impossible les commandes ne sont pas chargées')
#    else :
#        await ctx.send('Commandes musique désactivées')


"""
Help
"""
@bot.command()
async def aide(ctx):
    embed = discord.Embed(
        title = 'PCSI Bot V1.1',
        description = "\n Fonctionalités : \n \n --------------Utilité-------------- \n \n !aide : pour afficher ce message  \n  \n [indisponible]  !appel pour faire l'appel \n !sondage pour créer des sondages \n Ajoutez la réaction :pushpin: à un message pour l'épingler \n !clear n : Pour effacer n messages (admin) \n \n ----------------Fun---------------- \n \n !fun [matière] : Pour toujours plus de fun \n !vac : pour le nombre de dodos avant les vacances \n (et une autre fonctionalité suprise) \n \n Les idées de nouvelles fonctionalités sont les bienvenues"
    )
    embed.set_footer(text='PCSI Bot by @Malo Tiriau')
    await ctx.send(embed = embed)

bot.run('Njk5Mjg2Nzc5OTY2MjU5Mjky.XpSLkA.cjvXHU2xtYepKyy_MOudrZNzO3c')

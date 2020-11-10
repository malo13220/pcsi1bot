#!/usr/bin/python

import discord
import random
import datetime
import asyncio
import os
import os.path
from pathlib import Path
from os import system
from datetime import date
from discord.ext import commands


'''
DESACTIVEE
'''

class Explorer(commands.Cog, name = 'Explorateur de fichier'):
    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=['f'])
    async def file(self, ctx):
        def disp(l) :
            a = ""
            liste = sorted(l)
            for i in range((len(liste)-1)//2):
                if liste[2*i+1][1] == '.':
                    a = a + "\n" + liste[2*i+1]
            a = a + "\n"
            for i in range(len(liste)//2):
                if liste[2*i+1][0] == '1' and liste[2*i+1][1] != '.':
                    a = a+"\n" + liste[2*i+1]
            a = a + "\n"
            for i in range(len(liste)//2):
                if liste[2*i+1][0] == '2' and liste[2*i+1][1] != '.':
                    a = a+"\n" + liste[2*i+1]
            a = a + "\n"
            for i in range(len(liste)//2):
                if liste[2*i+1][0] == '3' and liste[2*i+1][1] != '.':
                    a = a+"\n" + liste[2*i+1]
            return a
        def title(l):
            liste = sorted(l)
            return liste[len(liste)-1]

        def is_good(m):
            if m.pinned:
                return False
            elif not m.attachments :
                if  m.author != ctx.author :
                    if m.author.name != 'PCSI Bot DEV' :
                        if m.author.name != 'PCSI Bot':
                            return False
                        else : return True
                    else :
                        return True
                else :
                        return True
            else : return False

        li = os.listdir(f"./cogs/DOC")
        embed = discord.Embed(
            title = f':file_folder: {title(li)} :',
            description = f'Taper le numéro pour accéder aux dossiers : \n {disp(li)}',
            color =  15977347
        )
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        embed.set_author(name ='Explorateur de fichier (BETA)')
        a = await ctx.send(embed = embed)
        def pred(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await self.bot.wait_for("message", check=pred, timeout = 30.0)
        except asyncio.TimeoutError:
            embed1 = discord.Embed(
                description = 'Erreur : temps écoulé veuillez recommencer',
                color =  15977347
            )
            embed1.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.channel.purge(limit = 2, check = is_good)
            await ctx.send(embed = embed1)
            await asyncio.sleep(10)
            await ctx.channel.purge(limit = 1, check = is_good)

        else :
            if msg.content == '1' or msg.content == '2' or msg.content == '3' or msg.content == '4' or msg.content =='5':
                l = os.listdir(f"./cogs/DOC/{msg.content}")
                embed2 = discord.Embed(
                    title = f':file_folder: {title(li)} > {title(l)} :',
                    description = f'Taper le numéro pour accéder aux dossiers : \n {disp(l)}',
                    color =  15977347
                )
                embed2.set_footer(text='PCSI Bot by @Malo Tiriau')
                embed2.set_author(name ='Explorateur de fichier (BETA)')
                await ctx.send(embed = embed2)
                try:
                    msg2 = await self.bot.wait_for("message", check=pred, timeout = 30.0)
                except asyncio.TimeoutError:
                    embed1 = discord.Embed(
                        description = 'Erreur : temps écoulé veuillez recommencer',
                        color =  15977347
                    )
                    embed1.set_footer(text='PCSI Bot by @Malo Tiriau')
                    await ctx.channel.purge(limit = 4, check = is_good)
                    await ctx.send(embed = embed1)
                    await asyncio.sleep(10)
                    await ctx.channel.purge(limit = 1, check = is_good)
                else :
                    try :
                        l2 = os.listdir(f"./cogs/DOC/{msg.content}/{msg2.content}")
                    except Exception as e:
                        embedE = discord.Embed(
                            description = 'Erreur : entrée incorrect veuillez recommencer',
                            color =  15977347
                        )
                        embedE.set_footer(text='PCSI Bot by @Malo Tiriau')
                        await ctx.channel.purge(limit = 5, check = is_good)
                        await ctx.send(embed = embedE)
                        await asyncio.sleep(10)
                        await ctx.channel.purge(limit = 1, check = is_good)
                    else :
                        embed3 = discord.Embed(
                            title = f':file_folder: {title(li)} > {title(l)} > {title(l2)} :',
                            description = f'Taper le numéro pour accéder aux dossiers : \n {disp(l2)} \n',
                            color =  15977347
                        )
                        embed3.set_footer(text='PCSI Bot by @Malo Tiriau')
                        embed3.set_author(name ='Explorateur de fichier (BETA)')
                        await ctx.send(embed = embed3)
                        try:
                            msg3 = await self.bot.wait_for("message", check=pred, timeout = 30.0)
                        except asyncio.TimeoutError:
                            embed1 = discord.Embed(
                                description = 'Erreur : temps écoulé veuillez recommencer',
                                color =  15977347
                                )
                            embed1.set_footer(text='PCSI Bot by @Malo Tiriau')
                            await ctx.channel.purge(limit = 6, check = is_good)
                            await ctx.send(embed = embed1)
                            await asyncio.sleep(10)
                            await ctx.channel.purge(limit = 1, check = is_good)
                        else :
                            try :
                                l3 = os.listdir(f"./cogs/DOC/{msg.content}/{msg2.content}/{msg3.content}")
                            except Exception as e:
                                await ctx.channel.purge(limit = 7, check = is_good)
                                embedE = discord.Embed(
                                    description = 'Erreur : entrée incorrect veuillez recommencer',
                                    color =  15977347
                                )
                                embedE.set_footer(text='PCSI Bot by @Malo Tiriau')
                                await ctx.send(embed = embedE)
                                await asyncio.sleep(10)
                                await ctx.channel.purge(limit = 1, check = is_good)
                            else :
                                for i in range(len(l3)) :
                                    await ctx.send(file=discord.File(f'./cogs/DOC/{msg.content}/{msg2.content}/{msg3.content}/{l3[i]}'))
                                await asyncio.sleep(2)
                                await ctx.channel.purge(limit =7+len(l3), check = is_good)
            else :
                embedE = discord.Embed(
                    description = 'Erreur : entré incorrect veuillez recommencer',
                    color =  15977347
                )
                embedE.set_footer(text='PCSI Bot by @Malo Tiriau')
                await ctx.channel.purge(limit = 4, check = is_good)
                await ctx.send(embed = embedE)
                await asyncio.sleep(10)
                await ctx.channel.purge(limit = 1, check = is_good)











def setup(bot):
    bot.add_cog(Explorer(bot))

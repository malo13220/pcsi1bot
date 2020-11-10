import discord
import random
from discord.ext import commands


class Mat(commands.Cog, name = 'Matière'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx, arg):
        if arg == 'physique':
            embed = discord.Embed(
                title = 'Informations physique : Mr Cmielewski ',
                description = 'Support de cours : Zoom \n \n Documents : email et <#688338899277185052> \n \n Contact : physiquepcsi1@yahoo.fr \n \n Cours : Mardi (14h-16h), Mercredi (10h-12h), Jeudi(14h-15h), Vendredi(8h-10h)*, vendredi(14h-15h30) \n',
                colour = 12713971
            )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')

        elif arg == 'maths':
            embed = discord.Embed(
                title = 'Informations mathématiques : Mr Barbaza ',
                description = 'Support de cours : Discord \n \n Documents : https://pcsithiers.weebly.com/ et <#688338687745982495> \n \n Contact : l.barbaza@free.fr \n \n Cours : Lundi (10h-12h), Mercredi (8h-10h), Jeudi(8h-10h), Jeudi(15h-16h30 ou 16h30-18h), Vendredi(8h-10h)*, vendredi(15h30-17h) \n',
                colour = 12743423
            )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')

        elif arg == 'chimie':
            embed = discord.Embed(
                title = 'Informations chimie(PC) : Mme Berlot ',
                description = 'Support de cours : Discord \n \n Documents : http://www.lyc-thiers.ac-aix-marseille.fr/webphp/share/filtrer.php et <#688338934006284288> et Pronote \n \n Contact : isabelle.berlot@ac-aix-marseille.fr \n \n Cours : Mardi (9h-12h), Vendredi(10h-12h) \n',
                colour = 4784018
            )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        else :
            embed = discord.Embed(
                description = 'Erreur : matière inexistente ou pas encore dispo',
            )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)


def setup(bot):
    bot.add_cog(Mat(bot))

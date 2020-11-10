import discord
import random
import datetime
from datetime import date
from discord.ext import commands


class Fun(commands.Cog, name = 'Fun'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fun(self, ctx, arg):
        if arg == 'physique' :
            r = ["Sorter une demi feuille !!",
                "Je laisse en rouge ou en bleu pour l'année prochaine ?",
                "Problème pyschomoteur",
                "Ben pendant les vcances !",
                "...pour ceux qui sont un peu tangents pour le passage en 2eme année...",
                "Là c'est chiant c'est que du blabla",
                "J'ai reçu aucune question, j'espère que vous les avez réussi",
                "Allez plus que 3 heures",
                "Maths sup ca veut pas dire maternelle superieure",
                "Bonjooooooouuuur! <:Bonjoour:696732074673045595>",
                "Ce soir c'est le weekend",
                "Ca vous l'avez du le faire en grande section de maternelle",
                "Ce qui revient c'est que vous bossez pas encore assez",
                "Allez on se dépeche j'ai envie de faire des exemples",
                "Y'en a qui ont fait la fête hier soir",
                "Aller on fait la méthoe bébé !",
                "Rédigez bien vos TP!!",
                "C'est pas normale qu'il y est encore des gens qui ont moins de 10 en kholle",
                "En x6 pour demain sinon 0 équivalent DS !",
                "Je fais cela pour vous remonter la moyenne",
                "Je veux tous vous voir à Polytechnique dans 2 ans",
                "Vous travaillez pendant 2 ans pour le diplôme le plus important de votre vie !",
                f'Bien vu ! Plus 10 au prochain DS Mr {ctx.author.display_name}',
                'Sans alcool la fête est plus folle ! ']
            await ctx.send(f'{random.choice(r)} <:Cmielewski:690905805733494824>')
        elif arg == 'maths' or arg == 'math' or arg == 'mathématiques':
            r = [":heart: #ILOVETRIGO  ",
                "Mais vous faites quoi de vos nuits ? De la chimie ?",
                "Aller faisons un jolie dessin",
                "Les garagistes... et les chimistes...",
                "Il se voit à l'oeil nul le changement de variable",
                "Mickey <:mickey:697837043174080622> parade",
                "Mais c'est TRIVIAL !!",
                "On prend sa plus belle craie rouge et on biffe rageusement !!",
                ":brontosaure:",
                f'{ctx.author.display_name}... Quel bon vent tamène ?',
                "C'est par la factorisation que l'âme s'élève",
                "C'est du chocapic :chocapic: ça !",
                "CHANGEMENT DE BORNE  !!!",
                "Dans le joie l'algrésse et la bonne humeur !!",
                "Y'en qui ont pas encore gagné la guerre algébrique !",
                "Je laisse la démo au Lecteur Conscencieux",
                "Vous avez encore mangé mes craies ???",
                "Tatouez vous la courbe d'arctan !",
                "Le PCSI 1 MOYEN ...",
                "Geste auguste",
                "Le pauvre Cadran il a du se retourner dans sa tombe",
                "Aller on fait le sémaphores !",
                "Dans certains pays vous devriez être pendu pour cela !",
                "Principe zéro de la pédagogie : Répéter"]
            await ctx.send(f'{random.choice(r)} <:BBZ:691665304111153194>')
        elif arg == 'chimie' :
            r = ["https://imgur.com/a/lTfKmaJ"]
            await ctx.send(f'{random.choice(r)}')
        else :
            await ctx.send('Matière incorrecte ou pas encore dispo')


    @commands.command()
    async def vac(self, ctx):
        today = date.today()
        v = date(year = 2020, month = 12, day = 19)
        d = v-today
        if d.days > 0 or d.days == 0 :
            await ctx.send(f'Aller plus que {d.days} dodos avant les vacances !! <:Cmielewski:690905805733494824>')
        else :
            await ctx.send("C'est les vacances !")


    @commands.command()
    async def bonjour(self, ctx):
        await ctx.send(f'Bonjooooooouuuur {ctx.author.display_name}')

    @commands.Cog.listener()
    async def  on_message(self, message):
        l = ["quoi","quoi?","quoi ?","quoi??","quoi ??","quoi.","quoi...","quoi$","quoi*","quoi  ??","quoi !","quoi!","Quoi","QUOI ?","Quoi ?", "QUOI","Quoi !"]
        for word in l :
            if message.content.endswith(word):
                await message.channel.send("feur ! <:Cmielewski:690905805733494824>")


def setup(bot):
    bot.add_cog(Fun(bot))

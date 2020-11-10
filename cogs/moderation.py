import discord
import random
import datetime
import asyncio
from datetime import date
from discord.ext import commands


class Moderation(commands.Cog, name = 'Modération'):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clearall(self, ctx):
        await ctx.channel.purge(limit = None, check=lambda msg : not msg.pinned)
        embed = discord.Embed(
            description = 'Messages suprimés'
        )
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)
        await asyncio.sleep(2)
        await ctx.channel.purge(limit = 1, check=lambda msg : not msg.pinned)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, arg : int):
        await ctx.channel.purge(limit=arg+1, check=lambda msg: not msg.pinned)
        embed = discord.Embed(
            description = f'{arg} Messages suprimés'
        )
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)
        await asyncio.sleep(2)
        await ctx.channel.purge(limit = 1, check=lambda msg : not msg.pinned)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if str(reaction.emoji) == "📌":
            await  	reaction.message.pin()
            await asyncio.sleep(2)
            await reaction.message.channel.purge(limit = 1, check=lambda msg : not msg.pinned)


    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if reaction.emoji == "📌":
            if not ":pushpin:" in [ reaction.emoji for reaction in  reaction.message.reactions]:
                await  	reaction.message.unpin()

    @commands.command()
    async def sondage(self, ctx):
        def pred(m):
            return m.author == ctx.author and m.channel == ctx.channel
        embed = discord.Embed(
            title = 'Nouveau sondage' ,
            description = 'Insérer le titre : ',
            color = 7070186
        )
        embed.set_author(name = '🔎Sondage')
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)

        tt = await self.bot.wait_for("message", check=pred,timeout = 30.0)
        embed = discord.Embed(
            title = 'Nouveau sondage' ,
            description = 'Insérer la question : ',
            color = 7070186
        )
        embed.set_author(name = '🔎Sondage')
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)

        q = await self.bot.wait_for("message", check=pred,timeout = 30.0)
        embed = discord.Embed(
            title = 'Nouveau sondage' ,
            description = "Rentrer le nombre d'options (max 5)",
            color = 7070186
        )
        embed.set_author(name = '🔎Sondage')
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)
        msg1 = await self.bot.wait_for("message", check=pred, timeout = 30.0)
        nb = int(msg1.content)
        opt = []
        for i in range(nb):
            embed = discord.Embed(
                title = 'Nouveau sondage' ,
                description = f'Nom option {i+1} ?',
                color = 7070186
            )
            embed.set_author(name ='🔎Sondage')
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send(embed = embed)
            msg2 = await self.bot.wait_for("message", check=pred, timeout = 30.0)
            opt.append(msg2.content)
        embed = discord.Embed(
            title = 'Nouveau sondage' ,
            description = f'Durée du sondage ? (en minutes)',
            color = 7070186
        )
        embed.set_author(name = '🔎 Sondage')
        embed.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embed)
        t = await self.bot.wait_for("message", check=pred, timeout = 30.0)
        def disp(l):
            a = ""
            for i in range(len(l)):
                a = a + "\n" + f'{i+1} : ' + l[i]
            return a
        try :
            embedf = discord.Embed(
                title = f'{tt.content}' ,
                description = f'{q.content} \n {disp(opt)} \n \n Durée du sondage :  {t.content} minutes \n \n Répondez en réaction pour voter : \n',
                color = 7070186
                )
            embedf.set_author(name ='🔎Sondage')
            embedf.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send('@everyone')
            sd = await ctx.send(embed = embedf)
            id = sd.id
        except Exception as e :
            embedE = discord.Embed(
                title = "Erreur veuillez recommencer" ,
                color = 7070186
                )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send(embed = embedE)
        else :
            embedR = discord.Embed(
                title = "Sondage créé avec succès" ,
                color = 7070186
                )
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send(embed = embedR)
            if nb == 1 :
                await sd.add_reaction('1️⃣')
            elif nb == 2 :
                await sd.add_reaction('1️⃣')
                await sd.add_reaction('2️⃣')
            elif nb == 3 :
                await sd.add_reaction('1️⃣')
                await sd.add_reaction('2️⃣')
                await sd.add_reaction('3️⃣')
            elif nb == 4 :
                await sd.add_reaction('1️⃣')
                await sd.add_reaction('2️⃣')
                await sd.add_reaction('3️⃣')
                await sd.add_reaction('4️⃣')
            elif nb == 5 :
                await sd.add_reaction('1️⃣')
                await sd.add_reaction('2️⃣')
                await sd.add_reaction('3️⃣')
                await sd.add_reaction('4️⃣')
                await sd.add_reaction('5️⃣')

            t2 = int(t.content)*60
            await asyncio.sleep(t2)
            sd2 = await ctx.fetch_message(id)
            l = []
            for rea in sd2.reactions:
                reactors = await rea.users().flatten()
                l.append(len(reactors)-1)
            totale = 0
            for i in range(len(l)):
                totale += l[i]
            def dispR(l1, l2):
                a = ""
                for i in range(nb):
                    a  = a + "\n" + f'{i+1} : ' + f'  {l2[i]} ' +'votes' + f' : {(l[i])/(totale)*100}' + "%"
                return a
            def optg(l1, l2):
                a = 0
                b = l2[a]
                for i in range(nb):
                    if int(l2[i]) > b :
                        a = i
                        b = l2[a]
                return l1[a]

            embedR = discord.Embed(
                title = f'{tt.content}' ,
                description = f'{q.content} \n {dispR(opt, l)} \n \n Nombre totale de votant : {totale} \n \n :triangular_flag_on_post:  Option gagnante :  {optg(opt, l)} ',
                color = 7070186
                )
            embedR.set_author(name = '🔎 Sondage - Résultats')
            embedR.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send('@everyone')
            await ctx.send(embed = embedR)

#FONCTIONALITE désactivé
'''
    @commands.command()
    async def appel(self, ctx):
        embedI = discord.Embed(
            title = 'Nouvel appel :',
            description = ' Pour qui  ?  \n \n  1. Tous les élèves  \n 2. Pour les élèves PC \n 3. Pours les élèves PSI \n 4. Pours les élèves du groupe 1 \n 5. Pour les élèves du groupe 2 \n \n Envoyer 1,2,3,4 ou 5 pour choisir ',
            color = 8930125

            )
        embedI.set_author(name = ' 📑 Appel :')
        embedI.set_footer(text='PCSI Bot by @Malo Tiriau')
        await ctx.send(embed = embedI)
        def pred(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await self.bot.wait_for("message", check=pred, timeout = 30.0)
        except asyncio.TimeoutError:
            embed1 = discord.Embed(
                description = 'Erreur : temps écoulé veuillez recommencer',
                color =  8930125
            )
            embed1.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send(embed = embed1)
        else :
            if msg.content == '1' :
                etudiantrole = ctx.guild.get_role(688085010066309153)
            elif msg.content == '2':
                etudiantrole = ctx.guild.get_role(688084387207708800)
            elif msg.content == '3':
                etudiantrole = ctx.guild.get_role(688084538781597722)
            elif msg.content == '4':
                etudiantrole = ctx.guild.get_role(688084571702558737)
            elif msg.content == '5':
                etudiantrole = ctx.guild.get_role(688084722991366382)
            else :
                embedE = discord.Embed(
                description = 'Erreur : entrée invalide',
                color =  8930125
                )
                embedE.set_footer(text='PCSI Bot by @Malo Tiriau')
                await ctx.send(embed = embedE)
            date = datetime.datetime.now()
            embed = discord.Embed(
                title = 'Nouvel appel :',
                description = f' Le {date.day}/{date.month}/{date.year} à {date.hour}H{date.minute} \n \n  Vous avez 3 minutes pour  signaler votre présence en ajoutant la réaction :ok: ',
                color = 8930125

                )
            embed.set_author(name = ' 📑 Appel :')
            embed.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send(etudiantrole.mention)
            ap = await ctx.send(embed = embed)
            a = ap.id
            await ap.add_reaction('🆗')

            await asyncio.sleep(180)
            channel = ctx.channel
            ap2 = await ctx.channel.fetch_message(a)
            liste = []
            rea = ap2.reactions[0]
            reactors = await rea.users().flatten()
            for member in reactors:
                liste.append(member.display_name)
            nb = len(liste) -1
            def disp1(l):
                a = ""
                for i in range(1, len(l)):
                    a = a + "\n - " + l[i]
                return a
            def disp2(l):
                a = ""
                for i in range(len(l)):
                    a = a + "\n - " + l[i]
                return a
            etudiantsbrut = etudiantrole.members
            etudiants = []
            for i in range(len(etudiantsbrut)):
                etudiants.append(etudiantsbrut[i].display_name)
            ab = []
            for i in range(len(etudiants)):
                if etudiants[i] not in liste :
                    ab.append(etudiants[i])
            embedR = discord.Embed(
                title = "Résultat de l'appel :",
                description = f'Nombre de présents : {nb}/{len(etudiants)} \n \n :small_blue_diamond:    Liste des présents :  {disp1(liste)} \n \n :small_orange_diamond:  Liste des absents : {disp2(ab)}',
                color = 8930125

                )
            embedR.set_author(name = ' 📑 Appel :')
            embedR.set_footer(text='PCSI Bot by @Malo Tiriau')
            await ctx.send(embed = embedR)
'''







def setup(bot):
    bot.add_cog(Moderation(bot))

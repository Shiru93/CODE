# On peut accéder aux variables d'environnement avec le module os (pour voir comment récupérer une variable d'environnement, aller à la dernière ligne)
from cProfile import label
import os
from typing_extensions import Self

import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio

# Pour créer des commandes plus facilement
# On créer une instance d'un bot (commands.Bots) qu'on met dans une variable (ici bot)
# On lui donne un prefix grâce à command_prefix = " "
bot = commands.Bot(command_prefix = "$")

# Retirer la commande help (qui est déjà intégrée de base) afin de pouvoir personnaliser sa propre commande help
bot.remove_command('help')

# Pour récupérer une variable d'environnement avec le module os, on va utiliser la fonction os.getenv()

# Comme notre fichier se nomme .env on a pas besoin de mettre quoique ce soit en paramètre
# Ca va récupérer tout ce qui est à l'intérieur du fichier (ici .env) et les loader dans les variables d'environnement (voir ligne 1)
load_dotenv()

# Si notre fichier se nommait autrement que par .env (par exemple config) alors on ecrit la fonction de manière suivante : load_dotenv(dotenv_path = "config")

# Créer une instance qui va nous permmettre de créer une instence avec toutes les permissions par défaut
default_intents = discord.Intents.default()

# Activer les instances qui sont relatives aux membres
default_intents.members = True


'''-------------------------------------------------- LE BOT EST PRET --------------------------------------------------'''
# Nous permet d'utiliser les fonctions déjà établies pour l'utilisation d'un bot discord
@bot.event

# Permet de nous assurer que le bot est prêt
async def on_ready():
    print("Le bot est prêt")


'''-------------------------------------------------- HELP --------------------------------------------------'''
# La commande help
@bot.command()
async def help(ctx):
    await ctx.send("Veuillez vérifier vos messages privés")

    # Envoie la liste des commandes et leurs fonctions par message privé
    embed = discord.Embed(colour=discord.Colour.blue())
    embed.set_author(name='Liste des commandes')

    #Commandes User
    embed.add_field(name="**$coucou**", value="Salutations", inline=False)
    embed.add_field(name="**$python**", value="Aide Python", inline=False)
    embed.add_field(name="**$del <nombre>**", value="Supprimes des messages", inline=False)
    embed.add_field(name="**$dire**", value="Le bot va répèter le texte que t'as tapé", inline=False)
    embed.add_field(name="**$jouer**", value="Démarrer un jeu (pour de faux hein)", inline=False)
    embed.add_field(name="**$InfoServeur**", value="Afficher les informations du serveur", inline=False)
    embed.add_field(name="----------------------------------------------", value="---------------------------------------------", inline=False)

    #Commandes Admin 
    for role in ctx.message.author.roles:
        if role.name == 'The King':
            embed.add_field(name="**COMMANDES ADMINS**", value="commandes admins", inline=False)
            embed.add_field(name="**Test**", value="test", inline=True)
            embed.add_field(name="**Test**", value="test", inline=True)
            embed.add_field(name="**Test**", value="test", inline=True)

    await ctx.author.send(embed=embed)


'''-------------------------------------------------- NOUVEAUX MEMBRES --------------------------------------------------'''
# Réagir à l'arrivé d'un nouveau membre
@bot.event
async def on_member_join(member):
    # Récupérer le salon principal où l'on affichera les notifications
    # On indique le type de la variable
    general_channel: discord.TextChannel = bot.get_channel(978233174767321101)

    # Ecrire le message tout en insérant à l'intérieur de cette chaîne de caractère le nom d'affichage de l'utilisateur qui vient de rejoindre le serveur
    # display_name est le nom d'affichage de l'utilisateur
    await general_channel.send(content = f"Bienvenue sur le serveur {member.display_name} !")


'''-------------------------------------------------- PING ET PONG --------------------------------------------------'''
@bot.event
async def on_message(message):
    # Permet d'afficher dans le terminal le message que nous avons envoyés sur le serveur
    await bot.process_commands(message)

    # Vérifier le contenu du message pour s'assurer que le message contient bien le mot ping
    # La méthode lower() permet de vérifier peut importe si j'ai mis une majuscule ou minuscule au mot ping
    if message.content.lower() == "ping":
        # Savoir dans quel salon nous sommes
        # delete_after = 5 permet de supprimer automatiquement le message après 5 secondes
        await message.channel.send("pong", delete_after = 5)


'''-------------------------------------------------- SALUTATIONS --------------------------------------------------'''
@bot.command()
async def coucou(ctx):
    await ctx.send("Toutes mes salutations mon roi")
    await ctx.send("Comment allez-vous ?")
    @bot.event
    async def on_message(message):
        # Permet d'afficher dans le terminal le message que nous avons envoyés sur le serveur
        await bot.process_commands(message)

        # Vérifier le contenu du message pour s'assurer que le message contient bien le mot ping
        # La méthode lower() permet de vérifier peut importe si j'ai mis une majuscule ou minuscule au mot ping
        if message.content.lower() == "je vais bien merci":
            # Savoir dans quel salon nous sommes
            # delete_after = 5 permet de supprimer automatiquement le message après 5 secondes
            await message.channel.send("Vous m'en voyez ravis")

        elif message.content.lower() == "je vais mal":
            await message.channel.send("Puis-je savoir pourquoi ?")
            @bot.event
            async def on_message(message):
                await bot.process_commands(message)
                if message.content.lower() == "non":
                    await message.channel.send("Je ne peux dans ce cas là, rien faire pour vous")
                elif message.content.lower() == "j'ai du mal avec python":
                    await message.channel.send("vous trouverez toute l'aide dont vous avec besoin en tapant la commande `$python`, si vous voulez plus d'information sur les commandes, veuillez taper la commande `$help`")



'''-------------------------------------------------- SUPPRIMER LES MESSAGES --------------------------------------------------'''
# On utilise le décorateur command et on va donner un nom à cette commande (ici del)
# Attention, le nom ici est ce qu'on va utiliser à l'intérieur du serveur pour appeler la commande
@bot.command(name = 'del')

# On créer une fonction qu'on décidera d'appeler delete (ça peut être n'importe quoi)
# On met comme paramètre le contexte qu'on appelera ctx (ici aussi ça peut être n'importe quoi mais on l'appel ainsi par convention)
# Grâce à ctx on pourra récupérer des informations comme par exemple le salon où a été posté la commande
# On créer une 2e paramètre dont on précisera le type (ici int). Le type nous permettra de convertir automatiquement le paramètre qui va être envoyé après la commande
async def delete(ctx, number_of_messages: int):

    # Je récupère tous les messages (avec le paramètre number_of_messages ici) et je les supprime
    messages = await ctx.channel.history(limit = number_of_messages + 1).flatten()

    for each_message in messages:
        await each_message.delete()


'''-------------------------------------------------- A QUOI ON VEUT JOUER --------------------------------------------------'''
@bot.command()
async def jouer(ctx):
    await ctx.send("A quoi voulez-vous jouer ?")

    # Vérification pour savoir si c'est bien le joueur qui a répondu à sa propre commande dans le même channel
    def check_message(message):
        return message.author == ctx.message.author and ctx.message.channel == message.channel

    # Vérifier s'il nous a bien envoyé le message
    try:
        # Le bot attend notre message avec un délait de 10 secondes
        commande = await bot.wait_for("message", timeout = 10, check = check_message)
    # Si on a passé les 10 secondes de timeout
    except:
        await ctx.send("Vous avez été trop lent, veuillez retaper la commande")
        return

    message = await ctx.send(f"Nous préparons votre jeu ({commande.content}). Cochez la réaction ✅ pour confirmer ou la réaction ❌ pour refuser")

    # Ajouter les réactions (message est ce que l'on a défini au dessus)
    await message.add_reaction("✅")
    await message.add_reaction("❌")

    # Vérifier que c'est bien l'auteur de la commande qui coche la réaction
    def check_emoji(reaction, user):
        return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoj == "❌"))

    try:
        reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = check_emoji)
        if reaction.emoji == "✅":
            await ctx.send("Votre jeu va démarrer !")
        else:
            await ctx.send("Votre jeu ne démarrera pas !")

    except:
        await ctx.send("Votre jeu ne démarrera pas !")


'''-------------------------------------------------- INFORMATIONS DU SERVEUR --------------------------------------------------'''
# Afficher les informations du serveur
@bot.command()
async def InfoServeur(ctx):
    serveur = ctx.guild
    nombreDeChainesTexte = len(serveur.text_channels)
    nombreDeChainesVocale = len(serveur.voice_channels)
    Description_du_serveur = serveur.description
    Nombre_de_personnes = serveur.member_count
    Nom_du_serveur = serveur.name
    message = f"Le serveur **{Nom_du_serveur}** contient *{Nombre_de_personnes}* personnes ! \nLa description du serveur est {Description_du_serveur}. \nCe serveur possède {nombreDeChainesTexte} salons écrit et {nombreDeChainesVocale} salon vocaux."
    await ctx.send(message)


'''-------------------------------------------------- COPIEUR --------------------------------------------------'''
# Le bot répète (à l'écrit) se qu'on a écrit
@bot.command()
async def dire(ctx, *message):
    await ctx.send(" ".join(message))


'''-------------------------------------------------- AIDE PYTHON --------------------------------------------------'''
@bot.command()
async def python(ctx):
    embed=discord.Embed(title="Aide Python", description="Liens aide Python", color=0xf100f5)
    embed.set_author(name="Aide")
    embed.add_field(name="$pyglobal", value="Python (Globale)", inline=True)
    embed.add_field(name="$pymodules", value="Python (Modules)", inline=True)
    embed.add_field(name="$pyindex", value="Python (Index)", inline=True)
    embed.add_field(name="$pyglossaire", value="Python (Glossaire)", inline=True)
    embed.add_field(name="$pycours", value="Python (playlist YouTube)", inline=True)
    embed.add_field(name="$pyvariables", value="Python (Variables)", inline=True)
    embed.add_field(name="$pyconditions", value="Python (Les Conditions)", inline=True)
    embed.add_field(name="$pylistes", value="Python (Listes)", inline=True)
    embed.add_field(name="$pyboucles", value="Python (Boucles)", inline=True)
    embed.add_field(name="$pyfonctions", value="Python (Fonctions)", inline=True)
    embed.add_field(name="$pyobjets", value="Python (Les Objets)", inline=True)
    embed.add_field(name="$pyheritage", value="Python (L'Héritage)", inline=True)
    embed.add_field(name="$pytkinter", value="Python (Interface Graphiquee)", inline=True)
    embed.add_field(name="$pyfichiers", value="Python (Les Fichiers)", inline=True)
    embed.add_field(name="$pydictionnaires", value="Python (Dictionnaires)", inline=True)
    embed.set_footer(text="Veuillez taper les commandes afin de bénéficier de l'aide fournit via les liens")
    await ctx.send(embed=embed)

@bot.command()
async def pyglobal(ctx):
    await ctx.send("Vous trouvez toute l'aide en Python dans sa globalité via le lien suivant : https://docs.python.org/3/")

@bot.command()
async def pymodules(ctx):
    await ctx.send("Vous trouvez toute l'aide que avez besoin pour apprendre et comprendre les différents modules en Python via le lien suivant : https://docs.python.org/3/py-modindex.html")

@bot.command()
async def pyindex(ctx):
    await ctx.send("Vous trouverez l'index de Python via le lien suivant : https://docs.python.org/3/genindex.html")
    
@bot.command()
async def pyglossaire(ctx):
    await ctx.send("Vous trouverez le glossaire via le lien suivant : https://docs.python.org/3/glossary.html")

@bot.command()
async def pycours(ctx):
    await ctx.send("Vous trouverez ci-joint une playlist YouTube contenant toute l'aide que vous avez besoin en Python : https://www.youtube.com/playlist?list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR")

@bot.command()
async def pyvariables(ctx):
    await ctx.send("Vous avez du mal avec les variables ? Veuillez consulter le lien suivant : https://www.youtube.com/watch?v=nvyX8JfoOWY&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=2")

@bot.command()
async def pyconditions(ctx):
    await ctx.send("Vous voulez apprendre les conditions ? Veuillez alors consulter le lien suivant : https://www.youtube.com/watch?v=_AgUOsvMt8s&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=3")

@bot.command()
async def pylistes(ctx):
    await ctx.send("Vous souhaitez vous apprendre l'utilisation des listes ? Voici l'aide dont vous avez besoin : https://www.youtube.com/watch?v=kyxF5eH3Kic&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=4")

@bot.command()
async def pyboucles(ctx):
    await ctx.send("Les boucles sont difficiles ? Pas de soucis, voici de l'aide : https://www.youtube.com/watch?v=BrknhzrHm8w&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=5")

@bot.command()
async def pyfonctions(ctx):
    await ctx.send("Petit indice, les fonctions vous faciliteront la vie : https://www.youtube.com/watch?v=sgJt64iTOYM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=6")

@bot.command()
async def pyobjets(ctx):
    await ctx.send("Qu'est-ce qu'un objet en Python ? https://www.youtube.com/watch?v=dfUM_9xibf8&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=7")

@bot.command()
async def pyheritage(ctx):
    await ctx.send("L'héritage ? https://www.youtube.com/watch?v=fW4818AS88I&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=8")

@bot.command()
async def pytkinter(ctx):
    await ctx.send("Vous souhaitez apprendre à utiliser une  interface graphique en Python ? Ne vous inquiétez pas, j'ai la solution pour : https://www.youtube.com/watch?v=N4M4W7JPOL4&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=9")

@bot.command()
async def pyfichiers(ctx):
    await ctx.send("https://www.youtube.com/watch?v=jOHpZg8k668&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=10")

@bot.command()
async def pydictionnaires(ctx):
    await ctx.send("Quelle est la différence entre un dictionnaire et une liste ? La voici : https://www.youtube.com/watch?v=0pgYBjW1OVM&list=PLMS9Cy4Enq5JmIZtKE5OHJCI3jZfpASbR&index=11")
            

'''-------------------------------------------------- TOKEN --------------------------------------------------'''
# Pour récupérer une variable d'environnement avec le module os, on va utiliser la fonction os.getenv() qui aura comme paramètre le nom de la variable contenant le TOKEN (se trouve dans le fichier .env)
bot.run(os.getenv("TOKEN"))
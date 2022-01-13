import os
import configparser
from configparser import ConfigParser
import discord
from discord.enums import RelationshipType
from discord.ext import commands
import aiocron

intents = discord.Intents.default()
intents.members = True
intents.presences = True

###### CONFIG

tocken =                # TOCKEN DEL BOT
idguid =                # ID DEL SERVIDOR
rolastro =              # ID DEL ROL
juego = "ASTRONEER"     # NOMBRE DEL JUEGO

###### FIN DEL CONFIG

bot = commands.Bot(command_prefix='/', description="Bot creado para añadir role de astroneer, si esta jugando", intents=intents)


@bot.event
async def on_ready():
    print('El bot de se esta ejecutando')

@aiocron.crontab('*/1 * * * *')
async def cornjob3():
    guild = bot.get_guild(idguid)
    astroneer = guild.get_role(rolastro)
    for X in range(len(guild.members)):
        miembro = guild.members[X]
        try:
            if miembro.activities[0].name == juego:
                await miembro.add_roles(astroneer)
            else:
                await miembro.remove_roles(astroneer)
        except:
            pass

@bot.command()
async def juego(ctx, userdiscord: discord.Member = None):
    if ctx.author.guild_permissions.manage_roles is True:
        if userdiscord is None:
            ctx.send("No has puesto el usuario")
            return
        miembro = bot.get_member(userdiscord.id)
        await ctx.send('Esta jugando a "{}"'format(userdiscord.activities[0].name))
    else:
        return
    
    

bot.run(tocken)

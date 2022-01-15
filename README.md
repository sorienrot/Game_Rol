# Game_Rol
 Añade un rol cuando juegas al ASTRONEER, o al juego que elijas

```python
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

@aiocron.crontab('*/1 * * * *')  # Revisa cada minuto el estado
async def cornjob3():
    guild = bot.get_guild(idguid)
    astroneer = guild.get_role(rolastro)
    for X in range(len(guild.members)):
        miembro = guild.members[X]
        if len(miembro.activities) == 0:
            if astroneer in miembro.roles:
                await miembro.remove_roles(astroneer)
        else:
            try:
                if miembro.activities[0].name == juego:
                    await miembro.add_roles(astroneer)
                else:
                    if astroneer in miembro.roles:
                        await miembro.remove_roles(astroneer)
            except:
                if astroneer in miembro.roles:
                    await miembro.remove_roles(astroneer)

@bot.command()  # Obtener el nombre del juego, preguntando por un usuario
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
```

Obtener el tocken

![image](https://user-images.githubusercontent.com/10135600/149390451-9108d5cb-ed8e-4eb5-a195-0ac23361c602.png)

Obtener id del servidor

![image](https://user-images.githubusercontent.com/10135600/149390872-305d5c4d-7c17-4012-86dc-d18929b0466d.png)

Obtener id del Rol

![image](https://user-images.githubusercontent.com/10135600/149391331-89e0c470-829b-489d-8a60-0c2c75dbc7c9.png)





import discord
from discord.ext.commands import Bot

butter = Bot(command_prefix="b^")

Bot.change_status(game="Prefix: b^", idle=False)

@butter.event
async def on_read():
    print("Client logged in")

@butter.command()
async def hello(*args):
    return await butter.say("Hello, world!")

#butter.run("MzIxNDA4Mzk4NjY5MjUwNTYy.DBgF4Q.1h6Z7TsKojZstNqQfKrjWcL")

@butter.command()
async def hlep(*args):
    send_message(user, content='''Hello there! I am Butterscotch, a Discord bot made in Python by Eve6262. The following are my commands:
Important:
-help : What you put in the chat to generate this message.
-info (@user) : Gets the info of a user. typed as: b^info @Eve6262
-invite : Procures the invite link for you to use. Have fun inviting me places!
-whitelist : Shows the certain users who can't use me, in case of abuse. No one gets to abuse me!
    -addwhitelist (@user) : Adds the @user to my whitelist. #StopButterscotchAbuse!
    -removewhitelist (@user) : Removes the @user from my whitelist. Hope they don't start again. (if they aren't there, I'll tell you.)


Magic:
-fireblast (@user) : Aims one of my beautiful fireblasts at the targeted user.
-icewall (optional @user) : Creates an ice wall of my own creation. Protects against one attack. If no user, used on yourself.
-thunderstrike : It's thunder, so it just kind of scares everyone. Not actually lightning.
-candy (@user) : Gives said user one of my famous Butterscotch candies! They'll love it.
-sour (@user) : Gives said user one of my...failed attempts at candy. Hey, no one's perfect!
My prefix is b^, so make sure to put b^ before each command you call me!''', tts=False, embed=None)
    
@butter.command()
async def fireblast(user, *args):
    butter.say("Hya! %s was hit with my fireball! Take that! Hehe." % (user))

@butter.command()
async def icewall(user, *args):
    if user != None:
        butter.say("And...Done! %s was covered in an ice wall! So nice of you to do that." % (user))
    else:
        butter.say("And...Done! You're protected by an ice wall! A bit chilly.")

@butter.command()
async def thunderstrike(*args):
    butter.say ("Everyone got kinda spooked by the thunderstrike. Except you and me, because we expected it. *shake*")

@butter.command()
async def candy(user, *args):
    butter.say ("And now, %s gets to taste my candy! They were delighted, of course. Hehe." % (user))

@butter.command()
async def sour(user, *args):
    butter.say ("Since I have no use for this failure, %s gets to taste it! Blech. Surprised you didn't throw up." % (user))


from discord import Embed, Colour
from datetime import datetime
from dotenv import load_dotenv
import os
import gettext
load_dotenv()

#setup gettext
appname = 'zomboid_bot'
localedir = os.getenv("LANGUAGE_DIR")
language= os.getenv("BOT_LANGUAGE")
bot_translate = gettext.translation(appname, localedir, fallback=False, languages=[language])
bot_translate.install(names=['ngettext'])

# Message formatting and coloring for public-facing logs
#def __embedify(timestamp: datetime, colour: Colour, message: str) -> Embed:
#   return Embed(timestamp=timestamp, colour=colour, description=message)

def __embedify(ShowTimestamp,timestamp: datetime, colour: Colour, message: str) -> Embed:
    if ShowTimestamp == "yes":
        return Embed(timestamp=timestamp, colour=colour, description=message)
                
    else:
        return Embed(timestamp=None, colour=colour, description=message)
 
'''
Chat Message
'''

def chat_message(timestamp: datetime, user: str, avatar, message: str) -> Embed:
    """Stock blurple embed to relay a user's message"""
    #embed creation
    if os.getenv("SHOW_TIMESTAMP") == "yes":
        embed=Embed(timestamp=timestamp, description=message, color=Colour.og_blurple())
                
    else:
        embed=Embed(timestamp=None, description=message, color=Colour.og_blurple())
    #embed additionnal field
    embed.set_author(name=user, icon_url=avatar)

    return embed

'''
Perk
'''
def perk(timestamp: datetime, user: str, aka: str, perk: str, level: int) -> Embed:
    """Blue embed to indicate a user's level-up"""
    message = _("PERK_ICON") + f"  ** {user}** {aka} " + _("PERK_REACHED") + f"  {perk}  " + _("PERK_LEVEL") + f"  {level}  "
    return __embedify(os.getenv("SHOW_TIMESTAMP"), timestamp, Colour.blue(), message)
    
'''
Join
'''
def join(timestamp: datetime, user: str, aka: str) -> Embed:
    """Green embed to indicate a new user/character joining"""
    message = _("JOIN_MESSAGE_ICON") + _("JOIN_MESSAGE_START") + f" **{user}** " + _("JOIN_MESSAGE_END")
    return __embedify(os.getenv("SHOW_TIMESTAMP"), timestamp, Colour.green(), message)
    
'''
Resume
'''
def resume(timestamp: datetime, user: str, aka: str, hours: int) -> Embed:
    """Green embed to indicate a user/character resuming"""
    message = _("ARRIVAL_MESSAGE_ICON") + _("ARRIVAL_MESSAGE_START") + f" **{user}** {aka} " + _("ARRIVAL_MESSAGE_MIDDLE") + f" {hours} " + _("ARRIVAL_MESSAGE_END")
    return __embedify(os.getenv("SHOW_TIMESTAMP"), timestamp, Colour.green(), message)
    
'''
Leave
'''
def leave(timestamp: datetime, user: str, avatar) -> Embed:
    """Red embed to indicate a user disconnecting"""
    message = _("LEFT_MESSAGE")
    #embed creation
    if os.getenv("SHOW_TIMESTAMP") == "yes":
        embed=Embed(timestamp=timestamp, description=message, color=Colour.red())
                
    else:
        embed=Embed(timestamp=None, description=message, color=Colour.red())
    #embed additionnal field
    embed.set_author(name=user, icon_url=avatar)

    return embed

    
'''
Death 
'''
def death(timestamp: datetime, user: str, aka: str, hours: int) -> Embed:
    """Dark embed to indicate a user's/character's death"""
    message = _("DIED_ICON") + f" **{user}** {aka} " + _("DIED_MESSAGE") +  f" {hours} " +_("DIED_MESSAGE_END")
    return __embedify(os.getenv("SHOW_TIMESTAMP"), timestamp, Colour.dark_red(), message)
    
'''
Skill Recovery Journal
'''
def srj(timestamp: datetime, user: str, aka: str, hours: int) -> Embed:
    """Gold embed to indicate a user reading is skill journal"""
    message = _("SRJ_ICON") + _("SRJ_MESSAGE_START") + f" **{user}** {aka} " + _("SRJ_MESSAGE_END")
    return __embedify(os.getenv("SHOW_TIMESTAMP"), timestamp, Colour.gold(), message)

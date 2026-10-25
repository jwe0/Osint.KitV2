import os
from core.modules.logging import *
from pystyle import Colors, Colorate

def ascii_art():
    art = """   ____       _       __    __ __ _ __ 
  / __ \\_____(_)___  / /_  / //_/(_) /_
 / / / / ___/ / __ \\/ __/ / ,<  / / __/
/ /_/ (__  ) / / / / /__ / /| |/ / /_  
\\____/____/_/_/ /_/\\__(_)_/ |_/_/\\__/ v2

❱ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ /ᴊᴡᴇ0   
                                       """
    print(Colorate.Color(Colors.pink, art))

def clear_screen():
    os.system("clear")

def flatten_json(data):
    keys = list(data.keys())
    vals = list(data.values())

    key_pad =  max([len(key) for key in keys])

    for i in range(len(keys)):
        info(f"{keys[i]} {" " * (key_pad - len(keys[i]))} | {vals[i]}")
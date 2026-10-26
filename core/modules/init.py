import os, json
from core.modules.logging import *
from pystyle import Colors, Colorate

def ascii_art():
    art = """   ____       _       __    __ __ _ __ 
  / __ \\_____(_)___  / /_  / //_/(_) /_
 / / / / ___/ / __ \\/ __/ / ,<  / / __/
/ /_/ (__  ) / / / / /__ / /| |/ / /_  
\\____/____/_/_/ /_/\\__(_)_/ |_/_/\\__/ v2
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

def load_config():
    file = "core/dependencies/config.json"
    if not os.path.exists(file):
        clear_screen()
        ascii_art()
        error("Config does not exist")
        print()
        results = {}
        args = {
            "discord_token" : {
                "name" : "Discord Token",
                "required" : True,
                "default" : None
            }
        }

        for arg in args:
            arg_info = args[arg]

            name     = arg_info["name"]
            required = arg_info["required"]
            default  = arg_info["default"]
            user_input = inpt(name)

            while not user_input and required:
                error("Required value")
                user_input = inpt(name)

            if not user_input:
                user_input = default

            results[arg] = user_input

        with open(file, "w") as f:
            f.write(json.dumps(results, indent=4))

    config = json.load(open(file))

    return config
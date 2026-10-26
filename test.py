from core.modules.logging import *

def flatten_json(data):

    for section in data:
        information = data[section]
        info(section)

        keys = list(information.keys())
        vals = list(information.values())

        key_pad = max([len(key) for key in keys]) + 2

        for i in range(len(keys)):
            info(f"  {keys[i]}{" " * (key_pad - len(keys[i]))} |  {vals[i]}")




    # keys = list(data.keys())
    # vals = list(data.values())

    # key_pad =  max([len(key) for key in keys])

    # for i in range(len(keys)):
    #     print(f"{keys[i]} {" " * (key_pad - len(keys[i]))} | {vals[i]}")

x = {
    "info": {
        "[U] id": "1330293793865465948",
        "[U] username": "fachixy_",
        "[U] global_name": "Cloud_Roxi",
        "[U] avatar": "f6e510f92fef328a576891f82fdce861",
        "[U] avatar_decoration_data": None,
        "[U] collectibles": None,
        "[U] discriminator": "0",
        "[U] display_name_styles": None,
        "[U] public_flags": 0,
        "[U] flags": 0,
        "[U] banner": None,
        "[U] banner_color": "#000000",
        "[U] accent_color": 0
    },
    "connected": {
        "[S] spotify": "c.ddmn"
    }
}

flatten_json(x)
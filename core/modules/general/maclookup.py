import json
# https://github.com/Tanathy/OUI-lookup <--- Oui source
# 38:c9:86:41:53:41

def maclookup(self, args):
    mac = args.get("mac", "")
    ouis = json.load(open("core/dependencies/oui.json"))
    mac = mac.replace("-", "").replace(":", "").upper()[:6]
    oui_info = ouis["ouis"].get(mac)
    if not oui_info:
        return {
            "status" : "error", 
            "message" : "MAC address not found"
        }
    country = ouis["countries"][oui_info["cc"]]
    organization = ouis["organizations"][oui_info["org"]]
    data = {
        "mac" : mac,
        "oui" : oui_info,
        "country" : country,
        "organization" : organization
    }
    return {
        "status" : "success", 
        "data" : {
            "info" : data
        }
    }

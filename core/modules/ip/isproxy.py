import json

def isproxy(self, args):
    ipaddress = args.get("ip", "")
    if not ipaddress:
        return {
            "message" : "error", 
            "info" : "You did not supply IP information"
        }
    
    dump = json.load(open("core/dependencies/vpnlist.json"))

    for provider in dump:
        ips = dump[provider]
        if ipaddress in ips:
            data = {
                "ip" : ipaddress,
                "provider" : provider
            }
            return {
                "message" : "success", 
                "info" : data
            }
    return {
        "message" : "error", 
        "info" : "No provider found"
    }
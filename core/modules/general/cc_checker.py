import json

def search(dump, bin):
    val = dump.get(bin)
    return val

def cc_checker(self, args):
    card = args.get("card", "")
    
    dump = json.load(open("core/dependencies/bin_info.json"))

    val = search(dump, card[0:6])
    if val:
        return {
            "status" : "success", 
            "data" : {
                "info" : val
            }
        }
    else:
        val = search(dump, card[0:8])
        if val:
            return {
                "status" : "success", 
                "data" : {
                    "info" : val
                }
            }
    return {
        "status" : "error", 
        "message" : f"No valid information found for {card}"
    }
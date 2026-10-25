import json

def search(dump, bin):
    val = dump.get(bin)
    return val

def cc_checker(self, args):
    card = args.get("card", "")
    if not card:
        return {
            "message" : "error", 
            "info" : "You did not supply card information"
        }
    
    dump = json.load(open("core/dependencies/bin_info.json"))

    val = search(dump, card[0:6])
    if val:
        return {
            "message" : "success", 
            "info" : val
        }
    else:
        val = search(dump, card[0:8])
        if val:
            return {
                "message" : "success", 
                "info" : val
            }
    return {
        "message" : "error", 
        "info" : f"No valid information found for {card}"
    }
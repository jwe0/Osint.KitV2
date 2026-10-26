def webhook_lookup(self, args):

    response = self.session.get(args.get("webhook"))

    if response.status_code != 200:
        return {
            "status" : "error",
            "message" : f"API error occured {response.status_code}"
        }
    
    return {
        "status" : "success",
        "data" : {
            "info" : response.json()
        }
    }
def webhook_lookup(self, args):

    response = self.session.get(args.get("webhook"))

    if response.status_code != 200:
        return {
            "message" : "error",
            "info" : f"API error occured {response.status_code}"
        }
    
    return {
        "message" : "success",
        "info" : response.json()
    }
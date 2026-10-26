def user_id_lookup(self, args):
    api = "https://discord.com/api/v9/users/{}/profile".format(args.get("user_id"))

    headers = {
        "Authorization" : self.config.get("discord_token"),
        "Content-Type" : "application/json"
    }

    response = self.session.get(
        api,
        headers=headers
    )

    if response.status_code == 200:
        response_data = response.json()

        resultsU = {}
        resultsC = {}
        key_blacklist = [
            "bio"
        ]

        user_info = response_data["user"]

        for key, value in user_info.items():
            if type(value) != dict and key not in key_blacklist:
                resultsU[f"[U] {key}"] = value

        connected_accounts = response_data["connected_accounts"]

        for account in connected_accounts:
            resultsC[f"[S] {account.get("type")}"] = account["name"]

        return {
            "status" : "success",
            "data" : {
                "info" : resultsU,
                "connected" : resultsC
            }
        }

    return {
        "status" : "error",
        "message" : f"API error {response.status_code}"
    }


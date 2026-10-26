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

        results = {}

        key_blacklist = [
            "bio"
        ]

        user_info = response_data["user"]

        for key, value in user_info.items():
            if type(value) != dict and key not in key_blacklist:
                results[f"[U] {key}"] = value

        connected_accounts = response_data["connected_accounts"]

        for account in connected_accounts:
            results[f"[S] {account.get("type")}"] = account["name"]

        return {
            "message" : "success",
            "info" : results
        }

    return {
        "message" : "error",
        "info" : f"API error {response.status_code}"
    }


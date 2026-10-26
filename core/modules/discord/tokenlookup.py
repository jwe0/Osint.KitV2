def token_lookup(self, args):
    api = "https://discord.com/api/v9/users/@me"
    headers = {
        "Authorization" : args["token"],
        "Content-Type" : "application/json"
    }

    response = self.session.get(
        api,
        headers=headers
    )

    if response.status_code != 200:
        return {
            "status" : "error",
            "message" : f"Api error {response.status_code}"
        }

    response_data = response.json()

    info = {}

    needed = [
        "global_name",
        "username",
        "id",
        "email",
        "phone"
    ]

    for item in needed:
        info[item] = response_data.get(item, "N/A")

    return {
        "status": "success",
        "data" : {
            "info" : info
        }
    }
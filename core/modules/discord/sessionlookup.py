
def discord_session(self, args):

    api = "https://discord.com/api/v9/auth/sessions"
    headers = {
        "Authorization" : args["token"],
        "Content-Type" : "Application/Json"
    }

    response = self.session.get(
        api, headers=headers
    )

    if response.status_code != 200:
        return {
            "status" : "error",
            "message" : f"API error {response.status_code}"
        }
    
    response_data = response.json()

    info = {}

    sessions = response_data["user_sessions"]

    current = sessions[-1]

    response_data["current"] = current

    for session in sessions:
        hash = session["id_hash"]
        last_use = session["approx_last_used_time"]
        
        client_info = session["client_info"]

        os = client_info["os"]
        platform = client_info["platform"]
        location = client_info["location"]


        
        trunc_hash = hash[:5]

        items = {
            "Hash" : hash,
            "Last Use" : last_use,
            "OS" : os,
            "Platform" : platform,
            "Location" : location,
            "[!]" : "-" * 45
        }

        for key, value in items.items():
            info[f"{trunc_hash} | [?] {key}"] = value 



    return {
            "status" : "success",
            "data"   : {
                "info" : info
            }
        }
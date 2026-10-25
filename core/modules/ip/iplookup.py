
def ip_lookup(self, args):
    ip = args.get("ip")

    api = "http://ip-api.com/json/{}".format(ip)

    response = self.session.get(api)

    if response.status_code != 200:
        return {
            "message" : "error",
            "info" : "Failed lookup [{}]".format(response.status_code)
        }
    return {
        "message" : "success",
        "info" : response.json( )
    }
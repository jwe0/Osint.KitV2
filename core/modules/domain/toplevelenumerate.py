import socket, threading
from core.modules.logging import *

class Enumerate_:
    def __init__(self, domain):
        self.domain     = domain
        self.subs       = "core/dependencies/topleveldomains.txt"
        self.prog       = 0
        self.subs_count = 0

        self.result = {"domain" : "Status"}

        self.domains = []

        self.load_subs()

    def load_subs(self):
        for subs in open(self.subs, "r"):
            self.domains.append(subs.strip())
        self.subs_count = len(self.domains)

    def scan(self, domain):
        try:
            socket.gethostbyname(domain)
            self.result[domain] = "Found"
        except:
            pass
        self.prog += 1

    def run(self):
        for sub in self.domains:
            api = self.domain.split(".")[0] + "." + sub
            threading.Thread(target=self.scan, args=[api]).start()

        while int(self.prog) + 1 != int(self.subs_count):
            percent = (self.prog / self.subs_count) * 100
            msg = info(f"{percent:.2f}% [{self.prog}/{self.subs_count}]", False)
            print(msg, end="\r")
        print()
        return self.result


def top_level_enumerate(self, args):
    enum = Enumerate_(args.get("domain"))
    result = enum.run()
    return {
        "status" : "success",
        "data" : {
            "info" : result
        }
    }
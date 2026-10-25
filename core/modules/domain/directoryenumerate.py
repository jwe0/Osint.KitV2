import threading
from core.modules.logging import *

class Enumerate_:
    def __init__(self, url, ext):
        self.url       = url
        self.external  = ext
        self.dirs      = "core/dependencies/subdirectories.txt"
        # self.dirs      = ["content/contact.html", "content/projects.html"]
        self.prog      = 0
        self.dir_count = 0

        self.result = {"link" : "code"}

        self.paths = []

        self.load_dirs()

    def load_dirs(self):
        for dir in open(self.dirs, "r"):
            self.paths.append(dir.strip())
        self.dir_count = len(self.paths)

    def scan(self, url):
        try:
            response = self.external.session.get(
                url
            )

            if response.status_code == 200:
                self.result[url] = response.status_code
                print(response.status_code)
        except:
            pass
        self.prog += 1

    def run(self):
        for dir in self.paths:
            api = self.url + dir
            threading.Thread(target=self.scan, args=[api]).start()

        while int(self.prog) + 1 != int(self.dir_count):
            percent = (self.prog / self.dir_count) * 100
            msg = info(f"{percent:.2f}", False)
            print(msg, end="\r")
        return self.result




def dir_enumerate(self, args):
    enum = Enumerate_(args.get("url"), self)
    result = enum.run()

    return {
        "message" : "success",
        "info" : result
    }
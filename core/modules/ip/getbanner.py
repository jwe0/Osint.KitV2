import socket

def getbanner(self, args):
    ip = args.get("host")
    port = args.get("port")

    s = socket.socket()
    try:
        s.settimeout(5)
        s.connect((ip, int(port)))
        banner = s.recv(1024).decode().strip()
        s.close()
    except:
        return {
            "status" : "error", 
            "message" : "Could not connect to server"
        }
    if banner:
        return {
            "status" : "success", 
            "data" : {
                "info" : {"banner" : banner}
            }
        }
    else:
        return {
            "status" : "error", 
            "message" : "Banner not found"
        }
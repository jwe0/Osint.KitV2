import tls_client
from core.modules.init import ascii_art, clear_screen, flatten_json, load_config
from core.modules.logging import *


# General
from core.modules.general.cc_checker import cc_checker
from core.modules.general.maclookup import maclookup
from core.modules.general.defaultrouter import router

# IP
from core.modules.ip.iplookup import ip_lookup
from core.modules.ip.getbanner import getbanner
from core.modules.ip.isproxy import isproxy

# Domain
from core.modules.domain.directoryenumerate import dir_enumerate
from core.modules.domain.subdomaineumerate import sub_domain_enumerate
from core.modules.domain.toplevelenumerate import top_level_enumerate

# Discord
from core.modules.discord.useridlookup import user_id_lookup
from core.modules.discord.webhooklookup import webhook_lookup
from core.modules.discord.tokenlookup import token_lookup
from core.modules.discord.sessionlookup import discord_session

class Main:
    def __init__(self):
        self.modules = {
            "General" : {
                "CC_Checker" : {
                    "name" : "CC Checker",
                    "description" : "Check if a card has a valid bank BIN",
                    "args" : ["card"],
                    "func" : cc_checker
                },
                "Router_PW" : {
                    "name" : "Default router password",
                    "description" : "Find default passwords to common routers",
                    "args" : ["model", "brand"],
                    "func" : router
                },
                "Mac_Lookup" : {
                    "name" : "Mac lookup",
                    "description" : "Lookup mac address info",
                    "args" : ["mac"],
                    "func" : maclookup
                }
            },
            "IP" : {
                "IP_Lookup" : {
                    "name" : "IP Lookup",
                    "description" : "Plain old IP lookup",
                    "args" : ["ip"],
                    "func" : ip_lookup
                },
                "Banner" : {
                    "name" : "Banner lookup",
                    "description" : "Get a server banner",
                    "args" : ["host", "port"],
                    "func" : getbanner
                },
                "IsProxy" : {
                    "name" : "Is Proxy",
                    "description" : "Checks an IP against a common proxy list",
                    "args" : ["ip"],
                    "func" : isproxy
                }
            },
            "Domain" : {
                "Directory_Fuzz" : {
                    "name" : "Directory enumerator",
                    "description" : "Find hidden pages eg (https://google.com/)",
                    "args" : ["url"],
                    "func" : dir_enumerate
                },
                "Subdomain_Enumerate" : {
                    "name" : "Subdomain Enumerate",
                    "description" : "Enumerate subdomains from a domain eg (google.com)",
                    "args" : ["domain"],
                    "func" : sub_domain_enumerate
                },
                "Toplevel_Enumerate" : {
                    "name" : "Top level enumerate",
                    "description" : "Enumerate all domains eg (google.com)",
                    "args" : ["domain"],
                    "func" : top_level_enumerate
                }
            },
            "Discord" : {
                "UserID_Lookup" : {
                    "name" : "User ID lookup",
                    "description" : "Lookup a user ID",
                    "args" : ["user_id"],
                    "func" : user_id_lookup
                },
                "Webhook_Lookup" : {
                    "name" : "Webhook Lookup",
                    "description" : "Pull webhook info",
                    "args" : ["webhook"],
                    "func" : webhook_lookup
                },
                "Token_Lookup" : {
                    "name" : "Token Lookup",
                    "description" : "Lookup private token details",
                    "args" : ["token"],
                    "func" : token_lookup
                },
                "Discord_Session" : {
                    "name" : "Session Lookup",
                    "description" : "Grab a tokens sessions",
                    "args" : ["token"],
                    "func" : discord_session
                }
            }
        }

        self.conversion_table = {}
        for i, section in enumerate(self.modules):
            self.conversion_table[str(i + 1)] = section

        self.session = tls_client.Session()

        self.method_count, self.module_count = self.count_modules()

        self.config = load_config()

    def count_modules(self):
        methods = 0
        modules = 0

        for section in self.modules:
            methods += 1
            for module in self.modules[section]:
                modules += 1

        return methods, modules

    def menu(self):
        clear_screen()
        ascii_art()
        print("❱ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ /ᴊᴡᴇ0   ")
        print(f"❱ ʟᴏᴀᴅᴇᴅ | ᴍᴇᴛʜᴏᴅꜱ [{self.method_count}] | ᴍᴏᴅᴜʟᴇꜱ [{self.module_count}]")
        print("❱ ᴇɴᴛᴇʀ !Q ᴛᴏ ʀᴇᴛᴜʀɴ")
        print()

    def main(self):
        while True:
            def start():
                self.menu()
                info(f"[>] Home")
                print()

            def get_section():

                for section in self.conversion_table:
                    info(f"[{section}] {self.conversion_table[section]}")
                print()
                section_choice = inpt("Section")

                while not section_choice.isdigit() or section_choice not in self.conversion_table:
                    error("Please enter a valid section value")
                    section_choice = inpt("Section")

                return self.conversion_table[section_choice]


            def get_module(section_):
                self.menu()
                info(f"[>] Home/{section_}")
                print()

                temp_conversion_table = {}

                for i, module in enumerate(self.modules[section_]):
                    temp_conversion_table[str(i + 1)] = module

                if not temp_conversion_table:
                    error("No modules created")
                    inpt("Press enter to continue")
                    return
                
                for module in temp_conversion_table:
                    info(f"[{module}] {temp_conversion_table[module]}")
                print()

                module_choice = inpt("Module")

                if module_choice.lower() == "!q":
                    return {
                        "response" : "reboot"
                    }

                while not module_choice.isdigit() or module_choice not in temp_conversion_table:
                    error("Please enter a valid module value")
                    module_choice = inpt("Module")
                    if module_choice.lower() == "!q":
                        return {
                            "response" : "reboot"
                        }

                return {
                    "response" : temp_conversion_table[module_choice]
                }
            
            def run_module(section_, module_):

                self.menu()
                info(f"[>] Home/{section_}/{module_}")
                print()

                module_info = self.modules[section_][module_]

                module_name = module_info["name"]
                module_desc = module_info["description"]
                module_args = module_info["args"]
                module_func = module_info["func"]

                
                info(f"Module: {module_name}")
                info(f"{module_desc}")

                print()

                args = {}

                for arg in module_args:
                    arg_input = inpt(arg.title())
                    if arg_input == "!q":
                        return
                    while not arg_input:
                        error("Please enter an argument")
                        arg_input = inpt(arg.title())
                        if arg_input == "!q":
                            return
                    args[arg] = arg_input

                if not args:
                    return
                
                self.menu()
                info(f"[>] Home/{section_}/{module_}/Confirm")
                print()
                for arg in args:
                    info(f"{arg.title()} = [{args[arg]}]")

                    print()

                confirm = inpt("Would you like to execute this ?module y/n")

                if confirm.lower() == "y":

                    self.menu()
                    info(f"[>] Home/{section_}/{module_}/Confirm/Executing")
                    print()

                    response = module_func(self, args)

                    self.menu()
                    info(f"[>] Home/{section_}/{module_}/Confirm/Executing/Results")
                    print()

                    message     = response["status"]

                    if message == "error":
                        print()
                        error("Module failed")
                        info(response["message"])
                    else:
                        success("Module ran")
                        print()
                        
                        flatten_json(response["data"])

                else:
                    print()
                    error("Cancelled by user request")
                print()
                inpt("Press enter to continue")


            while True:
                start()
                section = get_section()
                module = get_module(section).get("response")

                if module == "reboot":
                    continue
                else:
                    run_module(section, module)

if __name__ == "__main__":
    main = Main()
    main.main()
            
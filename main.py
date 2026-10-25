import json, tls_client
from core.modules.init import ascii_art, clear_screen, flatten_json
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
                    "args" : ["ip", "port"],
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
                    "description" : "Find hidden pages",
                    "args" : ["url"],
                    "func" : dir_enumerate
                },
                "Subdomain_Enumerate" : {
                    "name" : "Subdomain Enumerate",
                    "description" : "Enumerate subdomains from a domain",
                    "args" : ["domain"],
                    "func" : sub_domain_enumerate
                }
            }
        }

        self.conversion_table = {}
        for i, section in enumerate(self.modules):
            self.conversion_table[str(i + 1)] = section

        self.session = tls_client.Session()

    def menu(self):
        clear_screen()
        ascii_art()

    def main(self):
        while True:
            self.menu()
            info(f"[>] Home")
            print()

            for section in self.conversion_table:
                info(f"[{section}] {self.conversion_table[section]}")
            section_choice = inpt("Section")

            while not section_choice.isdigit() or section_choice not in self.conversion_table:
                error("Please enter a valid section value")
                section_choice = inpt("Section")

            section_ = self.conversion_table[section_choice]

            self.menu()
            info(f"[>] Home/{section_}")
            print()

            temp_conversion_table = {}

            for i, module in enumerate(self.modules[section_]):
                temp_conversion_table[str(i + 1)] = module

            if not temp_conversion_table:
                error("No modules created")
                inpt("Press enter to continue")
                continue

            for module in temp_conversion_table:
                info(f"[{module}] {temp_conversion_table[module]}")

            module_choice = inpt("Module")

            if module_choice == "!q":
                continue

            while not module_choice.isdigit() or module_choice not in temp_conversion_table:
                error("Please enter a valid module value")
                module_choice = inpt("Module")

            module_ = temp_conversion_table[module_choice]

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

            args = {}

            for arg in module_args:
                arg_input = inpt(arg.title())
                if arg_input == "!q":
                    continue
                while not arg_input:
                    error("Please enter an argument")
                    arg_input = inpt(arg.title())
                args[arg] = arg_input

            if not args:
                continue
            
            self.menu()
            info(f"[>] Home/{section_}/{module_}/Confirm")
            print()
            for arg in args:
                info(f"{arg.title()} = [{args[arg]}]")

            confirm = inpt("Would you like to execute this moduke? y/n")

            if confirm.lower() == "y":

                self.menu()
                info(f"[>] Home/{section_}/{module_}/Confirm/Executing")
                print()

                response = module_func(self, args)

                self.menu()
                info(f"[>] Home/{section_}/{module_}/Confirm/Executing/Results")
                print()

                message     = response["message"]
                information = response["info"]

                if message == "error":
                    print()
                    error("Module failed")
                    info(information)
                else:
                    success("Module ran")
                    print()
                    flatten_json(information)

            else:
                print()
                error("Cancelled by user request")
            print()
            inpt("Press enter to continue")


if __name__ == "__main__":
    main = Main()
    main.main()
            
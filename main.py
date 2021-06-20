import subprocess
import optparse
# regex
import re


def get_command():
    # optParse object takes argument from command line
    parse_object = optparse.OptionParser()
    #  For interface
    parse_object.add_option("-i", "--interface", dest="interface", help="interface to change")

    # For mac address , it may change later
    parse_object.add_option("-m", "--mac", dest="mac_address", help="new mac adress")
    return parse_object.parse_args()

    # Sign


def change_mac(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", "ether", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_after_process(user_interface):
    ifconfig = subprocess.check_output(["ifconfig", user_interface])

    # new mac does not return string it is a group
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac:
        return new_mac.group(0)
    else:
        return None


# Welcome Screen


print("\033[3;31;40m Mac Changer -V 0.0.1  \n Coded By M.OnerKocal \n")


(user_input, arguments) = get_command()
change_mac(user_input.interface, user_input.mac_address)
final_mac = control_after_process(str(user_input.interface))
if final_mac == user_input.mac_address:
    print("Succes ! ")
else:
    print("Error ur mac did not changed ! ")

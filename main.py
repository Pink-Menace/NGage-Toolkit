import os, sys, time, subprocess, termcolor, modules, getmac, getpass, platform, socket
from getmac import get_mac_address as gma
from termcolor import cprint, colored
from modules import __classes__

os.system('clear')

colors = __classes__.colors
highlights = __classes__.highlights
attributes = __classes__.attributes
banner = """
 ##############################################
 ##############################################
 ###                                        ###
 ###  #     #  #####                        ###
 ###  ##    # #     #   ##    ####  ######  ###
 ###  # #   # #        #  #  #    # #       ###
 ###  #  #  # #  #### #    # #      #####   ###
 ###  #   # # #     # ###### #  ### #       ###
 ###  #    ## #     # #    # #    # #       ###
 ###  #     #  #####  #    #  ####  ######  ###
 ###                                        ###
 ##############################################
 ##############################################
 """

def device_ip():
  ip_addr = subprocess.run(["ip route | awk '{print $9}'"], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
  return colored(ip_addr, colors.green, attrs = attributes.bold)
    
def root_check():
  passed = "Your device is rooted"
  failed = "Your device is not rooted"
  rooted = os.getuid()
  if rooted == 0:
    return passed
  else:
    return failed

def system():
  sys_arch = " ".join(platform.architecture())
  system_specs = """System: %s
Release: %s
Machine: %s
Architecture: %s
Total Device Space: %s bytes of storage
Root Check: %s
Mac Address: %s
IP Address: %s""" % (platform.system(), platform.release(), platform.machine(), sys_arch, os.statvfs('/').f_frsize, root_check(), gma(), device_ip())
  cprint(colored(system_specs, colors.green, attrs = attributes.bold))

cprint(colored(banner, colors.cyan, attrs = attributes.bold))
cprint(colored("""The NGage Toolkit was developed by J0k3r for testing purposes on Termux. I am not responsible for any damages or illegal actions caused/performed during the usage of my software. All my software is released as is, and free of charge, without warranty. Thank you for choosing to use the NGage-Toolkit!
""", colors.green, attrs = attributes.bold))
cprint(colored("""Welcome to the NGage Menu:
01: NGage Network Tools
02: NGage Tools Downloader
03: NGage Device Management
04: NGage Device Specifications
05: NGage Discord Tools
06: NGage Root Checker
07: Restart NGage-Toolkit
08: Exit NGage Toolkit
""", colors.yellow, attrs = attributes.bold))
selection = input(colored(">>> Please Select An Option: ", colors.magenta, attrs = attributes.bold))

if selection == '1':
  os.system('python modules/network.py')
elif selection == '2':
  os.system('python modules/tools-installer.py')
elif selection == '3':
  os.system('python modules/device-management.py')
elif selection == '4':
  os.system('clear')
  system()
  time.sleep(5)
  os.system('python main.py')
elif selection == '5':
  os.system('python modules/discord-tools.py')
elif selection == '6':
  os.system('clear')
  cprint(colored("Root Checker Results: %s" % root_check(), colors.green, attrs= attributes.bold))
  time.sleep(2)
  os.system('python main.py')
elif selection == '7':
  os.system('clear && python main.py')
elif selection == '8':
  os.system('clear')
  sys.exit()
else:
  sys.exit()
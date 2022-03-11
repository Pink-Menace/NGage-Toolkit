import os, sys, urllib, termcolor, __classes__
from urllib.request import Request as reqs, urlopen, urlretrieve
from termcolor import cprint, colored 

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
cprint(colored(banner, colors.cyan, attrs = attributes.bold))
cprint(colored("""Welcome to the Tools Downloader Menu:
01: Clavis Keyboard
02: Acode Pro apk (best android ide)
03: ShowKey Latest apk
04: DroidEdit Pro (Notepad++ equivalent for android)
05: Termux Desktop
06: Back To The Main Menu
""", colors.yellow, attrs = attributes.bold ))
selection = input(colored(">>> Please Select An App To Download: ", colors.magenta,  attrs = attributes.bold))
if selection == '1':
  url = "https://github.com/J0k3r-Squ4d/cracked-apks/raw/main/Clavis%20Keyboard%20Free_v2.05_free_apkpure.com.apk"
  cprint(colored("Downloading Clavis Keyboard apk", colors.green, attrs = attributes.bold))
  #urlretrieve(url, "/sdcard/clavis_keyboard.apk")
  cprint(colored("Clavis Keyboard apk finished downloading", colors.green, attrs = attributes.bold))
elif selection == '2':
  url = "https://github.com/J0k3r-Squ4d/cracked-apks/raw/main/_OceanofAPK.com_Acode-v1.1.14.138_build_138.apk"
  cprint(colored("Downloading Acode Pro apk", colors.green, attrs = attributes.bold))
 # urlretrieve(url, "/sdcard/acode_pro_cracked.apk")
  cprint(colored("Acode Pro apk finished downloading", colors.green, attrs = attributes.bold))
elif selection == '3':
  url = "https://github.com/J0k3r-Squ4d/cracked-apks/raw/main/showkey_1.0.apk"
  cprint(colored("Downloading ShowKey apk", colors.green, attrs = attributes.bold))l
 # urlretrieve(url, "/sdcard/ShowKey.apk")
  cprint(colored("ShowKey finished downloading", colors.green, attrs = attributes.bold))
elif selection == '4':
  url = "https://github.com/J0k3r-Squ4d/cracked-apks/raw/main/DroidEdit_Pro_Mod_v1.23.7_ApkModo.apk"
  cprint(colored("Downloading DroidEdit Pro", colors.green, attrs = attributes.bold))
 # urlretrieve(url, "/sdcard/DroidEditPro.apk")
  cprint(colored("DroidEdit Pro finished downloading", colors.green, attrs = attributes.bold))
elif selection == '5':
  os.system('git clone https://github.com/adi1090x/termux-desktop')
elif selection == '6':
  os.system('python main.py')
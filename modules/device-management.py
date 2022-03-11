import os, sys, urllib, shutil, termcolor, __classes__
from termcolor import cprint, colored
from urllib.request import urlretrieve

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
cprint(colored("""Welcome to the Device Management Menu:
01: Delete File
02: Delete Directory
03: Create Folder
04: ES File Manager Pro Apk
05: Start/Stop SSH Service
06: Back To The Main Menu
""", colors.yellow, attrs = attributes.bold))
selection = input(colored(">>> Please Select An Option: ", colors.magenta,  attrs = attributes.bold))
if selection == '1':
  path = input(colored("File Path (i.e path/to/file/example.txt): ", colors.magenta,  attrs = attributes.bold))
  os.system('rm -r ' + path)
elif selection == '2':
  path = input(colored("Folder Path (i.e path/to/folder): ", colors.magenta,  attrs = attributes.bold))
  shutil.rmtree(path)
elif selection == '3':
  dir_name = input(colored("Directory Name: ", colors.magenta,  attrs = attributes.bold))
  os.system('mkdir ' + dir_name)
elif selection == '4':
  url = "https://github.com/J0k3r-Squ4d/es-file-manager-pro/raw/main/ES_File_Explorer_v4.2.4.3.2_MOD_apkmody.io.apk"
  cprint(colored("ES-File-Manager-Pro.apk is downloading to directory: /sdcard. Please Wait...", colors.yellow, attrs = attributes.bold))
  urlretrieve(url, "/sdcard/ES-File-Manager-Pro.apk")
  cprint(colored("ES-File-Manager-Pro.apk finished downloading. It is ready to install.", colors.yellow, attrs = attributes.bold))
elif selection == '5':
  os.system("sshd")
elif selection == '6':
  os.system("python main.py")
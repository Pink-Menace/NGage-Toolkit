import os, requests, termcolor, __classes__, time
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

def webhook_sender():
  webhook = input(colored("Please enter a webhook: ", colors.magenta))
  name = input(colored("Please enter your username: ", colors.magenta))
  message = input(colored("Please enter a message to send: ", colors.magenta))
  data = {
    "username": name,
    "content": message
  }
  requests.post(webhook, data=data)
  
def webhook_spammer():
  num = 0
  webhook = input(colored("Please enter a webhook: ", colors.magenta))
  name = input(colored("Please enter your username: ", colors.magenta))
  message = input(colored("Please enter a message to send: ", colors.magenta))
  data = {
    "username": name,
    "content": message
  }
  while True:
    num += 1
    requests.post(webhook, data=data)
    cprint(colored("[%s] I sent the message to the webhook" % num, colors.cyan))
    if num == 100:
      cprint(colored("Ratelimiting Detected. Restarting Spammer...", colors.red, attrs = attributes.bold))
      time.sleep(2)
      num = 0
      continue
  
cprint(colored(banner, colors.cyan, attrs = attributes.bold))  
cprint(colored("""Welcome to the Discord Tools Menu:
01: NGage Webhook Sender
02: NGage Webhook Spammer
03: Back To The Main Menu
""", colors.yellow, attrs = attributes.bold))
selection = input(colored(">>> Please Select An Option: ", colors.magenta))

if selection == '1':
  webhook_sender()
elif selection == '2':
  webhook_spammer()
elif selection == '3':
  os.system('python main.py')

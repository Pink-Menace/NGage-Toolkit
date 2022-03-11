import asyncio, aiohttp, time, socket, os, sys
from aiohttp import ClientSession

os.system('clear')

if sys.version[0] in '2':
        exit("Use python 3.9")

print("""Make Sure URLs Are Correct
Some sites may disconnect""")
target = input("[*] Target website: ")

time.sleep(1)
print ("Checking links list...")
try:
	wu = open("__dicts__/links.txt","r").readlines()
	x = len(wu)
except IOError:
	print ("[!] Can't load links.txt, file does not exist")
	os.system('python main.py')		
time.sleep(1)
print ("[#] Load words in wordlist.txt".format(x))

time.sleep(1)
localtime = time.asctime( time.localtime(time.time()) )
print ("\n[*] Starting @", localtime)
print ("")

target = target.replace('https://', '')
target = target.replace('https://www.', '')
target = target.replace('http://', '')
target = target.replace('http://www.', '')
tar_list = target.split('/')
for tar in tar_list:
    if tar == '':
        tar_list.remove(tar)
target = '/'.join(tar_list)
target = 'http://' + target+'/'

start = time.time()
dfv = []
conn = aiohttp.TCPConnector(
        family=socket.AF_INET,
    )
semaphore = asyncio.Semaphore(100)
    
def daf():
    a=time.ctime().split(' ')[4]
    return a
    
async def fetch(url, session):
    async with session.get(url) as response: 
        status = response.status 
        if status == 200:
            print("{}".format(status, response.url,))
            dfv.append(response.url)
        elif status == 404:
            print("{}".format(status, response.url,))
        elif status == 403:
            print("{}".format(status, response.url,))
        else:
            print("{} {}".format(status, response.url,))
        return await response.read()

async def run():
    url = target + "{}"
    tasks = []
    admin_list = open('__dicts__/links.txt', 'r')
    paths = []
    for path in admin_list:
        path = path.replace('\n','')
        paths.append(path)
    async with semaphore:
      async with ClientSession(connector=conn) as session:
          for i in paths:
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)
            responses = asyncio.gather(*tasks)
            await responses
        
loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run())
loop.run_until_complete(future)

demon = "Results: "
file = open('.logs/admin-results.txt', 'w')
end = time.time()
script_time = end - start
print("\n[*] Scan complete at seconds to complete @ {} ".format(script_time, localtime))
print("Results: ")
if len(dfv) == 0:
    print("[!] No result !!!")
else:
    for y in dfv:
        print("\n *" " ",y)
        file.write(f"Results: {dfv}")
        file.close()
        os.system('python main.py')
# install pip:
# pip install arseinrubika
# pip install colorama
# pip install rainbowtext
# pip install pyfiglet
# pip install colorama

import rainbowtext
import pyfiglet
from colorama import Fore
from time import sleep
from arsein import Messenger
print("")
sleep(3)
print(rainbowtext.text(pyfiglet.figlet_format("M E S T E R \n D A R K ")))

auth = input(Fore.LIGHTYELLOW_EX+"Enter Your auth: ")
guid = input(Fore.LIGHTYELLOW_EX+"Enter Your Guid-Gap: ")
gap = input(Fore.LIGHTYELLOW_EX+"Enter Your link-Gap: ")

app = Messenger(auth)
app.joinGroup(gap)

n = 'link acs sexi'
u = 'link acs sexi'

send = app.sendPhoto(guid,n)
app.sendPhoto(guid,u)

if send['status'] == 'OK':
  print("")
  print(Fore.LIGHTGREEN_EX+"Start Filter Account ✔️")
  sleep(2)
else:
  print("")
  print(Fore.LIGHTRED_EX+"auth Error !")
  left = app.lockGroup(gap)
  if left['status'] == 'OK':
    print(Fore.LIGHTGREEN_EX+"Left Your Group")
  else:
    print(Fore.LIGHTRED_EX+"Left Not Group")
    
app.sendMessage(guid, "روم عکس هایی که فرستادم گزارش بزنید تا فیلتر شم💔🗿")
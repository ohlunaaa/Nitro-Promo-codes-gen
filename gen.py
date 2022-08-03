import requests
import random
import string
from colorama import Fore
import time
from datetime import datetime

def gen():
    print(f"""{Fore.BLUE}
 ██▓███   ██▀███   ▒█████   ███▄ ▄███▓ ▒█████      ▄████▄   ▒█████  ▓█████▄ ▓█████   ██████ 
▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▒██▒  ██▒   ▒██▀ ▀█  ▒██▒  ██▒▒██▀ ██▌▓█   ▀ ▒██    ▒ 
▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒▓██    ▓██░▒██░  ██▒   ▒▓█    ▄ ▒██░  ██▒░██   █▌▒███   ░ ▓██▄   
▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░▒██    ▒██ ▒██   ██░   ▒▓▓▄ ▄██▒▒██   ██░░▓█▄   ▌▒▓█  ▄   ▒   ██▒
▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░▒██▒   ░██▒░ ████▓▒░   ▒ ▓███▀ ░░ ████▓▒░░▒████▓ ░▒████▒▒██████▒▒
▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░   ░  ░░ ▒░▒░▒░    ░ ░▒ ▒  ░░ ▒░▒░▒░  ▒▒▓  ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░
░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ ░  ░      ░  ░ ▒ ▒░      ░  ▒     ░ ▒ ▒░  ░ ▒  ▒  ░ ░  ░░ ░▒  ░ ░
░░         ░░   ░ ░ ░ ░ ▒  ░      ░   ░ ░ ░ ▒     ░        ░ ░ ░ ▒   ░ ░  ░    ░   ░  ░  ░  
            ░         ░ ░         ░       ░ ░     ░ ░          ░ ░     ░       ░  ░      ░  
                                                  ░                  ░                      {Fore.RESET}""")
    dc = input("Discord token: ")
    s = requests.Session()
    xd = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(12))
    email = f'{xd}@gmail.com'

    password = ''.join(random.choice(string.ascii_lowercase) for i in range(15))

    reg = {'email': email, 'userName': xd, 'password': password}

    headers = {
        'Accept': 'application/json', 
        'Content-Type': 'application/json', 
        'User-Agent': 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production',  
        'Medal-User-Agent': 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production'
        }

    r = s.post("https://medal.tv/api/users", json=reg, headers=headers)

    if r.status_code == 200:
        auth = {'email': email, 'password': password}
        r = requests.post("https://medal.tv/api/authentication", json=auth, headers=headers).json()
        token = r['userId'] + ',' + r['key']
        userID = r['userId']
        key = r['key']
        print(f'{Fore.GREEN}[Good]{Fore.RESET} Successfully from 1')  
    else:
        print(F"{Fore.RED} [FAIL]{Fore.RESET}")
        time.sleep(3)
        gen()

    headers1 = {
        'Authorization': dc,
        'Content-Type': 'application/json'
    }
    r = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers1)
    if r.status_code == 200:
        r_json = r.json()
        user_name = f'{r_json["username"]}#{r_json["discriminator"]}'
        user_id1 = r_json['id']
        avatar_id1 = r_json['avatar']
        phone_number = r_json['phone']
        email1 = r_json['email']
        mfa_enabled = r_json['mfa_enabled']
        flags = r_json['flags']
        locale = r_json['locale']
        verified = r_json['verified']
        creation_date = datetime.utcfromtimestamp(((int(user_id1) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
        has_nitro = False
        if has_nitro:
                d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
                days_left = abs((d2 - d1).days)
        print(f"{Fore.GREEN}[Username]{Fore.RESET} {user_name}")
        print(f"{Fore.GREEN}[User ID]{Fore.RESET} {user_id1}")
        print(f"{Fore.GREEN}[Creation Date]{Fore.RESET} {creation_date}")
        print(f"{Fore.GREEN}[Nitro Status]{Fore.RESET} {has_nitro}")
        print(f"{Fore.GREEN}[Nitro Information] {Fore.RESET}")
        if has_nitro:
            print(f"{Fore.GREEN}[Expires in]{Fore.RESET} {days_left} day(s)")
        else:
            print(f"{Fore.GREEN}[Expires in]{Fore.RESET} None \n")
    elif r.status_code == 401:
        print(f"{Fore.LIGHTRED_EX}[Error]{Fore.RESET} Invalid token  {dc}\n")
        time.sleep(2)
        gen()
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=headers1)
    nitro_data = res.json()
    r = s.post('https://medal.tv/social-api/connections', json={'provider': 'discord'}, headers={'Accept': 'application/json', 'Content-Type': 'application/json', 'User-Agent': 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production',  'Medal-User-Agent': 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production', 'X-Authentication': token}).json()
    try:
        x = s.post(r['loginUrl'], headers={'Authorization': dc, 'Content-Type': 'application/json'}, json={'permissions':'0', 'authorize':'true'}).json()
    except Exception as e:
        print(e)
        print(F"{Fore.RED}[FAIL]{Fore.RESET} Send me a dm a440")
        time.sleep(3)
        gen()
    try:
        r = s.get(x['location'])
    
    except Exception as e:
        print(e)
        print(F"{Fore.RED}[FAIL]{Fore.RESET} Send me a dm a440")
        gen()
    r = s.get('https://medal.tv/api/social/discord/nitroCode', headers={'Accept':'application/json', 'Content-Type':'application/json', 'User-Agent': 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production', 'Medal-User-Agent': 'Medal-Electron/4.1674.0 (string_id_v2; no_upscale) win32/10.0.19042 (x64) Electron/8.5.5 Recorder/1.0.0 Node/12.13.0 Chrome/80.0.3987.163 Environment/production', 'X-Authentication': token}).json() 
    print(r)
    Status_code = r['httpStatusCode']
    if Status_code == 400: 
        print(F"{Fore.RED}[FAIL]{Fore.RESET} You must have a Discord connection to do this")
        time.sleep(3)
        gen()
    if Status_code == 429:
        print(F"{Fore.RED}[FAIL]{Fore.RESET} Ratelimited")
        time.sleep(3)
        gen()
    else:
        print(f"{Fore.GREEN}[Good]{Fore.RESET} {r}")
        gfd = open('link.txt','a+')
        gfd.write(str(r) + str('\n'))
        time.sleep(3)
        gen()
gen()
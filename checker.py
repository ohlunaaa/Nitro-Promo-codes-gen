
import os
import re
from requests import get
from colorama import Fore
import time


def filter_tokens(unfiltered):
    tokens = []
    for line in [x.strip() for x in unfiltered.readlines() if x.strip()]:
        for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
            for token in re.findall(regex, line):
                if token not in tokens:
                    tokens.append(token)

    return tokens

def checker(token):
    response = get(f'https://discordapp.com/api/v9/users/@me/library',headers={'Authorization': token})
    if "You need to verify your account in order to perform this action." in str(
        response.content) or "401: Unauthorized" in str(response.content):
        return False
    elif response.status_code == 401:
        return 'Invalid'
    else:
        return True


def manager():
    if __name__ == "__main__":
        try:
            checked = []
            with open('tokens.txt', 'r') as tokens:
                filtered = filter_tokens(tokens)
                filtr = len(filtered)
                for token in filtered:
                    if len(token) > 15 and token not in checked and checker(token) == True:
                        print(f'{Fore.LIGHTGREEN_EX}[+] {Fore.RESET}{token} Valid')
                        checked.append(token)
                    else:
                        print(f'{Fore.LIGHTRED_EX}[-] {Fore.RESET}{token} Invalid')
            if len(checked) > 0:
                save = input(f'{len(checked)} Valid\nDo you want to Save only Valid tokens? (y/n): ').lower()
                if save == 'y':
                    name = 'tokens'
                    with open(f'{name}.txt', 'w') as saveFile:
                        saveFile.write('\n'.join(checked))
                    print(f'{Fore.LIGHTGREEN_EX}[+]{Fore.RESET} Tokens saved to {name}.txt file!')
        except:
            print(f'{Fore.LIGHTRED_EX}[-]{Fore.RESET} Error, cant open tokens.txt file...... :(!')


start = input('press any key to start: ')
start = manager()

time.sleep(5)
exit = input('press any key: ')
clear = lambda: os.system('cls')
exit = clear()
import random

from utils import Requests
from lib.colors import Colors

async def vpnchecker(ip):
    with open("useragents.txt", "r") as user_file:
        user = user_file.read().split('\n')

    url = "https://api.protonmail.ch/vpn/logicals"

    response = await Requests(url, headers={"User-Agent": random.choice(user)}).sender()

    try:
        if ip in response.text:
            output = f"\n{Colors.CYAN}Proton{Colors.END}   | x | This IP address is currently affiliated with ProtonVPN."

        else:
            output =  f"\n{Colors.RED}Proton{Colors.END}   | x | This IP address is not currently affiliated with ProtonVPN."
    except Exception:
        output =  f"[-] ProtonRate limit."

    return output
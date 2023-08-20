import os
import argparse
from banner import *
from modules.ip_info import IP_TRACK

async def parser():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "ip",
        nargs="?",
        type=str,
        default=None,
        help="Type a IP ADDRESS"
    )
    args = parser.parse_args()

    if args.ip:
        print(MAIN_BANNER)
        Ip = args.ip
        IP_TRACK(Ip)

    else:
        print(MENU_BANNER)
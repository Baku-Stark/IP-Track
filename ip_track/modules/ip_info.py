import os
import json
from lib.colors import Colors

try:
    import requests

except ModuleNotFoundError:
    os.system("python install -r requirements.txt")
    print(Colors.GREEN + "INSTALLATION COMPLETED!" + Colors.END)
finally:
    pass

def IP_TRACK(ip: str):
    track_req = requests.get(
        f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query", timeout=5
    )
    # print(track_req.json())

    track = track_req.json()

    if track['status'] == 'success':
        print(Colors.BACK_GREEN + " IP ADDRESS " + Colors.END, end="")
        print(Colors.GREEN + f" {ip} - SUCCESS! " + Colors.END)
        print('')
        print(
            f"""
            ├── LOCATION -> (LAT: {track['lat']} | LON: {track['lon']})
                    ├── {track['timezone']}
                    ├── {track['continent']} - {track['continentCode']}
                    ├── {track['country']} - {track['countryCode']}
                    ├── {track['regionName']} - {track['region']}
                    └── {track['city']}
            """
        )
        print(
            f"""
            ├── SERVICE
                    ├── {track['isp']}
                    ├── {track['org']}
                    ├── {track['as']}
                    ├── {track['asname']}
                    └── {track['reverse']}
            """
        )
        print(
            f"""
            ├── CONNECTION
                    ├── HOST: {track['hosting']}
                    └── Mobile: {track['mobile']}
            """
        )
    
    else:
        print(Colors.BACK_RED + " IP ADDRESS " + Colors.END, end="")
        print(Colors.RED + f" {ip} - FAIL... " + Colors.END)
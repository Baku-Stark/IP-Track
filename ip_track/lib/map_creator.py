import requests
import folium, os

from lib.colors import Colors
from .temp import TempPrint

PATH = os.path.abspath("output/location.html")

class Creator:
    @staticmethod
    def GET_COORDINATES(ip: str) -> tuple():
        track_req = requests.get(
            f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query", timeout=5
        )
        track = track_req.json()
        return track['lat'], track['lon']
    
    @staticmethod
    def create_map(lat, long):
        map_world = folium.Map(location=[lat, long], zoom_start=5)
        folium.Marker(location=[lat, long], popup=f"{lat}\n{long}").add_to(map_world)

        return map_world
    
    @staticmethod
    def point_placer(ip: str):
        try:
            lat, lon = Creator.GET_COORDINATES(ip)
            map_with_point = Creator.create_map(lat, lon)
            map_with_point.save(PATH)
            TempPrint("[+] Creation of the map...").TPrint()
            print(f"[{Colors.GREEN}+{Colors.END}] Map created at path : {PATH}")

        except Exception as error:
            print(f"[{Colors.RED}!{Colors.END}] Error while creating the map : {PATH}")
            print(error)
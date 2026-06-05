import requests
from google_play_scraper import app

def AuToUpDaTE():
    
    r = requests.get('https://redzedupdater.vercel.app/').json()
    
    url = r['client_url']['ind']
    ob = r['latest_release_version']
    version = r['play_version']
    
    return url, ob, version, version
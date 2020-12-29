
from thailandpost_track import ThailandpostTrack
from bs4 import BeautifulSoup
import requests
from thailandpost_track import Language
from thailandpost_track import StatusCode
import json


URL = "https://api.trackingmore.com"

# Content-Type: application/json
Trackingmore_Api_Key: "2e6f4905-ab10-4abd-8a5f-b1636127c3ae"

header = {
	"Content-Type":"application/json",
	"Trackingmore-Api-Key":"2e6f4905-ab10-4abd-8a5f-b1636127c3ae",
}

r = requests.get(URL)
r.status_code
import requests
import json


URL = "https://api.trackingmore.com"

headers = {
	"Content-Type":"application/json",
	"Trackingmore-Api-Key":"2e6f4905-ab10-4abd-8a5f-b1636127c3ae",
}

r = requests.get(URL, headers=headers)
r.raise_for_status()
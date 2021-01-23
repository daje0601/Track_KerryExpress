from thailandpost_track import ThailandpostTrack
from bs4 import BeautifulSoup
import requests
from thailandpost_track import Language
from thailandpost_track import StatusCode
import json
import pprint

ENDPOINTS = {
    "API_ROOT": " https://trackapi.thailandpost.co.th",
    "AUTHENTICATE_TOKEN_PATH": "/post/api/v1/authenticate/token",
    "TRACK_PATH": "/post/api/v1/track",
}

headers = {
    "Content-Type": "application/json",
    "Authorization": "NNB5IdB:CFSwFNW-FDW:ZVM0V*XlJPPLB9U!AxUHLnR=O;CUXbWHRDVYRXYeInRsScAAUQJZYpBfPBQlXpS7ESIwFTH1L5S4HjX9",
}


barcode = "EF582568151TH"
thp = ThailandpostTrack(ENDPOINTS, headers=headers, data=barcode)
print(thp)
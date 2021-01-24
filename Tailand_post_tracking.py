from thailandpost_track import ThailandpostTrack
from bs4 import BeautifulSoup
import requests
from thailandpost_track import Language
from thailandpost_track import StatusCode
import json
import pprint

token = "NNB5IdB:CFSwFNW-FDW:ZVM0V*XlJPPLB9U!AxUHLnR=O;CUXbWHRDVYRXYeInRsScAAUQJZYpBfPBQlXpS7ESIwFTH1L5S4HjX9"

thp = ThailandpostTrack(token)

barcode = ["EF582568151TH"]
track = thp.track(barcode=barcode, status=StatusCode.ALL, language=Language.EN)


print(track)
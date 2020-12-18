from thailandpost_track import ThailandpostTrack
from bs4 import BeautifulSoup
import requests
from thailandpost_track import Language
from thailandpost_track import StatusCode
import json


TOKEN_KEY = "CAI:JfJhCVI?VHJQV~C!IkGYSaQsNfOCN~Z0Y8JAA$N~BmHMU6AoMnZPX-RbCBZKSZP-JWQGVwDyZ8EABYZJMMDHA&LNU5MqQ!F6"
thp = ThailandpostTrack(token_key=TOKEN_KEY)


barcode = ['ED384490065TH']
thp.track(barcode=barcode, status=StatusCode.FINAL_DELIVERY, language=Language.EN)
thp.expire()
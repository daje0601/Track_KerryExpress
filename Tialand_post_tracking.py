from thailandpost_track import ThailandpostTrack
from bs4 import BeautifulSoup
import requests
from thailandpost_track import Language
from thailandpost_track import StatusCode
import json


TOKEN_KEY = "HLEAN!R#ZTS?JFKzE*TxFYBMSqPSWNGhWKFxGMOUI=AxI~LgO#S+NSDxX@W6UnM;NIHlQBPZVVT%FaUzL3DjPQR*K:APNES9ZXY5"
thp = ThailandpostTrack(token_key=TOKEN_KEY)


# barcode = ['EF582568151TH']
# thp.track(barcode=barcode, status=StatusCode.FINAL_DELIVERY, language=Language.EN, encoding="UTF-8")

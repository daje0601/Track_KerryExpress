import requests
import json
import pprint


URL = "https://api.trackingmore.com/v2/carriers/detect"

headers = {
	"Content-Type":"application/json",
	"Trackingmore-Api-Key":"56e3999a-a656-4d00-b7ff-fae386fed96a",
}

tracking_number = "SHP5047646158"
data = {
	'tracking_number': tracking_number
}

r = requests.post(URL, headers=headers, data=json.dumps(data))
pprint.pprint(r.request.body)
print(r.status_code)
print(r.raise_for_status) # 200이 아니면 에러
pprint.pprint(json.loads(r.text))

res_data = r.json()

pprint.pprint(res_data['data'])

code = [d['code'] for d in res_data['data']][0]

realtime_url = 'https://api.trackingmore.com/v2/trackings/realtime'
realtime_req_data = {
	'tracking_number': tracking_number,
	'carrior_code': code
}
realtime_res = requests.post(realtime_url, headers=headers, data=json.dumps(realtime_req_data))
pprint.pprint(realtime_res.request.body)
print(realtime_res.status_code)
print(realtime_res.raise_for_status) # 200이 아니면 에러
pprint.pprint(json.loads(realtime_res.text))


# url = 'http://api.trackingmore.com/v2/carriers/detect'
# RelUrl = url + urlStr
# req = urllib.request.Request(RelUrl,requestData.encode('utf-8'), headers=headers,method="GET")
# result = urllib.request.urlopen(req).read()
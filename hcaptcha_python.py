import requests
import time
import json

api = "APIKEY"
sitekey = "SITEKEY"
pageurl = "PAGEURL"

url = f"https://2captcha.com/in.php?key={api}&method=hcaptcha&sitekey={sitekey}&pageurl={pageurl}&json=1"

response = requests.post(url)
data = response.json()

requestid = data['request']
print(data['request'])

while True:
    time.sleep(5)
    url2 = f"https://2captcha.com/res.php?key={api}&action=get&id={requestid}&json=1"
    response = requests.get(url2)
    data = response.json()
    if data['status'] == 1:
        print("CAPTCHA ÇÖZÜLDÜ.")
        yy2 = data['request']
        break
    else:
        print("CAPTCHA HAZIR DEĞİL.")

print(yy2)

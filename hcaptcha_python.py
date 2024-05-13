import requests
import time
import json

api = "e2f9ae503a1965015dac098d5be7c14a"
sitekey = "4c672d35-0701-42b2-88c3-78380b0db560"
pageurl = "https://canary.discord.com/register"

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

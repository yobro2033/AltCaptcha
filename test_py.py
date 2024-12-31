import subprocess, base64, time
import json
import requests
from altcha_pow import hash_match

headers = {
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': '_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1; _ga=GA1.1.732422030.1734463895; __hstc=126717202.11196e8fa4e7e5d8b3fa5df8c3ac9cd8.1734463895430.1734463895430.1734463895430.1; hubspotutk=11196e8fa4e7e5d8b3fa5df8c3ac9cd8; __hssrc=1; __hssc=126717202.17.1734463895430; _ga_V5MYF34JYV=GS1.1.1734463894.1.1.1734466862.16.0.0',
    'origin': 'https://tucowsdomains.com',
    'priority': 'u=1, i',
    'referer': 'https://tucowsdomains.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

data = {
    'action': 'tt_get_altcha_challenge',
}
session = requests.Session()
response = session.post('https://tucowsdomains.com/wp-admin/admin-ajax.php', headers=headers, data=data).json()
t = response["response"]["challenge"]
e = response["response"]["salt"]
r = response["response"]["algorithm"]
print(f"t: {t}, e: {e}, r: {r}")
signature = response["response"]["signature"]
result = hash_match(t, e, r)
altcha_result = base64.b64encode(json.dumps({"algorithm":r,"challenge":t,"number":result["number"],"salt":e,"signature":signature,"took":result["took"]}, separators=(',', ':')).encode()).decode()

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'vi-VN,vi;q=0.9',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://tucowsdomains.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://tucowsdomains.com/',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

data = {
    'domain': 'sad',
    'altcha_result': altcha_result,
    'altcha': altcha_result
}

response = session.post('https://tucowsdomains.com/provider-result/', headers=headers, data=data)
if "No match for" in response.text:
    print("Success")
else:
    print("Failed")
import curl_cffi

json_payload = {
  "refresh_token": "uewAz9yDJ_lcoB_SG7la0g",
  "platform": "android",
  "install_id": "169c3c4843de5925",
  "app_version": "2.5.13.2025"
}
r = curl_cffi.post("https://www.theinformation.com/api/v1/login", json=json_payload, impersonate="chrome_android")
rjson = r.json()
jwt = rjson["jwt"]
headers = {
  "Authorization": f"Bearer {jwt}"
}
r = curl_cffi.get("https://www.theinformation.com/api/v1/briefings?per_page=20&page=1&order=feed", headers=headers, impersonate="chrome")
print(r.json())

import curl_cffi

json_payload = {
  "refresh_token": "uewAz9yDJ_lcoB_SG7la0g",
  "platform": "android",
  "install_id": "169c3c4843de5925",
  "app_version": "2.5.13.2025"
}
r = curl_cffi.post("https://httpbin.org/post", json=json_payload, impersonate="chrome_android")

print(r.json())

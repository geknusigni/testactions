import json
import os
from datetime import datetime, timezone
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
data = r.json()

os.makedirs("./briefings", exist_ok=True)
timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
file_path = f"./briefings/{timestamp}.json"
with open(file_path, "w", encoding="utf-8") as f:
  json.dump(data, f, ensure_ascii=False, indent=4)

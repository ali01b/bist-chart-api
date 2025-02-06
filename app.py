# SCREENSHOTONE_API_KEY = "NFHVq-b8iZnSrg"
from flask import Flask, request, jsonify
import requests
import os
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# API Bilgileri
SCREENSHOTONE_API_KEY = "NFHVq-b8iZnSrg"
CLIENT_ID = "59a18efd50a05e8"
SCREENSHOT_FOLDER = "/tmp/screenshots"
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)  # Klasör oluştur

def take_screenshot(ticker):
    """ScreenshotOne kullanarak ekran görüntüsü alır."""
    screenshot_url = (
        f"https://api.screenshotone.com/take?wait_for_selector=canvas&access_key={SCREENSHOTONE_API_KEY}"
        f"&url=https://chart-index.vercel.app/chart?ticker={ticker}&full_page=true&format=png"
    )

    response = requests.get(screenshot_url, stream=True)
    if response.status_code == 200:
        filename = f"{int(time.time())}.png"
        filepath = os.path.join(SCREENSHOT_FOLDER, filename)
        with open(filepath, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        return filepath
    return None

def upload_to_imgur(image_path):
    """Resmi Imgur'a yükler ve URL'yi döndürür."""
    headers = {"Authorization": f"Client-ID {CLIENT_ID}"}
    with open(image_path, "rb") as img:
        response = requests.post(
            "https://api.imgur.com/3/upload",
            headers=headers,
            files={"image": img}
        )
    if response.status_code == 200:
        return response.json()["data"]["link"]
    return None

@app.route("/", methods=["GET"])
def screenshot():
    """URL'nin ekran görüntüsünü alır, Imgur'a yükler ve JSON döndürür."""
    ticker = request.args.get("ticker")  # GET parametre olarak al

    if not ticker:
        return jsonify({"error": "ticker belirtilmedi"}), 400

    screenshot_path = take_screenshot(ticker)
    if not screenshot_path:
        return jsonify({"error": "Ekran görüntüsü alınamadı"}), 500

    imgur_url = upload_to_imgur(screenshot_path)
    os.remove(screenshot_path)  # Dosyayı sil

    if imgur_url:
        return jsonify({"message": "Başarılı", "imgur_url": imgur_url}), 200
    else:
        return jsonify({"error": "Imgur yükleme başarısız"}), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True)
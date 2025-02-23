from flask import Flask, request, jsonify
import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

SCREENSHOT_FOLDER = "screenshots"
CLIENT_ID = "5614fe898f24ff0"  # Imgur Client ID

# # Chrome ve ChromeDriver'ın yolları (Render için elle belirtiyoruz)
# CHROME_BINARY_PATH = "/tmp/chrome/chrome-linux64/chrome"
# CHROMEDRIVER_PATH = "/tmp/chromedriver/chromedriver-linux64/chromedriver"

# Render'da geçici klasörü oluştur
os.makedirs(SCREENSHOT_FOLDER, exist_ok=True)

def take_screenshot_selenium(ticker, type):
    """Selenium ile ekran görüntüsü alır."""
    
    # chrome_bin = os.environ.get("CHROME_BIN", "/code/chrome/chrome-linux64/chrome")
    # chromedriver_path = os.environ.get("CHROMEDRIVER_PATH", "/code/chromedriver/chromedriver-linux64/chromedriver")

    if type == "erol":
        url = f"https://bist-chart-app.onrender.com/charts/main?ticker={ticker}"
    else:
        url = f"https://bist-chart-app.onrender.com/charts/erolatasoy?ticker={ticker}"
        
    # Chrome Seçenekleri
    chrome_options = Options()
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    # WebDriver Başlat
    service = Service("/usr/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        driver.get(url)
        time.sleep(3)  # Sayfanın yüklenmesini bekle
        
        # Canvas elementinin yüklenmesini bekle
        driver.find_element(By.TAG_NAME, "canvas")

        # Screenshot kaydet
        filename = f"{int(time.time())}.png"
        filepath = os.path.join(SCREENSHOT_FOLDER, filename)
        driver.save_screenshot(filepath)
    except Exception as e:
        print(f"Hata: {e}")
        filepath = None
    finally:
        driver.quit()

    return filepath

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
    """Selenium ile ekran görüntüsü alır, Imgur'a yükler ve JSON döndürür."""
    ticker = request.args.get("ticker")
    types  = request.args.get("type")
    if not ticker:
        return jsonify({"error": "ticker belirtilmedi"}), 400

    screenshot_path = take_screenshot_selenium(ticker, type=types)
    if not screenshot_path:
        return jsonify({"error": "Ekran görüntüsü alınamadı"}), 500

    imgur_url = upload_to_imgur(screenshot_path)
    os.remove(screenshot_path)  # Dosyayı temizle

    if imgur_url:
        return jsonify({"message": "Başarılı", "imgur_url": imgur_url}), 200
    else:
        return jsonify({"error": "Imgur yükleme başarısız"}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)

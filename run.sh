#!/bin/bash

# 📌 LOG: Mevcut dizini göster
echo "🔍 Mevcut dizin: $(pwd)"

# 📌 LOG: Sistem klasörlerini kontrol et
echo "📂 /tmp içeriği:"
ls -lah /tmp

echo "📂 /opt içeriği (Salt okunur olabilir!):"
ls -lah /opt

echo "📂 /home içeriği:"
ls -lah ~/

# ✅ Geçici dizinler oluştur
mkdir -p /tmp/chrome
mkdir -p /tmp/chromedriver

# 🖥️ Headless Chromium'u indir ve yükle
echo "🌍 Headless Chromium indiriliyor..."
wget -O /tmp/chrome.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chrome-linux64.zip
unzip /tmp/chrome.zip -d /tmp/chrome/
chmod +x /tmp/chrome/chrome-linux64/chrome
rm /tmp/chrome.zip

# ✅ LOG: Chromium nereye indi?
echo "📂 Chromium kurulduğu dizin:"
ls -lah /tmp/chrome/chrome-linux64/

# 🖥️ ChromeDriver'ı indir ve yükle
echo "🌍 ChromeDriver indiriliyor..."
wget -O /tmp/chromedriver.zip https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip
unzip /tmp/chromedriver.zip -d /tmp/chromedriver/
chmod +x /tmp/chromedriver/chromedriver-linux64/chromedriver
rm /tmp/chromedriver.zip

# ✅ LOG: ChromeDriver nereye indi?
echo "📂 ChromeDriver kurulduğu dizin:"
ls -lah /tmp/chromedriver/chromedriver-linux64/

# 📌 LOG: /tmp dizinini tekrar kontrol et
echo "📂 /tmp içeriği (Güncellenmiş):"
ls -lah /tmp

# 📦 Python bağımlılıklarını yükle
pip install -r requirements.txt

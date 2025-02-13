#!/bin/bash

# Geçici dizin oluştur
mkdir -p /tmp/chrome
mkdir -p /tmp/chromedriver

# Headless Chromium'u indir ve yükle
echo "Headless Chromium yükleniyor..."
wget -qO- https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chrome-linux64.zip | unzip - -d /tmp/chrome
chmod +x /tmp/chrome/chrome-linux64/chrome

# ChromeDriver'ı indir ve yükle
echo "ChromeDriver yükleniyor..."
wget -qO- https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip | unzip - -d /tmp/chromedriver
chmod +x /tmp/chromedriver/chromedriver-linux64/chromedriver

# Python bağımlılıklarını yükle
pip install -r requirements.txt

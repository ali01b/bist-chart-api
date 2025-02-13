#!/bin/bash

# Headless Chromium ve ChromeDriver'ı indireceğimiz dizini belirleyelim
mkdir -p /opt/chrome
mkdir -p /opt/chromedriver

# Headless Chromium'u indir ve yükle
echo "Headless Chromium yükleniyor..."
wget -qO- https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chrome-linux64.zip | bsdtar -xf - -C /opt/chrome
chmod +x /opt/chrome/chrome-linux64/chrome

# ChromeDriver'ı indir ve yükle
echo "ChromeDriver yükleniyor..."
wget -qO- https://storage.googleapis.com/chrome-for-testing-public/122.0.6261.94/linux64/chromedriver-linux64.zip | bsdtar -xf - -C /opt/chromedriver
chmod +x /opt/chromedriver/chromedriver-linux64/chromedriver

# Python bağımlılıklarını yükle
pip install -r requirements.txt
#!/bin/bash

# Google Chrome'u indir ve yükle
echo "Google Chrome yükleniyor..."
curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt update && apt install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# ChromeDriver'ı indir ve yükle
echo "ChromeDriver yükleniyor..."
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv chromedriver /opt/chromedriver  # ChromeDriver'ı /opt dizinine taşıyoruz
rm chromedriver_linux64.zip

# Python bağımlılıklarını yükle
pip install -r requirements.txt

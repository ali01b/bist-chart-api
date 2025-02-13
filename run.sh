#!/bin/bash

# Google Chrome'u yükle
echo "Google Chrome yükleniyor..."
curl -O https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
apt install -y ./google-chrome-stable_current_amd64.deb
rm google-chrome-stable_current_amd64.deb

# ChromeDriver'ı yükle
echo "ChromeDriver yükleniyor..."
CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE)
wget -N https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
chmod +x chromedriver
mv chromedriver /usr/bin/chromedriver
rm chromedriver_linux64.zip

# Python bağımlılıklarını yükle
pip install -r requirements.txt

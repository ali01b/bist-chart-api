# Hafif bir Python sürümünü kullan
FROM python:3.10-slim

# Gerekli bağımlılıkları yükle
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg \
    --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Çalışma dizinini belirle
WORKDIR /code

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Flask uygulamasını kopyala
COPY . .

# Docker konteynerini başlat
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

# Použijeme základní obraz Pythonu
FROM python:3.9-slim

# Nastavíme pracovní adresář v kontejneru
WORKDIR /app

# Zkopírujeme požadavky do kontejneru
COPY requirements.txt .

# Nainstalujeme požadované balíčky
RUN pip install --no-cache-dir -r requirements.txt

# Zkopírujeme zbytek aplikace do kontejneru
COPY . .

# Definujeme příkaz, který se spustí při startu kontejneru
CMD ["python", "app.py"]
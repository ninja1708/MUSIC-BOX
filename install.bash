#!/bin/bash

# Sprawdź uprawnienia administratora
if [ "$EUID" -ne 0 ]; then
    echo "Uruchom skrypt z uprawnieniami administratora (sudo)."
    exit
fi

echo "Aktualizacja listy pakietów..."
apt update

echo "Instalacja zależności wymaganych do budowy Pythona 3.10..."
apt install -y software-properties-common wget build-essential \
    libssl-dev zlib1g-dev libncurses5-dev libnss3-dev libsqlite3-dev \
    libreadline-dev libffi-dev curl libbz2-dev

echo "Dodawanie repozytorium PPA dla Pythona..."
add-apt-repository -y ppa:deadsnakes/ppa
apt update

echo "Instalacja Pythona 3.10..."
apt install -y python3.10 python3.10-distutils

echo "Pobieranie skryptu instalacyjnego Pip..."
curl -sS https://bootstrap.pypa.io/get-pip.py -o get-pip.py

echo "Instalacja Pip dla Pythona 3.10..."
python3.10 get-pip.py

echo "Usuwanie skryptu instalacyjnego Pip..."
rm get-pip.py

echo "Instalacja biblioteki numpy..."
python3.10 -m pip install discord.py yt_dlp

echo "Instalowanie ffmepg"
apt install ffmpeg

echo "Instalacja upadate"
apt update




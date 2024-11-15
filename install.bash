#!/bin/bash

# Sprawdź uprawnienia administratora
if [ "$EUID" -ne 0 ]; then
    echo "Uruchom skrypt z uprawnieniami administratora (sudo)."
    exit
fi

echo "Aktualizacja listy pakietów..."
apt update

echo "Instalacja Pythona 3.10..."
apt install -y software-properties-common
add-apt-repository -y ppa:deadsnakes/ppa
apt update
echo "Pobieranie skryptu instalacyjnego Pip..."
apt install -y python3.10 python3.10-venv python3.10-dev python3-pip

echo "Instalowanie ffmepg"
apt install ffmpeg

echo "Instalacja bibliotek"
pip install discord discord.py yt_dlp
pip uninstall pynacl
pip install -U pynacl



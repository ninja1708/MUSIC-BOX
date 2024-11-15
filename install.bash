#!/bin/bash

# Sprawdź uprawnienia administratora
if [ "$EUID" -ne 0 ]; then
    echo "Uruchom skrypt z uprawnieniami administratora (sudo)."
    exit
fi

echo "Aktualizacja listy pakietów..."
apt update

echo "Instalacja Pythona 3.10..."
apt install python3.10

echo "Pobieranie skryptu instalacyjnego Pip..."
sudo apt install python3 python3-pip

echo "Usuwanie skryptu instalacyjnego Pip..."
rm get-pip.py
echo "Instalowanie ffmepg"
apt install ffmpeg

echo "Instalacja bibliotek"
python3.10 -m pip install discord.py yt_dlp
pip uninstall pynacl
pip install -U pynacl


# Discord Music Bot

Prosty bot muzyczny dla Discorda napisany w Pythonie, wykorzystujący `discord.py` oraz `yt-dlp`. Umożliwia użytkownikom odtwarzanie muzyki z YouTube, zarządzanie kolejką, pomijanie utworów oraz zatrzymywanie odtwarzania. Dodatkowo, zawiera zabawną funkcję gry "777", w której użytkownicy mogą stawiać zakłady i kręcić wirtualnymi owocami.

## Funkcje

- **Odtwarzanie muzyki**: Odtwarzanie audio z linków YouTube bezpośrednio w kanale głosowym.
- **Zarządzanie kolejką**: Dodawanie utworów do kolejki i pomijanie lub zatrzymywanie utworów.
- **Gra 777**: Gra w prostą maszynę do losowania symboli z zakładami i nagrodami.
- **Komendy bota**: Interakcja z botem za pomocą różnych komend do kontroli odtwarzania i grania w gry.

## Wymagania

- Python 3.8 lub wyższy
- Wymagane biblioteki Python:
  - `discord.py`
  - `yt-dlp`
  - `ffmpeg` (do przetwarzania audio)

## Instalacja

### 1. Skopiuj repozytorium:

```bash
git clone https://github.com/your-username/discord-music-bot.git
cd discord-music-bot
```
## 2. Utwórz środowisko wirtualne (opcjonalnie, ale zalecane):
```bash
python -m venv venv
source venv/bin/activate  # Na Windows użyj `venv\Scripts\activate`
```
## 3. Zainstaluj zależności:
```bash
pip install -r requirements.txt
```
## 4. Pobierz i zainstaluj FFmpeg:
```bash
sudo apt update
sudo apt upgrade
sudo apt install ffmpeg
```
Możesz pobrać FFmpeg stąd. Upewnij się, że dodasz FFmpeg do zmiennej PATH w systemie.

## 5. Ustaw token swojego bota:
# Ustawienia Bota w Discord Developer Portal
Aby skonfigurować swojego bota w Discord Developer Portal, wykonaj poniższe kroki:

- Krok 1: Przejdź do Discord Developer Portal
Zaloguj się na swoje konto Discord.
Przejdź do Discord Developer Portal.
- Krok 2: Utwórz nową aplikację
Kliknij przycisk New Application.
Wprowadź nazwę swojej aplikacji (np. "MyMusicBot") i kliknij Create.
- Krok 3: Utwórz bota
W menu po lewej kliknij Bot.
Kliknij Add Bot i potwierdź klikając Yes, do it!.
Twój bot zostanie utworzony, a teraz możesz zmienić jego nazwę, zdjęcie profilowe i inne ustawienia.
- Krok 4: Skopiuj token bota
Na stronie ustawień bota, w sekcji Bot, zobaczysz pole TOKEN.
Kliknij przycisk Copy obok Token.
Token jest kluczowy do uruchomienia bota w twoim kodzie — przechowuj go w bezpiecznym miejscu.
- Krok 5: Ustaw uprawnienia bota
Aby bot działał poprawnie, musisz przyznać mu odpowiednie uprawnienia.

# W sekcji Bot, przewiń w dół do Privileged Gateway Intents.
Włącz następujące uprawnienia:
  - MESSAGE CONTENT INTENT – Pozwala botowi na odczytywanie treści wiadomości (ważne, jeśli bot używa komend).
  - SERVER MEMBERS INTENT – Pozwala botowi zarządzać członkami serwera, jeśli jest to wymagane.
- Krok 6: Ustaw OAuth2 (uprawnienia bota)
Aby zaprosić bota na swój serwer, musisz wygenerować odpowiedni link zaproszenia.

Przejdź do sekcji OAuth2 w menu po lewej stronie.

# W OAuth2 URL Generator wybierz następujące zakresy:

bot w sekcji SCOPES.
Wybierz wymagane uprawnienia w sekcji BOT PERMISSIONS.
Minimum wybierz następujące uprawnienia:

- Read Messages
- Send Messages
- Connect (aby dołączyć do kanałów głosowych)
- Speak (aby mówić w kanałach głosowych)
Skopiuj wygenerowany URL i otwórz go w przeglądarce, aby zaprosić bota na swój serwer.

## Krok 7: Zabezpiecz swojego bota
Jeśli bot będzie publiczny, upewnij się, że używasz zmiennych środowiskowych lub plików konfiguracyjnych do przechowywania tokenu bota, aby zapobiec jego ujawnieniu.
Użyj dodatkowych mechanizmów ochrony, takich jak Two-Factor Authentication (2FA), aby zabezpieczyć konto swojego bota.
## Krok 8: Uruchom swojego bota
Po wygenerowaniu tokenu, użyj go w kodzie swojego bota (np. bot.run('YOUR_BOT_TOKEN')).
Uruchom bota na swoim serwerze, aby sprawdzić, czy działa poprawnie.
Użycie
Uruchom bota: Aby uruchomić bota, wystarczy uruchomić skrypt Pythona:
```bash
python bot.py
```
## 2. Komendy:
- !play <YouTube URL>: Dodaj piosenkę do kolejki i rozpocznij odtwarzanie.
- !add <YouTube URL>: Dodaj piosenkę do kolejki bez rozpoczynania odtwarzania.
- !skip: Pomijaj bieżącą piosenkę i przejdź do następnej w kolejce.
- !stop: Zatrzymaj muzykę i wyczyść kolejkę.
- !queue: Pokaż aktualną kolejkę piosenek.
- !777 <kwota_zakładu>: Graj w prostą grę losową z zakładem. Wygraj, jeśli wszystkie trzy symbole będą takie same.
## 3. Uprawnienia bota:
Upewnij się, że bot ma uprawnienia do dołączenia i mówienia na kanale głosowym oraz niezbędne uprawnienia do odczytu i wysyłania wiadomości.

## Licencja
Ten projekt jest licencjonowany na podstawie licencji MIT - szczegóły w pliku LICENSE.

## Uwagi
Upewnij się, że masz zainstalowaną bibliotekę ffmpeg, ponieważ jest wymagana do odtwarzania audio w Discordzie. Jeśli bot napotka problemy z pobieraniem audio z YouTube, upewnij się, że yt-dlp jest zainstalowane i zaktualizowane poprawnie.

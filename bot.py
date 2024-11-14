import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio
import os
import random
restart = False
# Tworzymy obiekt intents z wymaganymi uprawnieniami
intents = discord.Intents.default()
intents.message_content = True  # Pozwala botowi na odczytywanie treści wiadomości

# Tworzymy instancję bota z prefiksem komend i intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Globalna kolejka piosenek
song_queue = []
is_playing = False

# Funkcja do pobierania audio z YouTube
def download_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',  # Pobierz najlepszy dostępny format audio
            'outtmpl': 'downloads/%(id)s.%(ext)s',  # Określenie ścieżki zapisu
            'quiet': False,  # Aby wyświetlić proces pobierania
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            audio_filename = f"downloads/{info_dict['id']}.{info_dict['ext']}"
            title = info_dict.get('title', 'Unknown')  # Pobieranie tytułu utworu
            return audio_filename, title
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None, None

# Funkcja do odtwarzania audio w kanale głosowym
async def play_audio(ctx):
    global is_playing
    if not song_queue:
        await ctx.send("Kolejka jest pusta!")
        is_playing = False
        return

    # Ustawiamy is_playing na True, aby nie uruchamiać odtwarzania ponownie
    is_playing = True

    # Pobieramy informacje o pierwszej piosence z kolejki
    url, title, download_path = song_queue.pop(0)

    # Jeśli plik audio nie istnieje, spróbujemy go pobrać
    if not os.path.exists(download_path):
        download_path, title = download_audio(url)

    if not download_path:
        await ctx.send("Nie udało się pobrać pliku audio.")
        return

    # Wyświetlanie aktualnie odtwarzanej piosenki
    await ctx.send(f'Odtwarzam teraz: "{title}"')

    # Wyświetlanie następnej piosenki, jeśli istnieje
    if song_queue:
        _, next_title, _ = song_queue[0]
        await ctx.send(f'Następna piosenka: "{next_title}"')

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)

    # Jeśli bot już jest połączony, nie łączymy się ponownie
    if voice_client is None:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()

    # Odtwarzamy audio w jego oryginalnym formacie
    voice_client.play(
        discord.FFmpegPCMAudio(download_path),
        after=lambda e: asyncio.run_coroutine_threadsafe(on_audio_end(ctx, download_path), bot.loop)
    )

# Funkcja do obsługi końca piosenki i przejścia do następnej w kolejce
async def on_audio_end(ctx, download_path):
    global is_playing
    # Usuwamy plik audio po zakończeniu odtwarzania
    if os.path.exists(download_path):
        os.remove(download_path)
        print(f"Plik {download_path} został usunięty.")
    
    if song_queue:
        await play_audio(ctx)  # Odtwarzamy następną piosenkę
    else:
        is_playing = False
        # Rozłączamy bota z kanału głosowego
        voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
        if voice_client:
            await voice_client.disconnect()

# Komenda do dodania piosenki do kolejki i odtwarzania
@bot.command(name='play')
async def play(ctx, url):
    global is_playing

    # Pobieramy audio i tytuł
    download_path, title = download_audio(url)
    if download_path is None:
        await ctx.send("Nie udało się pobrać audio.")
        return

    # Dodajemy URL, tytuł i ścieżkę pobrania do kolejki
    song_queue.append((url, title, download_path))
    await ctx.send(f'Piosenka "{title}" została dodana do kolejki.')

    # Jeśli to pierwsza piosenka, zaczynamy odtwarzanie
    if not is_playing:
        await play_audio(ctx)

# Komenda do dodawania piosenki do kolejki bez odtwarzania
@bot.command(name='add')
async def add(ctx, url):
    download_path, title = download_audio(url)
    if download_path is None:
        await ctx.send("Nie udało się pobrać audio.")
        return

    song_queue.append((url, title, download_path))
    await ctx.send(f'Piosenka "{title}" została dodana do kolejki.')

# Komenda do pominięcia bieżącej piosenki
@bot.command(name='skip')
async def skip(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        await ctx.send("Pomijam bieżącą piosenkę...")
        voice_client.stop()  # Przejście do następnej piosenki uruchomi się w on_audio_end

# Komenda do zatrzymywania muzyki i wyczyszczenia kolejki
@bot.command(name='stop')
async def stop(ctx):
    global song_queue, is_playing
    
    # Pobieramy voice_client i zatrzymujemy odtwarzanie
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()  # Zatrzymanie aktualnie odtwarzanej piosenki
    
    # Odłączenie bota od kanału głosowego
    if voice_client:
        await voice_client.disconnect()
        await ctx.send("Zatrzymano muzykę i rozłączono z kanałem.")

    # Usunięcie wszystkich plików audio w kolejce
    for file_path, _ in song_queue:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Plik {file_path} został usunięty.")
    
    # Wyczyszczenie kolejki i zresetowanie flagi odtwarzania
    song_queue.clear()
    is_playing = False

# Komenda do pokazania kolejki
@bot.command(name='queue')
async def queue(ctx):
    if not song_queue:
        await ctx.send("Kolejka jest pusta!")
        return

    queue_str = "Aktualna kolejka utworów:\n"
    for idx, (_, title, _) in enumerate(song_queue, 1):
        queue_str += f"{idx}. {title}\n"
    
    await ctx.send(queue_str)


# Komenda do włączenia bota
@bot.event
async def on_ready():
    print(f'Bot {bot.user} jest gotowy do działania!')
# Funkcja do gry 777 (losowy wynik)
def play_777(bet_amount):
    # Możliwe symbole w grze 777
    symbols = ['🍒', '🍋', '🍊', '🍉', '🍓', '🍇', '🍍']

    # Losowanie trzech symboli (wynik spinu)
    result = [random.choice(symbols) for _ in range(3)]

    # Sprawdzanie, czy użytkownik wygrał (wszystkie symbole muszą być takie same)
    if len(set(result)) == 1:
        # Wygrana (3 identyczne symbole)
        return result, True
    else:
        # Przegrana (brak takich samych symboli)
        return result, False

# Komenda do rozpoczęcia gry 777
@bot.command(name='777')
async def play(ctx, bet: int):
    # Sprawdzamy, czy użytkownik podał odpowiednią kwotę
    if bet <= 0:
        await ctx.send("Podaj poprawną kwotę zakładu (większą niż 0).")
        return
    
    # Wywołanie funkcji do gry
    result, won = play_777(bet)

    # Wynik gry (co zostało wylosowane)
    result_string = " | ".join(result)
    
    # Odpowiedź do użytkownika
    if won:
        await ctx.send(f"Wynik: {result_string} 🎉🎉 Wygrałeś {bet * 2} monet!")
    else:
        await ctx.send(f"Wynik: {result_string} 😞 Niestety, przegrałeś {bet} monet.")
        

bot.run('Your_TOKEN')
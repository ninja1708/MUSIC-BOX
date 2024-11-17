import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio
import os
import json
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

song_queue = []
is_playing = False


# Funkcja do pobierania audio z YouTube
def download_audio(url, folder="downloads"):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{folder}/%(id)s.%(ext)s',
            'quiet': False,
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info_dict)
            audio_filename = f"{folder}/{info_dict['id']}.{info_dict['ext']}"
            title = info_dict.get('title', 'Unknown')
            return audio_filename, title
    except Exception as e:
        print(f"Error downloading audio: {e}")
        return None, None
        
@bot.command(name='queue')  # =========================================================================== Zamień nazwę ustawienia komendy
async def queue(ctx):
    if not song_queue:
        await ctx.send("Kolejka jest pusta!")
        return

    queue_str = "Aktualna kolejka utworów:\n"
    for idx, (_, title, _) in enumerate(song_queue, 1):
        queue_str += f"{idx}. {title}\n"

    await ctx.send(queue_str)

# Funkcja do usuwania pliku po odtworzeniu
def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


# Funkcja do odtwarzania audio
async def play_audio(ctx):
    global is_playing

    if not song_queue:
        await ctx.send("Kolejka jest pusta!")
        is_playing = False
        return

    is_playing = True
    url, title, path = song_queue.pop(0)

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client is None:
        voice_channel = ctx.author.voice.channel
        voice_client = await voice_channel.connect()

    if not os.path.exists(path):
        path, title = download_audio(url)

    if path:
        voice_client.play(
            discord.FFmpegPCMAudio(path),
            after=lambda e: asyncio.run_coroutine_threadsafe(on_audio_end(ctx, path), bot.loop)
        )
        await ctx.send(f"Odtwarzam teraz: {title}")
    else:
        await ctx.send("Nie udało się odtworzyć utworu.")


async def on_audio_end(ctx, path):
    global is_playing
    if path.startswith("downloads"):
        delete_file(path)

    if song_queue:
        await play_audio(ctx)
    else:
        is_playing = False


@bot.command(name="play")
async def play(ctx, url):
    global is_playing

    download_path, title = download_audio(url)
    if download_path:
        song_queue.append((url, title, download_path))
        await ctx.send(f"Piosenka '{title}' została dodana do kolejki.")
        if not is_playing:
            await play_audio(ctx)
    else:
        await ctx.send("Nie udało się pobrać audio.")


@bot.command(name="skip")
async def skip(ctx):
    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await ctx.send("Pomijam utwór...")
    else:
        await ctx.send("Nie odtwarzam żadnej muzyki.")


@bot.command(name="stop")
async def stop(ctx):
    global song_queue, is_playing
    song_queue.clear()
    is_playing = False

    voice_client = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice_client and voice_client.is_playing():
        voice_client.stop()
        await voice_client.disconnect()
        await ctx.send("Zatrzymano odtwarzanie.")


# Obsługa playlist
@bot.command(name="addplaylist")
async def addplaylist(ctx, playlist_name: str, url: str):
    folder_path = f"playlists/{playlist_name}"
    os.makedirs(folder_path, exist_ok=True)

    download_path, title = download_audio(url, folder=folder_path)
    if not download_path:
        await ctx.send("Nie udało się pobrać audio.")
        return

    metadata_path = os.path.join(folder_path, "metadata.json")
    if not os.path.exists(metadata_path):
        with open(metadata_path, "w") as file:
            json.dump({}, file)

    with open(metadata_path, "r") as file:
        metadata = json.load(file)

    metadata[os.path.basename(download_path)] = title

    with open(metadata_path, "w") as file:
        json.dump(metadata, file)

    await ctx.send(f"Piosenka '{title}' została dodana do playlisty '{playlist_name}'.")


@bot.command(name="playlist")
async def playlist(ctx, playlist_name=None):
    if playlist_name is None:
        playlists = [f for f in os.listdir("playlists") if os.path.isdir(os.path.join("playlists", f))]
        if playlists:
            await ctx.send("Dostępne playlisty:\n" + "\n".join(playlists))
        else:
            await ctx.send("Brak dostępnych playlist.")
        return

    folder_path = f"playlists/{playlist_name}"
    metadata_path = os.path.join(folder_path, "metadata.json")

    if not os.path.exists(folder_path) or not os.path.exists(metadata_path):
        await ctx.send(f"Playlista '{playlist_name}' nie istnieje.")
        return

    with open(metadata_path, "r") as file:
        metadata = json.load(file)

    if not metadata:
        await ctx.send(f"Playlista '{playlist_name}' jest pusta.")
        return

    global song_queue
    for filename, title in metadata.items():
        song_queue.append((None, title, os.path.join(folder_path, filename)))

    await ctx.send(f"Załadowano playlistę '{playlist_name}' z {len(metadata)} utworami.")
    if not is_playing:
        await play_audio(ctx)

@bot.command(name="HELP")
async def help_command(ctx):
    help_message = """
**Lista dostępnych komend:**

1. **!play <URL>** - Dodaje utwór z podanym URL (YouTube) do kolejki i zaczyna odtwarzanie.
2. **!skip** - Pomija aktualnie odtwarzany utwór.
3. **!stop** - Zatrzymuje odtwarzanie muzyki, czyści kolejkę i rozłącza bota z kanału.
4. **!addplaylist <nazwa_playlisty> <URL>** - Tworzy playlistę z podaną nazwą (jeśli nie istnieje) i dodaje do niej utwór z YouTube.
5. **!playlist [nazwa_playlisty]** - Odtwarza playlistę o podanej nazwie lub wyświetla listę dostępnych playlist, jeśli nazwa nie jest podana.
6. **!HELP** - Wyświetla tę listę komend.
7. **!join** - Dołącza do ciebie na serwer.
6. **!leave** - Wychodzi z kanału.
6. **!clear** - czyści download.


Jeśli potrzebujesz dodatkowej pomocy, możesz skontaktować się z administratorem bota ninja1708a#1053.
    """
    try:
        await ctx.author.send(help_message)
        await ctx.send("Lista komend została wysłana na Twoją prywatną wiadomość!")
    except discord.Forbidden:
        await ctx.send("Nie mogę wysłać wiadomości prywatnej. Upewnij się, że masz włączone DM od członków serwera.")

@bot.command(name="clear")
async def clear_downloads(ctx):
    """Czyści folder 'downloads'."""
    downloads_folder = "downloads"
    if os.path.exists(downloads_folder) and os.path.isdir(downloads_folder):
        deleted_files = []
        for filename in os.listdir(downloads_folder):
            file_path = os.path.join(downloads_folder, filename)
            try:
                os.remove(file_path)
                deleted_files.append(filename)
            except Exception as e:
                await ctx.send(f"Nie udało się usunąć pliku: {filename}. Błąd: {e}")
        
        if deleted_files:
            await ctx.send(f"Folder 'downloads' został wyczyszczony. Usunięto pliki: {', '.join(deleted_files)}.")
        else:
            await ctx.send("Folder 'downloads' jest już pusty.")
    else:
        await ctx.send("Folder 'downloads' nie istnieje lub jest już pusty.")

@bot.event
async def on_ready():
    print(f"Bot {bot.user} jest gotowy do działania!")
    
@bot.command(name="join")
async def join(ctx):
    """Dołącza do kanału głosowego użytkownika, który wywołał komendę."""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Dołączyłem do kanału: {channel.name}")
    else:
        await ctx.send("Nie jesteś na żadnym kanale głosowym!")

@bot.command(name="leave")
async def leave(ctx):
    """Opuszcza kanał głosowy, jeśli jest na jakimś połączony."""
    if ctx.voice_client:  # Sprawdza, czy bot jest na kanale głosowym
        await ctx.voice_client.disconnect()
        await ctx.send("Opuszczam kanał.")
    else:
        await ctx.send("Nie jestem na żadnym kanale głosowym.")

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
@bot.command( name='777')  # =========================================================================== Zamień nazwę ustawienia komendy
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

bot.run('YOUR_TOKEN')

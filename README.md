Discord Music Bot
A simple music bot for Discord written in Python using discord.py and yt-dlp. It allows users to play music from YouTube, manage queues, skip tracks, and stop the bot from playing music. Additionally, it includes a fun "777" game feature where users can place bets and spin virtual fruit symbols.

Features
Music Playback: Play audio from YouTube links directly in a voice channel.
Queue Management: Add songs to a queue and skip or stop songs.
777 Game: Play a simple slot machine game with bets and rewards.
Bot Commands: Interact with the bot through a variety of commands to control playback and play games.
Requirements
Python 3.8 or higher
Required Python packages:
discord.py
yt-dlp
ffmpeg (for audio processing)
Installation
Clone the repository:

bash
Skopiuj kod
git clone https://github.com/your-username/discord-music-bot.git
cd discord-music-bot
Create a virtual environment (optional but recommended):

bash
Skopiuj kod
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash
Skopiuj kod
pip install -r requirements.txt
Download and install FFmpeg:

You can download FFmpeg from https://ffmpeg.org/download.html. Make sure to add FFmpeg to your system's PATH variable.

Set up your Discord bot token:

Replace the bot.run('YOUR_TOKEN') in the script with your actual bot token. To create a bot, visit the Discord Developer Portal, create an application, and generate a bot token.

Usage
Run the bot:

To start the bot, simply run the Python script:

bash
Skopiuj kod
python bot.py
Commands:

!play <YouTube URL>: Add a song to the queue and start playing it.
!add <YouTube URL>: Add a song to the queue without starting playback.
!skip: Skip the current song and play the next one in the queue.
!stop: Stop the music and clear the queue.
!queue: Show the current song queue.
!777 <bet_amount>: Play a simple slot game with a bet. Win if all three symbols match.
Bot Permissions:

Make sure the bot has permission to join and speak in the voice channel, and the necessary permissions to read and send messages.

Example Commands
!play https://www.youtube.com/watch?v=dQw4w9WgXcQ
!add https://www.youtube.com/watch?v=dQw4w9WgXcQ
!skip
!stop
!queue
!777 10
License
This project is licensed under the MIT License - see the LICENSE file for details.

Uwagi
Upewnij się, że masz zainstalowaną bibliotekę ffmpeg, ponieważ jest ona wymagana do odtwarzania audio w Discordzie.
Jeśli bot napotka problem z pobraniem pliku audio z YouTube, sprawdź, czy yt-dlp jest poprawnie zainstalowane i zaktualizowane.
Jeśli chcesz, aby README.md był bardziej szczegółowy lub zawierał dodatkowe informacje, daj znać!

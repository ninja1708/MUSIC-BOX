# Discord Music Bot

A simple music bot for Discord written in Python using `discord.py` and `yt-dlp`. It allows users to play music from YouTube, manage queues, skip tracks, and stop the bot from playing music. Additionally, it includes a fun "777" game feature where users can place bets and spin virtual fruit symbols.

## Features

- **Music Playback**: Play audio from YouTube links directly in a voice channel.
- **Queue Management**: Add songs to a queue and skip or stop songs.
- **777 Game**: Play a simple slot machine game with bets and rewards.
- **Bot Commands**: Interact with the bot through a variety of commands to control playback and play games.

## Requirements

- Python 3.8 or higher
- Required Python packages:
  - `discord.py`
  - `yt-dlp`
  - `ffmpeg` (for audio processing)

## Installation

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/discord-music-bot.git
cd discord-music-bot
```
## Installation

### 2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
### 3. Install dependencies:
```bash
pip install -r requirements.txt
```
### 4. Download and install FFmpeg:
```bash
sudo apt update
sudo apt upgrade
sudo apt install ffmpeg
```
You can download FFmpeg from here. Make sure to add FFmpeg to your system's PATH variable.

### 5. Set up your Discord bot token:
Replace the bot.run('YOUR_TOKEN') in the script with your actual bot token. To create a bot, visit the Discord Developer Portal, create an application, and generate a bot token.

### Usage
1. Run the bot:
To start the bot, simply run the Python script:

```bash
python bot.py
```
## 2. Commands:
!play <YouTube URL>: Add a song to the queue and start playing it.
!add <YouTube URL>: Add a song to the queue without starting playback.
!skip: Skip the current song and play the next one in the queue.
!stop: Stop the music and clear the queue.
!queue: Show the current song queue.
!777 <bet_amount>: Play a simple slot game with a bet. Win if all three symbols match.
## 3. Bot Permissions:
Make sure the bot has permission to join and speak in the voice channel, and the necessary permissions to read and send messages.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Notes
Make sure you have the ffmpeg library installed, as it is required for audio playback in Discord.
If the bot encounters issues with downloading audio from YouTube, ensure that yt-dlp is installed and updated properly.


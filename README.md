# Discord Music Bot

A simple music bot for Discord written in Python using `discord.py` and `yt-dlp`. It allows users to play music from YouTube, manage queues, skip tracks, and stop the bot from playing music. Additionally, it includes a fun "777" game feature where users can place bets and spin virtual fruit symbols.

## Features

- **Music Playback**: Play audio from YouTube links directly in a voice channel.
- **Queue Management**: Add songs to a queue and skip or stop songs.
- **777 Game**: Play a simple slot machine game with bets and rewards.
- **Bot Commands**: Interact with the bot through a variety of commands to control playback and play games.

## FAST INSTALL Requirements
```bash
chmod +x install.bash
sudo ./install.bash
```
## Requirements

- Python 3.10
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
# Bot Settings in Discord Developer Portal

To configure your bot in the Discord Developer Portal, follow these steps:

#### Step 1: Go to the Discord Developer Portal

1. Log in to your Discord account.
2. Go to the [Discord Developer Portal](https://discord.com/developers/applications).

#### Step 2: Create a New Application

1. Click the **New Application** button.
2. Enter a name for your application (e.g., "MyMusicBot") and click **Create**.

#### Step 3: Create the Bot

1. In the left menu, click **Bot**.
2. Click **Add Bot** and confirm by clicking **Yes, do it!**.
3. Your bot will now be created, and here you can change its name, profile picture, and other settings.

#### Step 4: Copy the Bot Token

1. On the bot settings page, under the **Bot** section, you will see the **TOKEN** field.
2. Click the **Copy** button next to **Token**.
3. The token is crucial for running the bot in your code — keep it in a secure place.

#### Step 5: Set Bot Permissions

For the bot to work correctly, you need to assign it the appropriate permissions.

1. Under the **Bot** section, scroll down to **Privileged Gateway Intents**.
2. Enable the following permissions:
   - **MESSAGE CONTENT INTENT** – Allows the bot to read message content (important if the bot uses commands).
   - **SERVER MEMBERS INTENT** – Allows the bot to manage server members if needed.

#### Step 6: Set OAuth2 (Bot Permissions)

To invite the bot to your server, you need to generate the appropriate invite link.

1. Go to the **OAuth2** section in the left menu.
2. In the **OAuth2 URL Generator**, select the following scopes:
   - **bot** under **SCOPES**.
   - Select the required permissions under **BOT PERMISSIONS**.

   At a minimum, choose the following permissions:
   - **Read Messages**
   - **Send Messages**
   - **Connect** (to join voice channels)
   - **Speak** (to speak in voice channels)

3. Copy the generated URL and open it in your browser to invite the bot to your server.

#### Step 7: Secure Your Bot

1. If the bot is going to be public, make sure to use environment variables or configuration files to store your bot token, preventing it from being exposed.
2. Use additional protection mechanisms, such as [Two-Factor Authentication (2FA)](https://discord.com/verify), to secure your bot's account.

#### Step 8: Run Your Bot

1. After generating the token, use it in your bot's code (e.g., `bot.run('YOUR_BOT_TOKEN')`).
2. Run your bot on your server to check if it's working properly.


## Usage
1. Run the bot:
To start the bot, simply run the Python script:

```bash
python3.10 bot.py
```
## 2. Commands:
- !play <YouTube URL>: Add a song to the queue and start playing it.
- !add <YouTube URL>: Add a song to the queue without starting playback.
- !skip: Skip the current song and play the next one in the queue.
- !stop: Stop the music and clear the queue.
- !queue: Show the current song queue.
- !leave: bot leave a channel
- !join: bot join a channel
- !clear: clear queue and folder downloads
- !777 <bet_amount>: Play a simple slot game with a bet. Win if all three symbols match.
## 3. Bot Permissions:
Make sure the bot has permission to join and speak in the voice channel, and the necessary permissions to read and send messages.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Notes
Make sure you have the ffmpeg library installed, as it is required for audio playback in Discord.
If the bot encounters issues with downloading audio from YouTube, ensure that yt-dlp is installed and updated properly.


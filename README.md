# **BASSIPY**

---

## INFO
Bassipy is a self-hosted, easy to use Discord bot for playing music in voice channels.
It is written in Python and uses `discord.py` and `yt-dlp`.  

## COMMANDS
Bassipy features some commands which are used by typing the prefix(!) following with the command(eg. !play).  

`PLAY`  
> Plays a song from Youtube or adds it to queue(eg. !play https://www.youtube.com/watch?v=dQw4w9WgXcQ)  

`SKIP`  
> Skips current song  

`SEARCH`  
> Gets 5 results for an argument(eg. !search rap)  

`QUEUE`  
> Shows songs in queue  

---

## HOW TO GET BOT TOKEN
1. Log into [DISCORD DEVELOPER PORTAL](https://discord.com/developers/applications)  
2. Make a new application/bot.  
3. Under the bot tab you will find your token.  
> [!WARNING]
> Never share your bot token!  

## HOW TO USE
### Prepare environment
1. Clone the repository
 `git clone https://github.com/n1xerii/bassipy.git`
2. Go inside the cloned folder
 `cd bassipy`
3. Create a new Python environment (I recommend using conda)
 `conda create -n bassipy python=3.11` or `python -m venv bassipy`
4. Activate the environment
 `conda activate bassipy` or `venv\Scripts\activate.bat`
5. Install the requirements
 `pip install -r requirements.txt`

### Bot data
1. Add a new file "bot_data.py"
2. Open the file and add your Discord bot token `my_token = "yourtokenhere"`
3. Save the file and exit
> [!WARNING]
> Never share your bot token!

### Install deno
1. Install node.js for Windows (https://nodejs.org/en/download). For Linux use your package manager
2. Run `npm install deno` in your terminal(CMD or Powershell on Windows)

### Running the bot
1. Open your terminal(CMD or Powershell on Windows)
2. Navigate to your bassipy repository `cd path/to/folder`
3. Run `python run_bot.py` and the bot should start!

---
 

# **BASSIPY**

---

## INFO
Bassipy is a local Discord bot made for playing music in voice channels.  
It uses Python with "yt-dlp" and "discord.py" packages.  
You can currently use commands "play", "skip" and "search" by typing the prefix(!) and then the command(eg. !search).  
The PLAY command takes a youtube link and plays it(eg. !play https://www.youtube.com/watch?v=dQw4w9WgXcQ).  
The SEARCH command takes an argument and searches for top 5 results of that argument(eg. !search rap).  
The bot does not yet feature a queue and only plays one song at a time.

---

## HOW TO USE
### Setting up environment
1. Create a new Python environment with venv or conda(I recommend conda)  
 `conda create -n bassipy python=3.10`
2. Activate the environment  
 `conda activate bassipy`
3. Head to the location of your repo  
 `cd path\to\your\folder`
4. Install requirements  
 `pip install -r requirements.txt`

### Running the bot
1. Add "bot_token.py" file into the projects root folder
2. Add `my_token = 'yourtokenhere'` into "bot_token.py"
4. Run a CMD instance in the root folder
6. Run `python main.py` command in the CMD

---
 

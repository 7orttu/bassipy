import os
import asyncio
import discord
import logging
import yt_dlp as youtube_dl
from discord.ext import commands
from discord import FFmpegOpusAudio
from bot_token import my_token
import data
from bot_instance import bot

# BASIC BOOLEANS
is_playing = False    # is_playing is used to check whether a track is currently being played
is_searching = False  # isSeacrhing is used to check whether a search is already running

# PLAY COMMAND
# | Plays any audio from Youtube in a Discord Voice Channel
async def runplay(ctx, url: str):
    global is_playing

    try:
        # If user is present in a voice channel, return/stop execution
        if not ctx.author.voice:
            await ctx.send("Join a voice channel first!")
            return

        # Users voice channel
        vc_to_join = ctx.author.voice.channel

        # Connect to the voice channel
        data.vc_conn = await vc_to_join.connect()

        # Set is_playing to true to prevent running the play command again during playback
        is_playing = True

        # Prepare file
        with youtube_dl.YoutubeDL(data.ydl_options) as ydl:
            infoDict = ydl.extract_info(url, download=True)
            audioFile = ydl.prepare_filename(infoDict)

        # Check whether file is found before playing, if not, return/stop execution
        if not os.path.isfile(audioFile):
            ctx.send(f"Audio file not found: {audioFile}")
            return

        # Prepare audio source
        audio_source = FFmpegOpusAudio(audioFile, executable=data.ffmpeg)

        # Play audio source in voice channel
        data.vc_conn.play(audio_source)

        # Keep playing the song until it ends
        while data.vc_conn.is_playing():
            await asyncio.sleep(1)

        # Delete audio file
        os.remove(audioFile)

        # Set is_playing to false to allow running play command again
        is_playing = False

        # Disconnect from voice channel
        await data.vc_conn.disconnect()
        await ctx.send("Finished playing audio.")

    # If any errors happen, send message to console and to the channel where user ran the command from
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        await ctx.send(f"An error occurred: {e}")
        return


# SKIP COMMAND
# | Skips the currently playing video/song if one is playing
async def runskip(ctx):
    global is_playing

    # If no audio is playing, there is nothing to skip
    if not is_playing:
        await ctx.send("No audio is currently playing!")
        return

    # If audio is playing, skip the currently playing song by stopping the connection and disconnecting
    if (data.vc_conn is not None):
        data.vc_conn.stop()
        await ctx.send("Song skipped!")
        await data.vc_conn.disconnect()    # Disconnect from voice channel

    # Set is_playing to false
    is_playing = False


# SEARCH COMMAND
# | Searches 5 top results for "arg" from Youtube and provides 5 buttons to select any of them to play
async def runsearch(ctx, *, arg):
    global is_searching
    
    try:
        await ctx.send("Searching... Please wait...")

        is_searching = True  # Searching to true
        
        # Call "ytsearch5" from ytdlp and populate "videos" with the result
        with youtube_dl.YoutubeDL(data.ydl_options) as ydl:
            videos = ydl.extract_info(f"ytsearch5:{arg}", download=False)   # Returns a dictionary with results
            
        # Ensure that "videos" is not None or empty
        if videos is None or "entries" not in videos:
            await ctx.send("No results found.")
            return

        videos = videos["entries"][:5]

        # Discord view
        view = discord.ui.View()

        # Loop through results in "videos"
        for index, vid in enumerate(videos):
            vidTitle = vid['title']
            vidUrl = vid['webpage_url']

            # Construction of buttons
            button = discord.ui.Button(
                label=f"{index + 1}.{vidTitle[:40]}",   # Button text
                style=discord.ButtonStyle.primary   # Button style
            )

            # Callback after button is clicked
            async def callback(interaction, url=vidUrl):
                global is_searching
                
                await ctx.send(f"**SELECTED VIDEO**: {url}")
                await runplay(ctx, url)    # Call "play" command to play the selected result/video
                is_searching = False

            button.callback = callback

            # Add button to view
            view.add_item(button)

        await ctx.send("**SELECT VIDEO**", view=view)
        is_searching = False
    except Exception as e:
        await ctx.send(f"An error occurred while searching. Error: {e}")
        return
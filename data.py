import os
import asyncio
import discord
import logging
import yt_dlp as youtube_dl
from discord.ext import commands
from discord import FFmpegOpusAudio

# FFMPEG
ffmpeg = os.path.join(os.path.dirname(__file__), 'ffmpeg', 'ffmpeg.exe')

# LOGGING
logging.basicConfig(level=logging.ERROR, filename="bot_errors.log")    # Logging

# CONNECTION
vc_conn = None

# YOUTUBE DOWNLOAD OPTIONS
ydl_options = {
    'format': 'bestaudio/best',
    'quiet': True,
    'outtmpl': 'downloads/%(id)s.%(ext)s',
}
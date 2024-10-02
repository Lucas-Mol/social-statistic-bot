import os
from domain.youtube.services import youtube_channel_builder, youtube_printer

def generate_txt(youtube_api_key, youtube_channel_id):
    youtube_channel = youtube_channel_builder.get_youtube_channel(youtube_api_key, youtube_channel_id)
    youtube_printer.generate_txt(youtube_channel)

def generate_sheets(youtube_api_key, youtube_channel_id):
    youtube_channel = youtube_channel_builder.get_youtube_channel(youtube_api_key, youtube_channel_id)
    youtube_printer.generate_sheets(youtube_channel)

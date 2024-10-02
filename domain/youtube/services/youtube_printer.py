from domain.youtube.objects.youtube_channel import Youtube_Channel
from domain.youtube.services.printers import youtube_text_printer, youtube_sheet_printer

OUTPUT_FOLDER_PATH = "./output"

def generate_txt(youtube_channel: Youtube_Channel):
    youtube_text_printer.print(youtube_channel, OUTPUT_FOLDER_PATH)

def generate_sheets(youtube_channel: Youtube_Channel):
    youtube_sheet_printer.print(youtube_channel, OUTPUT_FOLDER_PATH)
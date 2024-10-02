from pathlib import Path
from domain.instagram.services import instagram_printer, instagram_profile_builder

def generate_txt(instagram_api_key):
    instagram_profile = instagram_profile_builder.get_instagram_profile(instagram_api_key)
    instagram_printer.generate_txt(instagram_profile)

def generate_sheets(instagram_api_key):
    instagram_profile = instagram_profile_builder.get_instagram_profile(instagram_api_key)
    instagram_printer.generate_sheets(instagram_profile)

from domain.instagram.objects.instagram_profile import Instagram_Profile
from domain.instagram.services.printers import instagram_text_printer, instagram_sheet_printer

OUTPUT_FOLDER_PATH = "./output"


def generate_txt(instagram_profile: Instagram_Profile):
    instagram_text_printer.print(instagram_profile, OUTPUT_FOLDER_PATH)

def generate_sheets(instagram_profile: Instagram_Profile):
    instagram_sheet_printer.print(instagram_profile, OUTPUT_FOLDER_PATH)
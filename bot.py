from dotenv import load_dotenv
import os, argparse
from domain.instagram.services import instagram_services
from domain.youtube.services import youtube_services

load_dotenv()

youtube_api_key = os.getenv('YOUTUBE_API_KEY')
youtube_channel_id = os.getenv('YOUTUBE_CHANNEL_ID')
instagram_api_key = os.getenv('INSTAGRAM_API_KEY')

def main():
    parser = argparse.ArgumentParser(description="Escolha qual função executar.")
    parser.add_argument("funcao", choices=["yt_text", "ig_text", "yt_ig_text", "yt_sheets", "ig_sheets", "yt_ig_sheets"], help="Função a ser executada")

    args = parser.parse_args()

    if args.funcao == "yt_text":
        youtube_services.generate_txt(youtube_api_key, youtube_channel_id)
    elif args.funcao == "ig_text":
        instagram_services.generate_txt(instagram_api_key)
    elif args.funcao == "yt_ig_text":
        youtube_services.generate_txt(youtube_api_key, youtube_channel_id)
        instagram_services.generate_txt(instagram_api_key)
    elif args.funcao == "yt_sheets":
        youtube_services.generate_sheets(youtube_api_key, youtube_channel_id)
    elif args.funcao == "ig_sheets":
        instagram_services.generate_sheets(instagram_api_key)
    elif args.funcao == "yt_ig_sheets":
        youtube_services.generate_sheets(youtube_api_key, youtube_channel_id)
        instagram_services.generate_sheets(instagram_api_key)
        


if __name__ == "__main__":
    main()
from typing import List
from domain.youtube.objects.youtube_playlist import Youtube_Playlist

class Youtube_Channel:
    def __init__(self, username: str, subs_count: int, view_count: int, video_count: int, playlists: List[Youtube_Playlist]):
        self.username = username
        self.subs_count = subs_count
        self.view_count = view_count
        self.video_count = video_count
        self.playlists = playlists
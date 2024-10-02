from typing import List
from domain.youtube.objects.youtube_video import Youtube_Video

class Youtube_Playlist:
    def __init__(self, id: str, name: str, views: int, likes: int, comments: int, videos: List[Youtube_Video]):
        self.id = id
        self.name = name
        self.views = views
        self.likes = likes
        self.comments = comments
        self.videos = videos
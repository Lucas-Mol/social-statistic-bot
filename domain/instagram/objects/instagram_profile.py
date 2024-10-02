from typing import List
from domain.instagram.objects.instagram_post import Instagram_Post

class Instagram_Profile:
    def __init__(self, username: str, followers_count: int, media_count: int, total_likes: int, posts: List[Instagram_Post]):
        self.username = username
        self.followers_count = followers_count
        self.media_count = media_count
        self.total_likes = total_likes
        self.posts = posts
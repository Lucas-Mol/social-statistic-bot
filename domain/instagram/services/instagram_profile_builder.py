import requests
from typing import List
from domain.instagram.objects.instagram_profile import Instagram_Profile
from domain.instagram.objects.instagram_post import Instagram_Post

BASE_URL = 'https://graph.instagram.com/me'

def get_instagram_profile(api_key) -> Instagram_Profile:
    url = f"{BASE_URL}?fields=username,media_count,followers_count&access_token={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        username = data["username"]
        followers_count = data["followers_count"]
        media_count = data["media_count"]

        posts = _get_posts(api_key)

        total_likes = 0

        for post in posts:
            total_likes += post.likes

        return Instagram_Profile(username, followers_count, media_count, total_likes, posts)
    else:
        return f"Error: {response.status_code}"
    
def _get_posts(api_key):
    next_url = f'{BASE_URL}/media?fields=id,caption,like_count,comments_count&access_token={api_key}'
    posts: List[Instagram_Post] = []
    
    while next_url:
        response = requests.get(next_url)
        data = response.json()
        
        if 'data' in data:
            for item in data['data']:
                name = item['caption']
                likes = int(item['like_count'])
                comments = int(item['comments_count'])

                posts.append(Instagram_Post(name, likes, comments))
        
        if 'paging' in data and 'next' in data['paging']:
            next_url = data['paging']['next']
        else:
            next_url = None
    
    return posts
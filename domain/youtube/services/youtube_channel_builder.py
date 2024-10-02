import requests
from typing import List
from domain.youtube.objects.youtube_channel import Youtube_Channel
from domain.youtube.objects.youtube_playlist import Youtube_Playlist
from domain.youtube.objects.youtube_video import Youtube_Video

BASE_URL = "https://www.googleapis.com/youtube/v3"


def get_youtube_channel(api_key, channel_id) -> Youtube_Channel:
    url = f"{BASE_URL}/channels?part=snippet,statistics&id={channel_id}&key={api_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        username = data["items"][0]["snippet"]["title"]
        subs_count = data["items"][0]["statistics"]["subscriberCount"]
        view_count = data["items"][0]["statistics"]["viewCount"]
        video_count = data["items"][0]["statistics"]["videoCount"]

        playlists = _get_channel_playlist(api_key, channel_id)

        return Youtube_Channel(username, subs_count, view_count, video_count, playlists)
    else:
        return f"Error: {response.status_code}"
    
def _get_channel_playslist_ids(api_key, channel_id) -> List[str]:
    url = f"{BASE_URL}/playlists?part=snippet&channelId={channel_id}&key={api_key}&maxResults=50"
    playlists_ids = []

    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            playlists_ids += [(item['id'], item['snippet']['title']) for item in data['items']]
            url = data.get('nextPageToken')
            if url:
                url = f"{BASE_URL}/playlists?part=snippet&channelId={channel_id}&key={api_key}&maxResults=50&pageToken={url}"
        else:
            return f"Error: {response.status_code}"
    
    return playlists_ids


def _get_channel_playlist(api_key, channel_id):
    playlist_ids = _get_channel_playslist_ids(api_key,channel_id)
    playlists: List[Youtube_Playlist] = []

    for playlist_id, playlist_name in playlist_ids:
        videos_ids = _get_video_ids_from_playlist(api_key, playlist_id)
        videos: List[Youtube_Video] = []

        videos += _get_videos(api_key, videos_ids)

        playlist_total_views = 0
        playlist_total_likes = 0
        playlist_total_comments = 0

        for video in videos:
            playlist_total_views += video.views
            playlist_total_likes += video.likes
            playlist_total_comments += video.comments

        playlists.append(Youtube_Playlist(playlist_id, playlist_name, playlist_total_views, playlist_total_likes, playlist_total_comments, videos))
    
    return playlists


def _get_video_ids_from_playlist(api_key, playlist_id):
    url = f"{BASE_URL}/playlistItems?part=contentDetails&playlistId={playlist_id}&key={api_key}&maxResults=50"
    video_ids = []
    
    while url:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            video_ids += [item['contentDetails']['videoId'] for item in data['items']]
            url = data.get('nextPageToken')
            if url:
                url = f"https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&playlistId={playlist_id}&key={api_key}&maxResults=50&pageToken={url}"
        else:
            return f"Error: {response.status_code}"
    
    return video_ids

def _get_videos(api_key, video_ids):
    videos: List[Youtube_Video] = []
    
    for i in range(0, len(video_ids), 50):
        ids = ",".join(video_ids[i:i+50])
        url = f"{BASE_URL}/videos?part=snippet,statistics&id={ids}&key={api_key}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            for item in data['items']:
                name = item['snippet']['title']
                views = int(item['statistics'].get('viewCount', 0))
                likes = int(item['statistics'].get('likeCount', 0))
                comments = int(item['statistics'].get('commentCount', 0))

                videos.append(Youtube_Video(name, likes, views, comments))
        else:
            return f"Error: {response.status_code}"
    
    return videos

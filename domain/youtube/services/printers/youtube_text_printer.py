import os
from domain.youtube.objects.youtube_channel import Youtube_Channel

FILE_NAME= '/youtube_statistics.txt'

def print(youtube_channel: Youtube_Channel, path):
    content_lines = _build_content_lines(youtube_channel)
    content = '\n'.join(content_lines)

    _write_file(content, path)


def _build_content_lines(youtube_channel: Youtube_Channel) -> str:
    content_lines = []

    content_lines.append('*YOUTUBE*')
    content_lines.append('')
    content_lines.append('Inscritos: ' + youtube_channel.subs_count)
    content_lines.append('Total vídeos: ' + youtube_channel.video_count)
    content_lines.append('Total visualizações: ' + youtube_channel.view_count)
    content_lines.append('')
    content_lines.append('----')
    content_lines.append('')
    for playlist in youtube_channel.playlists:
        content_lines.append('*Playlist: ' + playlist.name + '*')
        content_lines.append('Total de visualizações: ' + str(playlist.views))
        content_lines.append('Total de curtidas: ' + str(playlist.likes))
        content_lines.append('Total de comentários: ' + str(playlist.comments))
        content_lines.append('Vídeos: ')
        content_lines.append('')
        for video in playlist.videos:
            content_lines.append('- Nome: ' + video.name)
            content_lines.append('- Curtidas: ' + str(video.likes))
            content_lines.append('- Visualizações: ' + str(video.views))
            content_lines.append('- Comentários: ' + str(video.comments))
            content_lines.append('')
    
    return content_lines

def _write_file(content, path):
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + FILE_NAME, 'w') as file:
        file.write(content)
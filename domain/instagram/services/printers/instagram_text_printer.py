import os
from domain.instagram.objects.instagram_profile import Instagram_Profile

FILE_NAME = '/instagram_statistics.txt'

def print(instagram_profile: Instagram_Profile, path):
    content_lines = _build_content_lines(instagram_profile)
    content = '\n'.join(content_lines)

    _write_file(content, path)

def _build_content_lines(instagram_profile: Instagram_Profile):
    content_lines = []

    content_lines.append('*INSTAGRAM*')
    content_lines.append('')
    content_lines.append('Seguidores: ' + str(instagram_profile.followers_count))
    content_lines.append('Quantidade de posts: ' + str(instagram_profile.media_count))
    content_lines.append('Total de curtidas: ' + str(instagram_profile.total_likes))
    content_lines.append('')
    content_lines.append('----')
    for post in instagram_profile.posts:
        content_lines.append('*Post: ' + post.name + '*')
        content_lines.append('- Curtidas: ' + str(post.likes))
        content_lines.append('- Comentários: ' + str(post.comments))
        content_lines.append('')

    return content_lines

def _write_file(content, path):
    if not os.path.exists(path):
        os.makedirs(path)

    with open(path + FILE_NAME, 'w') as file:
        file.write(content)
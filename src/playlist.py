import os
import datetime
import re
from googleapiclient.discovery import build

def parse_duration(duration_string: str) -> datetime.timedelta:
    """
    Преобразует строку продолжительности YouTube (ISO 8601) в объект timedelta.
    Например, 'PT1H43M39S' преобразуется в datetime.timedelta(hours=1, minutes=43, seconds=39).

    :param duration_string: Строка продолжительности YouTube (например, 'PT1H43M39S')
    :return: Объект timedelta с соответствующей продолжительностью
    """
    duration_regex = re.compile(r'PT((\d+)H)?((\d+)M)?((\d+)S)?')
    hours, minutes, seconds = duration_regex.match(duration_string).groups()[1::2]
    return datetime.timedelta(hours=int(hours or 0), minutes=int(minutes or 0), seconds=int(seconds or 0))

class Video:
    """
    Класс, представляющий видео на YouTube.
    """
    def __init__(self, title: str, url: str, duration: datetime.timedelta, likes: int):
        self.title = title  # Название видео
        self.url = url  # Ссылка на видео
        self.duration = duration  # Продолжительность видео, представленная объектом timedelta
        self.likes = likes  # Количество лайков у видео

class PlayList:
    """
    Класс, представляющий плейлист на YouTube.
    """
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id  # id плейлиста на YouTube
        self.title = None  # Название плейлиста
        self.url = None  # Ссылка на плейлист
        self.videos = []  # Список видеороликов в плейлисте
        self.api_key = os.environ.get("YT_API_KEY")  # Ключ API

        # Вызываем метод для загрузки данных о плейлисте и видео
        self.load_playlist_data()

    @property
    def total_duration(self) -> datetime.timedelta:
        """
        Вычисляем общую продолжительность всего плейлиста.
        """
        total_seconds = sum(video.duration.total_seconds() for video in self.videos)
        return datetime.timedelta(seconds=total_seconds)

    def show_best_video(self) -> str:
        """
        Возвращает ссылку на видео с наибольшим количеством лайков.
        """
        best_video = max(self.videos, key=lambda video: video.likes)
        return best_video.url

    def load_playlist_data(self):
        """
        Загружаем информацию о плейлисте и видео в нем.
        """
        youtube = build('youtube', 'v3', developerKey=self.api_key)

        # Загружаем основную информацию о плейлисте
        playlist_data = youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        playlist = playlist_data['items'][0]['snippet']
        self.title = playlist['title']  # Задаем название плейлиста
        self.url = f"https://www.youtube.com/playlist?list={self.playlist_id}"  # Задаем ссылку на плейлист

        # Загружаем видео из плейлиста
        playlist_items = youtube.playlistItems().list(playlistId=self.playlist_id, part='snippet').execute()

        # Извлекаем ids видеороликов и загружаем информацию о каждом
        video_ids = [item['snippet']['resourceId']['videoId'] for item in playlist_items['items']]
        for video_id in video_ids:
            video_data = youtube.videos().list(id=video_id, part='snippet,statistics,contentDetails').execute()
            video_info = video_data['items'][0]['snippet']
            content_details = video_data['items'][0]['contentDetails']

            # Преобразуем строку продолжительности в объект timedelta
            duration = parse_duration(content_details['duration'])

            # Получаем количество лайков и формируем ссылку на видео
            likes = int(video_data['items'][0]['statistics']['likeCount'])
            video_url = f"https://youtu.be/{video_id}"

            # Создаем объект Video и добавляем его в список видеороликов плейлиста
            video = Video(video_info['title'], video_url, duration, likes)
            self.videos.append(video)

import os
from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id, title=None, url=None, view_count=None, like_count=None):
        """
        Инициализация объекта класса Video с получением данных о видео из YouTube API.

        :param video_id: Уникальный идентификатор видео на YouTube.
        :param title: Заголовок видео. По умолчанию None, будет получен из YouTube API.
        :param url: URL видео. По умолчанию None, будет сформирован на основе video_id.
        :param view_count: Количество просмотров видео. По умолчанию None, будет получено из YouTube API.
        :param like_count: Количество лайков под видео. По умолчанию None, будет получено из YouTube API.
        """

        youtube = build('youtube', 'v3', developerKey=os.environ.get("YT_API_KEY"))  # Инициализация сервиса YouTube
        request = youtube.videos().list(part="snippet,statistics", id=video_id)  # Создание запроса к API
        response = None  # Установка начального значения переменной ответа

        try:
            response = request.execute()  # Выполнение запроса
        except Exception as e:
            print(f'Произошла ошибка: {e}')

        # Если были получены данные из API
        if response['items']:
            item = response['items'][0]  # Получение информации о видео

            self.video_id = video_id
            self.title = item['snippet']['title']  # Получение заголовка видео
            self.url = f'https://www.youtube.com/watch?v={video_id}'  # Формирование URL видео
            self.view_count = int(item['statistics'].get('viewCount', 0))  # Получение количества просмотров
            self.like_count = int(item['statistics'].get('likeCount', 0))  # Получение количества лайков
        else:
            self.video_id = video_id
            self.title = None
            self.url = None
            self.view_count = None
            self.like_count = None

    def __str__(self):
        """Возвращение строки при преобразовании объекта в текст.

        :return: Заголовок видео.
        """
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id, title=None, url=None, view_count=None, like_count=None):
        """
        Инициализация объекта класса PLVideo, наследника класса Video, с дополнительным параметром playlist_id.

        :param video_id: Уникальный идентификатор видео на YouTube.
        :param playlist_id: Уникальный идентификатор плейлиста, которому принадлежит видео.
        :param title: Заголовок видео. По умолчанию None, будет получен из YouTube API.
        :param url: URL видео. По умолчанию None, будет сформирован на основе video_id.
        :param view_count: Количество просмотров видео. По умолчанию None, будет получено из YouTube API.
        :param like_count: Количество лайков под видео. По умолчанию None, будет получено из YouTube API.
        """

        super().__init__(video_id, title, url, view_count, like_count)  # Инициализация класса Video
        self.playlist_id = playlist_id  # Установка идентификатора плейлиста

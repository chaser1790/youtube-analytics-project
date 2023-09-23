from googleapiclient.discovery import build
import json
import os


class Channel:
    """Класс для работы с ютуб-каналом."""

    def __init__(self, channel_id: str) -> None:
        """
        Инициализирует объект канала с указанным ID канала.
        :param channel_id: строка, представляющая ID канала на YouTube.
        """
        self._channel_id = channel_id
        self._youtube = self.get_service()
        self._fetch_channel_data()

    @property
    def channel_id(self) -> str:
        """ID канала"""
        return self._channel_id

    @property
    def title(self) -> str:
        """Заголовок (название) канала"""
        return self._title

    @property
    def description(self) -> str:
        """Описание канала"""
        return self._description

    @property
    def url(self) -> str:
        """URL канала на YouTube"""
        return f'https://www.youtube.com/channel/{self.channel_id}'

    @property
    def subscribers(self) -> int:
        """Количество подписчиков канала"""
        return self._subscribers

    @property
    def video_count(self) -> int:
        """Количество видео на канале"""
        return self._video_count

    @property
    def views(self) -> int:
        """Общее количество просмотров видео канала"""
        return self._views

    @classmethod
    def get_service(cls) -> 'Resource':
        """
        Возвращает объект для работы с YouTube API.
        :return: экземпляр googleapiclient.discovery.Resource для работы с YouTube API.
        """
        api_key: str = os.getenv('YT_API_KEY')
        return build('youtube', 'v3', developerKey=api_key)

    def _fetch_channel_data(self) -> None:
        """
        Получает данные канала с YouTube API и инициализирует атрибуты канала.
        """
        channel = self._youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self._title = channel['items'][0]['snippet']['title']
        self._description = channel['items'][0]['snippet']['description']
        self._subscribers = int(channel['items'][0]['statistics']['subscriberCount'])
        self._video_count = int(channel['items'][0]['statistics']['videoCount'])
        self._views = int(channel['items'][0]['statistics']['viewCount'])

    def to_json(self, filename: str) -> None:
        """
        Сохраняет значения атрибутов экземпляра Channel в указанный файл JSON.
        :param filename: имя файла для сохранения данных канала.
        """
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers': self.subscribers,
            'video_count': self.video_count,
            'views': self.views
        }

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)

    def print_json(self, data: dict) -> None:
        """
        Выводит словарь в удобном и красивом стиле JSON с отступами.
        :param data: словарь для вывода.
        """
        print(json.dumps(data, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """
        Выводит информацию о канале на YouTube с использованием YouTube Data API v3,
        включая название, описание, количество подписчиков, количестве просмотров и т. д.
        """
        data = {
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscribers': self.subscribers,
            'video_count': self.video_count,
            'views': self.views
        }
        self.print_json(data)

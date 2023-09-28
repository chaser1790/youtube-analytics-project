from googleapiclient.discovery import build
import json
import os


class Channel:
    """
    Класс для работы с YouTube-каналом.
    """

    def __init__(self, channel_id: str) -> None:
        """
        Инициализирует объект канала с указанным ID канала.

        :param channel_id: Строка, представляющая ID канала на YouTube.
        """
        self._channel_id = channel_id
        self._youtube = self.get_service()
        self._fetch_channel_data()

    @property
    def channel_id(self) -> str:
        """
        Возвращает ID канала.

        :return: Строка с ID канала.
        """
        return self._channel_id

    @property
    def title(self) -> str:
        """
        Возвращает название канала.

        :return: Строка с названием канала.
        """
        return self._title

    @property
    def description(self) -> str:
        """
        Возвращает описание канала.

        :return: Строка с описанием канала.
        """
        return self._description

    @property
    def url(self) -> str:
        """
        Возвращает URL канала на YouTube.

        :return: Строка с URL канала.
        """
        return f'https://www.youtube.com/channel/{self.channel_id}'

    @property
    def subscribers(self) -> int:
        """
        Возвращает количество подписчиков канала.

        :return: Целое число - количество подписчиков.
        """
        return self._subscribers

    @property
    def video_count(self) -> int:
        """
        Возвращает количество видео на канале.

        :return: Целое число - количество видео.
        """
        return self._video_count

    @property
    def views(self) -> int:
        """
        Возвращает общее количество просмотров видео канала.

        :return: Целое число - общее количество просмотров.
        """
        return self._views

    @classmethod
    def get_service(cls) -> 'Resource':
        """
        Возвращает объект для работы с YouTube API.

        :return: Экземпляр googleapiclient.discovery.Resource для работы с YouTube API.
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

        :param filename: Имя файла для сохранения данных канала.
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

        :param data: Словарь для вывода.
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

    def __str__(self):
        return f"{self.title} ({self.url})"

    def __add__(self, other):
        if isinstance(other, Channel):
            return self.subscribers + other.subscribers
        raise TypeError("Unsupported operand type for +: Channel and non-Channel")

    def __sub__(self, other):
        if isinstance(other, Channel):
            return self.subscribers - other.subscribers
        raise TypeError("Unsupported operand type for -: Channel and non-Channel")

    def __eq__(self, other):
        if isinstance(other, Channel):
            return self.subscribers == other.subscribers
        return False

    def __lt__(self, other):
        if isinstance(other, Channel):
            return self.subscribers < other.subscribers
        raise TypeError("Unsupported operand type for <: Channel and non-Channel")

    def __le__(self, other):
        if isinstance(other, Channel):
            return self.subscribers <= other.subscribers
        raise TypeError("Unsupported operand type for <=: Channel and non-Channel")

    def __gt__(self, other):
        if isinstance(other, Channel):
            return self.subscribers > other.subscribers
        raise TypeError("Unsupported operand type for >: Channel and non-Channel")

    def __ge__(self, other):
        if isinstance(other, Channel):
            return self.subscribers >= other.subscribers
        raise TypeError("Unsupported operand type for >=: Channel and non-Channel")
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
        self.channel_id = channel_id
        api_key: str = os.getenv('YT_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    @staticmethod
    def printj(dict_to_print: dict) -> None:
        """
        Выводит словарь в удобном и красивом стиле JSON с отступами.

        :param dict_to_print: словарь для вывода.
        """
        print(json.dumps(dict_to_print, indent=2, ensure_ascii=False))

    def print_info(self) -> None:
        """
        Получает и выводит информацию о канале на YouTube с использованием YouTube Data API v3,
        включая название, описание, количество подписчиков, количестве просмотров и т. д.
        """
        channel = self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        self.printj(channel)

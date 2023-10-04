import datetime
import os

from src.playlist import PlayList


def load_api_key(file_path: str) -> str:
    """
    Читает текстовый файл, содержащий ключ YouTube API, из указанного пути.

    :param file_path: Путь к файлу с ключом YouTube API.
    :return: Строка с ключом YouTube API.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()


api_key_file_path = 'D:\\api_key.txt'
# Устанавливает переменную среды YT_API_KEY равной значению ключа YouTube API
os.environ["YT_API_KEY"] = load_api_key(api_key_file_path)

if __name__ == '__main__':
    # Создаем объект плейлист из класса PlayList с id плейлиста
    pl = PlayList('PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw')

    # Проверяем правильно ли установлено название плейлиста
    assert pl.title == "Moscow Python Meetup №81"
    # Проверяем правильно ли установлена ссылка на плейлист
    assert pl.url == "https://www.youtube.com/playlist?list=PLv_zOGKKxVpj-n2qLkEM2Hj96LO6uqgQw"

    # Получаем общую продолжительность плейлиста
    duration = pl.total_duration
    # Проверяем, что общая продолжительность плейлиста соответствует ожидаемой
    assert str(duration) == "1:49:52"
    # Убеждаемся, что продолжительность представлена в формате datetime.timedelta
    assert isinstance(duration, datetime.timedelta)
    # Проверяем, что общее количество секунд соответствует ожидаемому
    assert duration.total_seconds() == 6592.0

    # В качестве проверки показываем видео с наибольшим количеством лайков
    assert pl.show_best_video() == "https://youtu.be/cUGyMzWQcGM"

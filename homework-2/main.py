from src.channel import Channel
import os

def load_api_key(file_path: str) -> str:
    """
    Читает текстовый файл, содержащий YouTube API ключ, из заданного пути.

    :param file_path: Путь к файлу с ключом YouTube API.
    :return: Строка с ключом YouTube API.
    """
    with open(file_path, 'r') as file:
        return file.read().strip()

api_key_file_path = 'D:\\api_key.txt'
# Устанавливает переменную окружения YT_API_KEY в значение ключа YouTube API
os.environ["YT_API_KEY"] = load_api_key(api_key_file_path)

if __name__ == '__main__':
    # Инициализирует объект Channel с указанным ID канала
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # Получаем значения атрибутов экземпляра Channel и выводим их
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (это значение может измениться со временем)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A
    print(moscowpython.channel_id)  # UC-OVMPlMA3-YCIeg4z5z23A
    print(moscowpython.description)  # Описание канала
    print(moscowpython.subscribers)  # Количество подписчиков
    print(moscowpython.views)  # Общее количество просмотров видео канала

    # Менять не можем: атрибуты Channel класса являются свойствами (property)
    # без соответствующих установщиков (setter)
    try:
        moscowpython.channel_id = 'Новое название'
    except AttributeError as error:
        print(error)  # property 'channel_id' of 'Channel' object has no setter

    # Получаем объект для работы с YouTube API вне класса
    print(Channel.get_service())
    # <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

    # Создаем файл 'moscowpython.json' с данными по каналу
    moscowpython.to_json('moscowpython.json')

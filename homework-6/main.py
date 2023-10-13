from src.video import Video
import os


def load_api_key(file_path: str) -> str:
    """
    Функция для загрузки ключа YouTube API из текстового файла.

    :param file_path: Путь к файлу с ключом YouTube API.
    :return: Строка с ключом YouTube API.
    """

    with open(file_path, 'r') as file:
        return file.read().strip()  # Считывает содержимое файла и удаляет лишние пробелы с обеих сторон строки


# Задает путь к файлу с ключом API
api_key_file_path = 'D:\\api_key.txt'

# Загружает ключ API из файла и сохраняет его в переменной среды YT_API_KEY
os.environ["YT_API_KEY"] = load_api_key(api_key_file_path)

# Если скрипт запускается как основная программа
if __name__ == '__main__':
    # Создается экземпляр объекта Video с несуществующим идентификатором видео
    broken_video = Video('broken_video_id')
    # Проверяем, что Title и Like_count не заполнены, так как видео не существует
    assert broken_video.title is None
    assert broken_video.like_count is None

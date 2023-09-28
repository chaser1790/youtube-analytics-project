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
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print(moscowpython)  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 100100
    print(moscowpython - highload)  # -48300
    print(highload - moscowpython)  # 48300
    print(moscowpython > highload)  # False
    print(moscowpython >= highload)  # False
    print(moscowpython < highload)  # True
    print(moscowpython <= highload)  # True
    print(moscowpython == highload)  # False
    

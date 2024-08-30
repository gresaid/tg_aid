import os


def path_detector(path):
    script_dir = os.path.dirname(__file__)  # Директория текущего скрипта
    return os.path.join(script_dir, path)  # Объединяем для получения абсолютного пути

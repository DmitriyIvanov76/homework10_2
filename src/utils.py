import json
import logging
from json import JSONDecodeError


def convertor_json(path: str) -> list[dict]:
    """функция принимает на вход путь до файла
    json, возвращает список словарей"""

    # настройка логгера для модуля
    logger = logging.getLogger("utils")
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="UTF-8")
    file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    file_handler.setFormatter(file_formater)
    logger.addHandler(file_handler)
    try:
        logger.info("Начало работы")
        with open(path, encoding="UTF-8") as file:
            content = json.load(file)
            logger.info("вывод результата")
            return content
    except FileNotFoundError:
        logger.error("Файл по указанному пути - отсутствует")
        return []
    except JSONDecodeError:
        logger.error("Файл не содержит информации для обработки")
        return []

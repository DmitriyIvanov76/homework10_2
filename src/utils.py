import json
import logging
from json import JSONDecodeError


def convertor_json(path: str) -> list[dict]:
    """функция принимает на вход путь до файла
    json, возвращает список словарей"""

    # настройка логгера для модуля
    logging.basicConfig(
        filename='logs/utils.log',
        filemode='w',
        encoding='UTF-8',
        format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
        level=logging.DEBUG,
    )

    logger = logging.getLogger('utils')

    try:
        logger.info('Начало работы')
        with open(path, encoding='UTF-8') as file:
            content = json.load(file)
            logger.info('вывод результата')
            return content
    except FileNotFoundError:
        logger.error('Файл по указанному пути - отсутствует')
        return []
    except JSONDecodeError:
        logger.error('Файл не содержит информации для обработки')
        return []

import json
from json import JSONDecodeError


def convertor_json(path: str) -> list[dict]:
    """функция принимает на вход путь до файла
    json, возвращает список словарей"""
    try:
        with open(path, encoding="UTF-8") as file:
            content = json.load(file)
            return content
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []

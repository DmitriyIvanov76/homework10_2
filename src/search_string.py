import json
import re


def search_banking_operation(bank_list: str, search_str: str) -> list[dict]:
    """функция принимает путь до файла с банковскими операциями и строку поиска,
    а возвращает список словарей согласно поисковой строке"""
    # читаем json с банковскими значениями
    with open(bank_list, encoding='UTF-8') as file:
        content = json.load(file)
    # компилируем регулярное выражение
    pattern = re.compile(search_str, re.IGNORECASE)

    result = [i for i in content if 'description' in i and pattern.search(i['description'])]
    return result


path_file = '../data/operations.json'
search = 'Перевод организации'

print(search_banking_operation(path_file, search))

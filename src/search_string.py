
import re

def search_banking_operation(bank_list: list[dict], search_str: str) -> list[dict] | str :
    """функция принимает список словарей с банковскими операциями и строку поиска,
    а возвращает список словарей согласно поисковой строке"""
    if isinstance(bank_list, list) and isinstance(search_str, str):

        # компилируем регулярное выражение
        pattern = re.compile(search_str, re.IGNORECASE)

        result = [i for i in bank_list if 'description' in i and pattern.search(i['description'])]
        return result
    else:
        return 'Вы ввели неверные данные!'






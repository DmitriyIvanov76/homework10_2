from collections import Counter


def categorize_operations(banking_operations: list[dict], categories_operations: list) -> dict | str:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращать словарь, в котором ключи — это названия категорий,
     а значения — это количество операций в каждой категории"""
    # Проверка типа входных данных
    if (
        isinstance(banking_operations, list)
        and all(isinstance(i, dict) for i in banking_operations)
        and isinstance(categories_operations, list)
    ):

        # Получаем банковские операции
        descriptions = [operation.get("description") for operation in banking_operations]
        # Считаем кол-во операций по категориям и формируем словарь{Операция: кол-во}
        description_count = Counter(descriptions)
        # Генерируем словарь
        category_count = {category: description_count.get(category, 0) for category in categories_operations}
        return category_count
    # если входные данные не верного типа
    else:
        return "проверьте входные данные!"

from collections import Counter
from src.utilsdel import a, c


def categorize_operations(banking_operations: list[dict], categories_operations: list) -> dict | str:
    if isinstance(banking_operations, list) and isinstance(categories_operations, list):
        # Считаем количество операций по категориям
        descriptions = [operation.get('description') for operation in banking_operations]
        description_count = Counter(descriptions)
        category_count = {category: description_count.get(category, 0) for category in categories_operations}

        return category_count
    else:
        return 'проверьте входные данные!'

print(categorize_operations(a, c))


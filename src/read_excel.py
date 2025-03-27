import pandas as pd


def reader_excel(path: str) -> list[dict]:
    """функция принимает путь до файла excel
    а возвращает список словарей"""
    # пустой список для вложения в него словаря
    result = []
    # чтение excel из указанного пути
    df = pd.read_excel(path)
    # проходим по строкам, генерируем словарь для каждой строки
    for index, row in df.iterrows():
        # преобразем строку в словарь и добавляем результат
        result.append(row.to_dict())

    return result

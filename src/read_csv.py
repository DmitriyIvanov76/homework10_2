import csv

def csv_reader(path_file:str) -> list[dict]:
    """Функция принимает на вход путь до
    файла в формате csv и выдает список словарей"""

    csv_list = []
    with open(path_file, newline='', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            csv_list.append(row)
    return csv_list


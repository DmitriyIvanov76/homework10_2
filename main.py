from src.processing import filter_by_state, sort_by_date
from src.read_csv import csv_reader
from src.read_excel import reader_excel
from src.search_string import search_banking_operation
from src.utils import convertor_json
from src.widget import get_date, mask_account_cart


def main():
    """функция для вывода банковских операций из файла,
    согласно выбранным значениям"""
    select_file = int(
        input(
            "Привет! Добро пожаловать в программу работы\nс банковскими транзакциями.\n"
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )
    )
    if select_file == 1:
        transactions = convertor_json("data/operations.json")
        print("Для обработки выбран JSON-файл")
    elif select_file == 2:
        transactions = csv_reader("data/transactions.csv")
        print("Для обработки выбран CSV-файл")
    elif select_file == 3:
        transactions = reader_excel("data/transactions_excel.xlsx")
        print("Для обработки выбран XLSX-файл")
    else:
        print("некорректный ввод")
        return

    status_operations_list = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        select_status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        ).upper()
        if select_status in status_operations_list:
            break
        else:
            print(
                f"Статус операции {select_status} недоступен\n"
                "Введите статус, по которому необходимо выполнить фильтрацию.\n"
                "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )
    filter_transactions = filter_by_state(transactions, state=select_status)
    print(f"Операции отфильтрованы по статусу {select_status}")

    select_sort_data = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if select_sort_data == "да":
        increase_decrease = input("Отсортировать по возрастанию или по убыванию?\n").lower()
        if increase_decrease == "по возрастанию":
            filter_transactions = sort_by_date(filter_transactions)
        elif increase_decrease == "по убыванию":
            filter_transactions = sort_by_date(filter_transactions, sorted_parameter=False)

    transactions_currency = input("Выводить только рублевые транзакции? Да/Нет\n").lower()
    if transactions_currency == "да":
        filter_transactions = [i for i in filter_transactions if "RUB" in i["operationAmount"]["currency"]["code"]]

    word_filter = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n").lower()
    if word_filter == "да":
        word_search = input("Ведите слово для 3поиска\n").lower()
        filter_transactions = search_banking_operation(filter_transactions, word_search)

    if not filter_transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке {len(filter_transactions)}")

        for i in filter_transactions:

            transactions_from_account = i.get("from", "")
            check_number = i.get("to", "")

            if (
                    transactions_from_account
                    and check_number
                    and len(transactions_from_account) > 1
                    and len(check_number) > 1
            ):

                print(f"{get_date(i['date'])} {i['description']}")
                print(f"{mask_account_cart(transactions_from_account)} -> {mask_account_cart(check_number)}")
                print(f"Сумма: {i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n")

            else:
                continue


if __name__ == "__main__":
    main()

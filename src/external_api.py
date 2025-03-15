import json
import os
import random
from typing import Any, Generator

import requests
from dotenv import load_dotenv


# эта функция для подачи на вход основной функции (sum_transaction)
def gen_transaction() -> Generator[dict]:
    """функция рандомно выбирает одну транзакцию из json файла"""
    with open("../data/operations.json", encoding="UTF-8") as file:
        content = json.load(file)
        content_random = random.choice(content)
        yield content_random


# API выведен из глобальной области видимости
if __name__ == "__main__":
    transaction = next(gen_transaction())
    load_dotenv()
    API_KEY = os.getenv("API_KEY")


def sum_transaction(trans: dict[str, Any]) -> float:
    """функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    code = trans["operationAmount"]["currency"]["code"]
    if code == "RUB":
        return trans["operationAmount"]["amount"]
    else:
        params = {"from": code, "to": "RUB", "amount": 1}
        header = {"apikey": API_KEY}
        response = requests.get("https://api.apilayer.com/currency_data/convert", params=params, headers=header)
        if response.status_code != 200:
            print("Нет соединения с сервером")
        return response.json()["result"]

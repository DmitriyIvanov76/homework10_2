import json
import os
import random
import requests
from typing import Generator
from dotenv import load_dotenv


def gen_transaction() -> Generator[dict]:
    with open('../data/operations.json', encoding='UTF-8') as file:
        content = json.load(file)
        content_random = random.choice(content)
        yield content_random

if __name__ == '__main__':
    transaction = next(gen_transaction())
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

def sum_transaction(trans: dict[str]) -> float:
    code = trans['operationAmount']['currency']['code']
    if code == 'RUB':
        return trans['operationAmount']['amount']
    else:
        params = {'from': code, 'to': 'RUB', 'amount': 1}
        header = {'apikey': API_KEY}
        response = requests.get('https://api.apilayer.com/currency_data/convert', params=params, headers=header)
        if response.status_code != 200:
            print('Не удается соединиться с сервером')
            return ''
        else:
            return response.json()['result']

print(sum_transaction(transaction))




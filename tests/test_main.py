from main import main


def test_main():
    assert main() == 'Не найдено ни одной транзакции, подходящей под ваши условия фильтрации'

import logging

# настройка логгера для модуля
logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="UTF-8")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def get_mask_card_number(number_cart: str) -> str:
    """функция принимает на вход номера карты, а возвращает номер с несколькими цифрами закрытыми звездочкой"""

    logger.info("проверка карты соответствию заданной длине")
    if len(number_cart) == 16 and number_cart.isdigit():
        logger.info("вывод информации")
        return f"{number_cart[0:4]} {number_cart[5:7]}** **** {number_cart[-4:]}"

    else:
        logger.error("номер карты не соответствует заданной длине")
        raise ValueError("Ошибка ввода номера карты")


def get_mask_account(number_account: str) -> str:
    """функция принимает на вход номер счета,а возвращает последние четыре цифры счета"""

    logger.info("проверка номера счета соответствию заданной длине")
    if len(number_account) == 20 and number_account.isdigit():
        logger.info("вывод информации")
        coded_account_number = "**" + number_account[-4:]
        return coded_account_number
    else:
        logger.error("Ошибка ввода номера счета")
        raise ValueError("ошибка ввода номера счета")

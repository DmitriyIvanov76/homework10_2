import datetime
from functools import wraps


def log(filename=None):
    """Декоратор для ведения лога функции"""
    def log_message(message):
        """Записывает сообщение в файл или выводит в консоль"""
        if filename:
            with open(filename, "a", encoding="UTF-8") as file:
                file.write(message + "\n")
        else:
            print(message)

    def real_decorator(func):
        """Реальный декоратор функции"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            now_time = datetime.datetime.now()
            try:
                log_message(f"{now_time:} Запуск функции {func.__name__}")
                result = func(*args, **kwargs)
                log_message(f"{now_time:} Функция {func.__name__} завершила выполнение с результатом {result}")
                return result
            except Exception as a:
                log_message(f"{now_time:} Во время работы функции {func.__name__} возникла ошибка {a}")
                if filename:
                    return f"произошла ошибка, подробности можно посмотреть в {filename}"
                else:
                    return f"Произошла ошибка {a}"

        return wrapper

    return real_decorator

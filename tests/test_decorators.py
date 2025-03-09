import os

import pytest

from src.decorators import log


@log(filename="test_log.txt")
def my_function(x, y):
    return x + y


@log()
def my_function_no_file(x, y):
    return x + y


@log(filename="test_log.txt")
def my_function_error():
    raise ValueError("тестовый вызов ошибки")


@log()
def my_function_error_no_file():
    raise ValueError("тестовый вызов ошибки")


def test_my_function():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = my_function(1, 2)
    assert result == 3

    with open("test_log.txt", "r", encoding="UTF-8") as file:
        content_log = file.read()

    assert "Запуск функции my_function\n" in content_log
    assert f"Функция my_function завершила выполнение с результатом {result}\n" in content_log


def test_my_function_no_file(capsys):
    result_func_no_file = my_function_no_file(1, 2)
    assert result_func_no_file == 3

    captured = capsys.readouterr()
    assert "Запуск функции my_function_no_file" in captured.out
    assert f"Функция my_function_no_file завершила выполнение с результатом {result_func_no_file}" in captured.out


def test_my_function_error():
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")
    result_work_func_error = my_function_error()
    assert result_work_func_error == "произошла ошибка, подробности можно посмотреть в test_log.txt"
    with open("test_log.txt", "r", encoding="UTF-8") as file:
        contetnt_log_error = file.read()
    assert "Во время работы функции my_function_error возникла ошибка тестовый вызов ошибки" in contetnt_log_error


def test_my_function_error_no_file(capsys):
    result_func_error_no_file = my_function_error_no_file()
    assert result_func_error_no_file == "Произошла ошибка тестовый вызов ошибки"
    captured = capsys.readouterr()
    assert "Запуск функции my_function_error_no_file" in captured.out
    assert "Во время работы функции my_function_error_no_file возникла ошибка тестовый вызов ошибки" in captured.out

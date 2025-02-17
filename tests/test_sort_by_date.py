import pytest

from src.processing import sort_by_date


# проверяем сортировку по убыванию даты
def test_sort_by_date_down(list_dict_for_sorted_date, correct_answer):
    assert sort_by_date(list_dict_for_sorted_date[4:], False) == correct_answer


# проверяем сортировку по возрастанию даты
def test_sort_by_date_up(list_dict_for_sorted_date, correct_answer_true):
    assert sort_by_date(list_dict_for_sorted_date[4:], True) == correct_answer_true


# проверяем корректность сортировки при вводе одинаковых дат
def test_sort_by_date_identical(list_dict_for_sorted_date, correct_answer_identical):
    assert sort_by_date(list_dict_for_sorted_date[2:5]) == correct_answer_identical


# вызываем ошибку подав неверный формат даты
def test_sort_by_date_error(list_dict_for_sorted_date):
    with pytest.raises(TypeError):
        sort_by_date(list_dict_for_sorted_date[1])


def test_sort_by_date_second_error(list_dict_for_sorted_date):
    with pytest.raises(TypeError):
        sort_by_date(list_dict_for_sorted_date[2])

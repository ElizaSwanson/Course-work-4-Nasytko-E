from src.class_vacancy import Vacancy
from src.utils import (get_salary_range, get_top_vacancies,
                       sort_vacancies_by_salary)

vac = [
    Vacancy("python", "https://hh.ru", "требования", "обязанности", 0),
    Vacancy("java", "https://hh.ru", "требования", "обязанности", 120000),
]


def test_get_salary_from():
    assert get_salary_range(vac, 40000) == [
        Vacancy("java", "https://hh.ru", "требования", "обязанности", 120000)
    ]
    assert get_salary_range(vac, 100000000) == []


def test_get_top():
    res = get_top_vacancies(vac, 2)
    assert res == [
        Vacancy("java", "https://hh.ru", "требования", "обязанности", 120000),
        Vacancy("python", "https://hh.ru", "требования", "обязанности", 0),
    ]


def test_sort():
    res = sort_vacancies_by_salary(vac)
    assert res == [
        Vacancy("java", "https://hh.ru", "требования", "обязанности", 120000),
        Vacancy("python", "https://hh.ru", "требования", "обязанности", 0),
    ]

import pytest

from src.class_vacancy import Vacancy


@pytest.fixture
def vac_dict():
    vacs = [
        {
            "name": "Продавец",
            "url": "https://hh.ru",
            "requirement": "продавать",
            "responsibility": "продажник",
            "salary": 0,
        },
        {
            "name": "Разработчик",
            "url": "https://hh.ru",
            "requirement": "кодить",
            "responsibility": "разрабатывать",
            "salary": 120000,
        },
    ]

    return vacs


@pytest.fixture
def vac_objects():
    vac = [
        Vacancy("python", "https://hh.ru", "требования", "обязанности", 0),
        Vacancy("java", "https://hh.ru", "требования 1", "обязанности 1", 10000),
    ]

    return vac

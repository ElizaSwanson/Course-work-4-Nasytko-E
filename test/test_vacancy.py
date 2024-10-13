from src.class_vacancy import Vacancy

vac1 = Vacancy("python", "https://hh.ru", "требования", "обязанности", 0)
vac2 = Vacancy("java", "https://hh.ru", "требования 1", "обязанности 1", 10000)
vac3 = Vacancy("java", "https://hh.ru", "требования 1", "обязанности 1", 30000)


def test_init():
    assert vac1.name == "python"
    assert vac1.url == "https://hh.ru"
    assert vac1.requirement == "требования"
    assert vac1.responsibility == "обязанности"
    assert vac1.salary == 0

def test_eq():
    assert vac2 != vac1

def test_le():
    assert vac2 < vac3

def test_lt():
    assert vac2 > vac1

def test_salary():
    assert str(vac1) == f"Должность: python.\nСсылка на вакансию: https://hh.ru.\nЗарплата: не указана.\nТребования: требования.\nОбязанности: обязанности"
    assert str(vac2) == f"Должность: java.\nСсылка на вакансию: https://hh.ru.\nЗарплата: 10000.\nТребования: требования 1.\nОбязанности: обязанности 1"

def test_vac_to_dict():
    assert vac1.vac_to_dict() == {'name': 'python',
 'requirement': 'требования',
 'responsibility': 'обязанности',
 'salary': 0,
 'url': 'https://hh.ru'}

def test_vac_to_list(vac_dict):
    res = Vacancy.vac_to_list(vac_dict)
    assert res[0].name == "Продавец"

def test_empty_list():
    res = Vacancy.vac_to_list([])
    assert res == []

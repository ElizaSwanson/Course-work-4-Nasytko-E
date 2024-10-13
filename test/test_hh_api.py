from src.class_hh_api import HH


def test_head_hunter_api():
    api = HH()
    assert api.url == "https://api.hh.ru/vacancies"


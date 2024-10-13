from src.class_vacancy import Vacancy


def get_salary_range(vacancies: list[Vacancy], salary_from: int) -> list:
    """возвращает вакансии в заданном диапазоне по зп"""

    return [vac for vac in vacancies if vac.salary >= salary_from]


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list:
    """сортировка по зп"""

    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)


def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list:
    """выводит топ N вакансий по зп"""

    sorted_vacancies = sort_vacancies_by_salary(vacancies)

    return sorted_vacancies[:top_n]

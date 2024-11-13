from src.class_hh_api import HH, Find_id_from_hh_api
from src.class_saver import JSON_saver
from src.class_vacancy import Vacancy
from src.utils import get_salary_range, get_top_vacancies
from src.class_DBManager_module import DBManager
from src.class_create_module import DBConnection


def user():
    employer_search = input("Введите ключевое слово для поиска:\n")
    employers_count = int(input("Введите желаемое число вакансий на странице (до 50):\n"))
    employer_obj = Find_id_from_hh_api()
    employers = employer_obj.get_employer_info(employers_count, keyword=employer_search)
    DBConnection().create_db()
    db_connect = DBConnection()
    db_connect.db_creating_employers()
    employers_id_list = list(input("Введите через запятую id не менее 1 компании для отслеживания:\n").split(", "))
    db_connect.db_employers(employers_id_list, employers)
    db_connect.db_vacancies()
    for emp_id in employers_id_list:
        vacancy_list = HH().get_vacancies_by_employer_id(emp_id)
        db_connect.db_adding_vacancies(vacancy_list)
    searching_keyword = input('Введите слово для поиска по имеющимся вакансиям ...')
    query_manager = DBManager()
    print(query_manager.get_companies_and_vacancies_count())
    print(query_manager.get_all_vacancies())
    print(query_manager.get_avg_salary())
    print(query_manager.get_vacancies_with_higher_salary())
    print(query_manager.get_vacancies_with_keyword(searching_keyword))


if __name__ == "__main__":
    user()

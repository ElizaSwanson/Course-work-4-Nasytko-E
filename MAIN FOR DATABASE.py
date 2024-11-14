from src.class_hh_api import HH, Find_id_from_hh_api
from src.class_DBManager_module import DBManager
from src.class_create_module import create_database, save_data_to_database
from src.parametes import config


def user():
    params = config()
    create_database('test_db', params)
    data_employer = Find_id_from_hh_api().get_emp()
    data_vacancies = Find_id_from_hh_api().load_vacancies()
    save_data_to_database(data_employer, data_vacancies, 'test_db', params)
    db_manager = DBManager(params)
    print("Привет! Я твой помощник для отслеживания вакансий выбранных тобой работодателей.")
    print("Что тебе нужно сделать? Вот что я могу:")
    print("1. Показать список компаний и количество вакансий у каждой компании")
    print("2. Показать список всех вакансий со ссылками на вакансию")
    print("3. Посчитать среднюю зарплату у вакансий")
    print("4. Показать вакансии с зарплатой выше средней")
    print("5. Отобрать вакансии по ключевому слову")
    print("6. Завершить работу программы")
    while True:
        user_input = input()
        if user_input == "1":
            companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
            for i in companies_and_vacancies_count:
                print(i)
            print("Что-то еще?")
        elif user_input == "2":
            all_vacancies = db_manager.get_all_vacancies()
            for i in all_vacancies:
                print(i)
            print("Что-то еще?")
        elif user_input == "3":
            avg_salary = db_manager.get_avg_salary()
            print(avg_salary)
            print("Что-то еще?")
        elif user_input == "4":
            vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
            for i in vacancies_with_higher_salary:
                print(i)
            print("Что-то еще?")
        elif user_input == "5":
            user_word = input("Введите слово для поиска\n").lower()
            vacancies_with_keyword = db_manager.get_vacancies_by_word(user_word)
            for i in vacancies_with_keyword:
                print(i)
            print("Что-то еще?")
        elif user_input == "6":
            print("Пока!")
            break


if __name__ == "__main__":
    user()

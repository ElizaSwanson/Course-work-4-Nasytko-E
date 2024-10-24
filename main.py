from src.class_hh_api import HH
from src.class_saver import JSON_saver
from src.class_vacancy import Vacancy
from src.utils import get_salary_range, get_top_vacancies


def user():
    search = input("Приветствуем! Введите ключевое слово для поиска на ХХ.ру:")

    print("Ищем, ожидайте.")

    search_api = HH()
    load_vacs = search_api.load_vacancy_info(search)

    save_vac = JSON_saver()
    save_vac.add_vac(load_vacs)

    if load_vacs:
        print(
            "Доступный список действий:\n 1. Показать вакансии.\n2. Поиск вакансии по уровню зарплаты.\n3. Поиск вакансии по ключевому слову.\n4. Показать топ вакансий по уровню зарплаты.\n5. Добавить вакансию.\n6. Удалить вакансию"
        )

        try:
            user_input = int(input("Введите цифру от 1 до 6: "))
        except ValueError:
            print("Введена неправильная цифра. Выбрано действие 1")
            user_input = 1
        else:
            if user_input not in range(1, 7):
                print("Введена неправильная цифра. Выбрано действие 1")
                user_input = 1

    if user_input == 1:
        for vac in Vacancy.vac_to_list(load_vacs):
            print(vac)
        print("Спасибо, что воспользовались нашими услугами!")

    elif user_input == 2:
        try:
            search_salary = int(input("Введите желаемый уровень дохода: "))
        except ValueError:
            print("Выбраны все вакансии с указанием зарплаты")
            search_salary = 0
        search_by_salary = Vacancy.vac_to_list(load_vacs)
        for vac in get_salary_range(search_by_salary, search_salary):
            print(vac)
        print("Спасибо, что воспользовались нашими услугами!")

    elif user_input == 3:
        search_key = input("Введите ключевое слово для поиска: ").lower()
        for vac in save_vac.vac_by_name(search_key):
            print(vac)
        print("Спасибо, что воспользовались нашими услугами!")

    elif user_input == 4:
        try:
            search_top = int(input("Введите количество желаемых вакансий: "))
        except ValueError:
            print("Будут выведены 5 вакансий")
            search_top = 5
        search_res = Vacancy.vac_to_list(load_vacs)
        for vac in get_top_vacancies(search_res, search_top):
            print(vac)
        print("Спасибо, что воспользовались нашими услугами!")

    elif user_input == 5:
        name_input = input("Введите название вакансии: ")
        url_input = input("Введите ссылку на вакансию: ")
        req_input = input("Введите требования для кандидата: ")
        res_input = input("Введите рабочие обязанности: ")
        sal_input = int(input("Введите зарплату: "))
        new_vacancy = Vacancy(name_input, url_input, req_input, res_input, sal_input)
        save_vac.add_vac(new_vacancy)
        print("Спасибо, что воспользовались нашими услугами!")

    elif user_input == 6:
        del_url = input("Введите ссылку на вакансию: ")
        save_vac.delete_vac(del_url)
        print("Вакансия успешно удалена")
        print("Спасибо, что воспользовались нашими услугами!")


if __name__ == "__main__":
    user()

import psycopg2

from src.class_create_module import DBConnection


class DBManager(DBConnection):
    """Класс для взаимодействия с базой данных"""

    def __init__(self):
        super().__init__()

    def connect_to_db(self, query, params=None):
        conn = psycopg2.connect(
            host="localhost", database="postgres", user="postgres", port="5432", password="4568093h")
        cur = conn.cursor()
        conn.autocommit = True
        cur.execute(query, params)
        result = cur.fetchall()
        cur.close()
        conn.close()
        return result

    def get_companies_and_vacancies_count(self):
        """получает список всех компаний и количество вакансий у каждой компании"""
        execute_message = """SELECT employers.company_name, COUNT(vacancies.employer_id)
        FROM employers JOIN vacancies USING (employer_id) GROUP BY employer_id"""
        return f'Компании и количество вакансий:\n{self.connect_to_db(execute_message)}'

    def get_all_vacancies(self):
        """получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию"""
        execute_message = """SELECT employers.company_name, vacancies.vacancy_name, 
        ((vacancies.salary_from + vacancies.salary_to) / 2), vacancies.url
        FROM vacancies JOIN employers USING(employer_id)"""
        return f'Список всех вакансий:\n{self.connect_to_db(execute_message)[:10]} \n ...'

    def get_avg_salary(self):
        """получает среднюю зарплату по вакансиям"""
        execute_message = """SELECT AVG((vacancies.salary_from + vacancies.salary_to) / 2) FROM vacancies"""
        return f'Средняя зарплата по вакансиям:\n{self.connect_to_db(execute_message)}'

    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        execute_message = """SELECT * FROM vacancies WHERE ((vacancies.salary_from + vacancies.salary_to) / 2) > 
(SELECT (AVG((vacancies.salary_from + vacancies.salary_to) / 2)) FROM vacancies)"""
        return f'Вакансии с зарплатой выше среднего:\n{self.connect_to_db(execute_message)[:10]}'

    def get_vacancies_with_keyword(self, keyword: str):
        """получает список всех вакансий, в названии которых содержатся переданные в метод слова"""
        execute_message = f"""SELECT * FROM vacancies WHERE vacancy_name ILIKE '%{keyword}%'"""
        return f'Вакансии по ключевому слову:\n{self.connect_to_db(execute_message)[:10]}'

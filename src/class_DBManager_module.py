import psycopg2


class DBManager:
    """класс для взаимодействия с базой данных"""

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname="test_db", **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """метод для получения всех компаний и вакансий у каждой из них"""
        self.cur.execute(
            """
                    SELECT employer_name, COUNT(vacancies.employer_id)
                    FROM employers
                    INNER JOIN vacancies USING (employer_id)
                    GROUP BY employer_name
                    ORDER BY COUNT DESC
            """
        )

        return self.cur.fetchall()

    def get_all_vacancies(self):
        """метод для вывода вакансий с указанием названия работодателя, названия вакансии, зп и ссылки на вакансию"""
        self.cur.execute(
            """
                    SELECT e.employer_name, v.vacancy_name, v.salary, v.vacancy_url
                    FROM vacancies v
                    INNER JOIN employers e USING (employer_id)
                    WHERE v.salary IS NOT NULL AND v.salary != 0
                    ORDER BY v.salary DESC

            """
        )

        return self.cur.fetchall()

    def get_avg_salary(self):
        """метод для подсчёта средней зп по всем вакансиям"""
        self.cur.execute(
            """
                    SELECT AVG(salary)
                    FROM vacancies
            """
        )

        result = self.cur.fetchone()
        avg_salary = float(round(result[0]))
        formatted_avg_salary = format(avg_salary, ".2f")
        return formatted_avg_salary

    def get_vacancies_with_higher_salary(self):
        """метод для поиска вакансий с зп выше, чем в методе со средней зп"""
        avg_salary = self.get_avg_salary()[0][0]

        self.cur.execute(
            """
            SELECT v.vacancy_name, v.salary
            FROM vacancies v
            WHERE v.salary > %s
            """,
            (avg_salary,),
        )
        return self.cur.fetchall()

    def get_vacancies_by_word(self, keyword):
        """
        Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например python.
        """

        query = """
        SELECT * FROM vacancies
        WHERE LOWER(vacancy_name) LIKE %s
        """
        self.cur.execute(query, ("%" + keyword.lower() + "%",))
        return self.cur.fetchall()

class Vacancy:
    """класс для обработки ключевых моментов вакансии"""

    __slots__ = ["name", "url", "requirement", "responsibility", "salary"]

    def __init__(
        self,
        name: str,
        url: str,
        requirement: str,
        responsibility: str,
        salary: int | None,
    ) -> None:
        """инициализатор класса"""

        self.name = name
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary = salary

    @classmethod
    def vac_to_list(cls, vacancies: list[dict]) -> list["Vacancy"]:
        """собирает данные и переделывает в список"""

        return [cls(**vac) for vac in vacancies]

    @staticmethod
    def __get_salary(salary: int | None) -> int | None:
        if salary:
            return salary
        return "Зарплата не указана"

    def __eq__(self, other):
        """сравнение - зарплаты равны"""

        return self.salary == other.salary

    def __lt__(self, other):
        """сравнение - зарплата меньше"""

        return self.salary < other.salary

    def __gt__(self, other):
        """сравнение - зарплата больше"""

        return self.salary > other.salary

    def __str__(self) -> str:
        """отображение ключевых моментов вакансии"""

        return (
            f"Должность: {self.name}.\nСсылка на вакансию: {self.url}.\nЗарплата: {self.salary if self.salary else "не указана"}."
            f"\nТребования: {self.requirement}.\nОбязанности: {self.responsibility}"
        )

    def vac_to_dict(self) -> dict:
        """возвращает словарь с данными"""

        return {
            "name": self.name,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "salary": self.salary,
        }

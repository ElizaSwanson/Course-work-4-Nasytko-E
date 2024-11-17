from abc import ABC, abstractmethod

import requests


class Parser(ABC):

    @abstractmethod
    def __init__(self):
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        """инициализация объектов класса"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = [1552753, 2180, 78638, 17862, 596246, 954660, 4787018, 9498112, 9739145, 1495025]

    @property
    def url(self) -> str:
        """возвращает ссылку"""
        return self.__url

    def __connect_to_api(self):
        """запрашивает данные у ХХ"""
        response = requests.get(
            self.__url, headers=self.__headers, params=self.__params
        )
        if response.status_code == 200:
            return response
        print("Ошибка получения данных")

    def load_vacancy_info(self, keyword):
        """ищет вакансии по ключевому слову"""

        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = self.__connect_to_api()
            if response:
                vacancy = response.json()["items"]
                self.__vacancies.extend(vacancy)
                self.__params["page"] += 1
            else:
                break

        vac_list = []

        if self.__vacancies:
            for vac in self.__vacancies:
                name = vac.get("name")
                url = vac.get("alternate_url")
                requirement = vac.get("snippet").get("requirement")
                responsibility = vac.get("snippet").get("responsibility")

                if vac.get("salary"):
                    if vac.get("salary").get("to"):
                        salary = vac.get("salary").get("to")
                    elif vac.get("salary").get("from"):
                        salary = vac.get("salary").get("from")
                else:
                    salary = 0

                vacancy = {
                    "name": name,
                    "url": url,
                    "requirement": requirement,
                    "responsibility": responsibility,
                    "salary": salary,
                }
                vac_list.append(vacancy)

            return vac_list

    def __get_vacancies_by_employer_id(self, employer_id: str):
        """метод для получения информации по айди компании"""
        try:
            self.__params["employer_id"] = employer_id
            while self.__params.get("page") != 10:
                response = requests.get(
                    self.__url, headers=self.__headers, params=self.__params
                )
                response_data = response.json()

                if "items" in response_data:
                    vacancies = response_data["items"]
                    self.__vacancies.extend(vacancies)
                else:
                    print(f"Нет вакансий для работодателя с ID: {employer_id}")
                    break

                self.__params["page"] += 1
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def get_vacancies_by_employer_id(self, employer_id: str):
        self.__get_vacancies_by_employer_id(employer_id)
        return self.__vacancies


class Find_id_from_hh_api(Parser):
    """Получение информации по работодателям"""

    def __init__(self):
        self._url = "https://api.hh.ru/"
        self._headers = {"User-Agent": "HH-User-Agent"}
        self._params = {"per_page": 100, "page": 0, "only_with_salary": True}
        self.employers = [1552753]

    def _get_employer_info(self, keyword=""):
        """метод для получения информации. ПРИВАТНЫЙ!"""
        try:
            self._params["text"] = keyword
            while self._params.get("page") != 20:
                response = requests.get(
                    self._url, headers=self._headers, params=self._params
                )
                employers = response.json()
                self._employers.extend(employers["items"])
                self._params["page"] += 1
        except Exception as e:
            print(f"Что-то не так с подключением, ошибка: {e}")

    def get_employer_info(self, employers_count, keyword=""):
        self._get_employer_info(keyword)
        for employer in self._employers[:employers_count]:
            print(f"{employer.get('name')}, id: {employer.get('id')}")
        return self._employers

    def get_emp(self):
        employers_info = []
        for employer_id in self.employers:
            temp_url = f"{self._url}employers/{employer_id}"
            employer_data = requests.get(temp_url).json()
            employers_info.append(employer_data)

        return employers_info

    def load_vacancies(self):
        """загрузка вакансий"""
        vacancy_info = []
        for employer_id in self.employers:
            self._params["employer_id"] = employer_id
            vacancy_url = f"{self._url}vacancies"
            response = requests.get(
                vacancy_url, headers=self._headers, params=self._params
            )
            vacancies = response.json()["items"]
            vacancy_info.extend(vacancies)
        return vacancy_info

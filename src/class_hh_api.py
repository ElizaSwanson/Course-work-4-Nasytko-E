from abc import ABC, abstractmethod
import requests


class Parser(ABC):

    @abstractmethod
    def load_vacancy_info(self, keyword: str) -> list:
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter  """

    def __init__(self):
        """инициализация объектов класса"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100}
        self.__vacancies = []

    @property
    def url(self) -> str:
        """возвращает ссылку"""
        return self.__url

    def __connect_to_api(self):
        """запрашивает данные у ХХ"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        print("Ошибка получения данных")

    def load_vacancy_info(self, keyword):
        self.__params['text'] = keyword
        while self.__params.get('page') != 20:
            response = self.__connect_to_api()
            if response:
                vacancy = response.json()['items']
                self.__vacancies.extend(vacancy)
                self.__params['page'] += 1
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

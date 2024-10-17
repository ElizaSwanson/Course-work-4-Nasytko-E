import json
import os.path
from abc import ABC, abstractmethod
from json import JSONDecodeError

from config import DATA_DIR
from src.class_vacancy import Vacancy


class ABC_saver(ABC):

    @abstractmethod
    def add_vac(self, vacancy: Vacancy) -> None:
        pass

    @abstractmethod
    def vac_by_name(self, keyword: str) -> list[Vacancy]:
        pass

    @abstractmethod
    def delete_vac(self, url: str) -> None:
        pass


class JSON_saver(ABC_saver):

    def __init__(self, filename: str = "my_vacancies.json"):
        """инициализация класса"""

        self.__filename = os.path.join(DATA_DIR, filename)

    def __read_file(self) -> list[dict]:
        """считывает путь до файла"""

        try:
            with open(self.__filename, encoding="utf-8") as file:
                data_json = json.load(file)
        except FileNotFoundError:
            data_json = []
        except JSONDecodeError:
            data_json = []

        return data_json

    def __save_file(self, vacancy: list[dict]) -> list[dict]:
        """сохраняет обновленный файл"""

        with open(self.__filename, "w", encoding="utf-8") as file:
            json.dump(vacancy, file, ensure_ascii=False)

    def add_vac(self, vacancies: Vacancy):
        """добавляет вакансию в файл"""

        vac_list = self.__read_file()
        for va in vacancies:
            if va["url"] not in [vac["url"] for vac in vac_list]:
                vac_list.append(va)
                self.__save_file(vac_list)

    def delete_vac(self, url: str) -> None:
        """Удаляет вакансию из файла"""

        vac_list = self.__read_file()
        for index, vac in enumerate(vac_list):
            if vac["url"] == url:
                vac_list.pop(index)

        self.__save_to_file(vac_list)

    def vac_by_name(self, word: str) -> list[Vacancy]:
        """здесь хранится список вакансий с keyword"""
        vac_found = []

        for vac in self.__read_file():
            if word in vac.get("name").lower():
                vac_found.append(vac)

        return Vacancy.vac_to_list(vac_found)

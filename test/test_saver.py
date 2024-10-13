import json
import os

from config import DATA_DIR
from src.class_saver import JSON_saver
from src.class_vacancy import Vacancy


def test_json():
    filename = JSON_saver("test.json")
    vac1 = Vacancy("python", "https://hh.ru", "требования", "обязанности", 0)

    filename.add_vac(vac1)
    file = os.path.join(DATA_DIR, "test.json")

    with open(file, encoding="utf-8") as f:
        res = json.load(f)
    assert res == [
        {
            "name": "python",
            "requirement": "требования",
            "responsibility": "обязанности",
            "salary": 0,
            "url": "https://hh.ru",
        }
    ]

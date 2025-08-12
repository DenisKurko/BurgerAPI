import json


class NotFoundError(Exception):
    pass


def get_db() -> dict[str, dict]:
    with open("app/db/data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def save_db(data: dict) -> None:
    with open("app/db/data/data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=0)
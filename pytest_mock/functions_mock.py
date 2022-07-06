import datetime
import time
from dataclasses import dataclass
from typing import List

import requests
from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return "<Blog: {}>".format(self.name)


class Calculator:
    def sum(self, a, b):
        time.sleep(6)  # long running process
        return a + b


def get_json(url):
    """Takes a URL, and returns the JSON."""
    r = requests.get(url)
    return r.json()


@dataclass
class Repository:
    entity_id: str
    name: str
    bitbucket_id: str


def search_db(query: str) -> List[Repository]:
    eng = create_engine("postgresql://postgres:admin@localhost:5432/postgres")

    with eng.connect() as con:
        statement = text("SELECT * FROM public.repository WHERE name LIKE :q")
        statement = statement.bindparams(q="%" + query + "%")
        rs = con.execute(statement)

        res: List[Repository] = []
        for row in rs.fetchall():
            res.append(Repository(entity_id=row[0], name=row[1], bitbucket_id=row[2]))

        return res


def discount_calculator(
    value: float, due_date: datetime.date, discount: float, days: int
) -> float:
    diff = due_date - datetime.date.today()
    if datetime.timedelta() <= diff < datetime.timedelta(days=days):
        return value * (1.0 - discount)
    else:
        return value

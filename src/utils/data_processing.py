import csv
from typing import TextIO
from typing import List
from typing import Mapping
from typing import Union
from typing import Tuple


from src.data import datasets


def process_ethnics(data: TextIO) -> List:
    """Returns a generator of ethnics dictionary

    Args:
        data (TextIO): A file-like object of ethnics data
    """
    next(data)
    datas = csv.reader(data)
    return [item[1] for item in datas]


def process_religions() -> List[str]:
    """Returns a list of religion dictionary"""
    return [religion.vietnamese for religion in datasets.RELIGION]


def process_working_status() -> List[str]:
    """Returns a list of working status dictionary"""
    return [status.vietnamese for status in datasets.WORKING_STATUS]


def process_employment_contract():
    """Returns a list of employment contract dictionary"""
    return [contract.vietnamese for contract in datasets.EMPLOYMENT_CONTRACT]


def process_level_settings(data: Tuple):
    """Returns a list of teaching title dictionary"""
    return [item.vietnamese for item in data]
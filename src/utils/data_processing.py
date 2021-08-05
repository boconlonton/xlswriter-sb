import csv
from typing import TextIO
from typing import List
from typing import Mapping
from typing import Union
from typing import Tuple
from typing import Any
from typing import Generator

from src.data import datasets


def process_provinces(data: Mapping[str, Union[str, int]]) -> List:
    """Returns list of all provinces from data file
    Args:
        data (Mapping): A dictionary of province data
    """
    for province in data:
        yield [province.get('code'), province.get('name')]


def process_districts(data: Mapping[str, Any]) -> Generator:
    """Yields list districts of a province
    Args:
        data (Mapping): A dictionary of province data
    """
    for province in data:
        for district in province.get('districts'):
            yield [
                district.get('code'),
                province.get('code'),
                district.get('name'),
                province.get('name')
            ]


def process_wards(data: Mapping[str, Union[str, int]]) -> Generator:
    """Returns a generator of dictionaries that contains ward information
    Args:
        data (Mapping): A dictionary of wards data
    """
    for ward in data:
        if ward.get('ward_name'):
            yield [
                ward.get('ward_code'),
                ward.get('district_code'),
                ward.get('province_code'),
                ward.get('ward_name'),
                ward.get('district_name'),
                ward.get('province_name')
            ]


def process_ethnics(data: TextIO):
    """Returns a generator of ethnics dictionary

    Args:
        data (TextIO): A file-like object of ethnics data
    """
    next(data)
    datas = csv.reader(data)
    return [item for item in datas]


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

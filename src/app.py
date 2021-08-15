import json
from datetime import date
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell

from src import utils

from src.data import datasets

contract_types = utils.process_employment_contract()
with open('data/ethnics.csv', 'r') as f:
    ethnics = utils.process_ethnics(f)
religions = utils.process_religions()
teaching_titles = utils.process_level_settings(datasets.TEACHING_TITLE)
academic_titles = utils.process_level_settings(datasets.ACADEMIC_TITLE)
degrees = utils.process_level_settings(datasets.DEGREE)
working_status = utils.process_working_status()

workbook = xlsxwriter.Workbook(
    'output/data.xlsx',
    # {
    #     'default_date_format': 'dd/mm/yyyy'
    # }
)
ws1 = workbook.add_worksheet('Data')
ws2 = workbook.add_worksheet('MA_TINH')
ws3 = workbook.add_worksheet('MA_HUYEN')
ws4 = workbook.add_worksheet('MA_PHUONG_XA')
ws5 = workbook.add_worksheet('DAN_TOC')

# Add a format for the header cells.
header_format = workbook.add_format({
    'border': 1,
    'bg_color': '#C6EFCE',
    'bold': True,
    'text_wrap': True,
    'valign': 'vcenter',
    'indent': 1,
})
cell_format = workbook.add_format({
    'border': 1,
    'text_wrap': True,
    'valign': 'vcenter',
    'indent': 1,
})

ws1.set_column(0, 40, 20)
ws1.set_row(0, 40)

headers = {
    'Last name': None,
    'Middle name': None,
    'First name': None,
    'Staff ID': None,
    'Date of Birth': 'is_date',
    'Work email': None,
    'Phone number': None,
    'Tax code': None,
    'Social code': None,
    'Government ID': None,
    'Government issued date': 'is_date',
    'Government issued place': None,
    'Passport ID': None,
    'Passport issued date': 'is_date',
    'Passport issued place': None,
    'Working status': working_status,
    'Start working date': 'is_date',
    'End working date': 'is_date',
    'User type': ['Staff', 'Teacher'],
    'Gender': ['Male', 'Female', 'Others'],
    'Permission profile': ['Default profile', 'Admin profile'],
    'Employment contract': contract_types,
    'Birthplace': None,
    'Hometown': None,
    'Ethnics': None,
    'Religion': religions,
    'Communist party status': ['True', 'False'],
    'Communist party entry date': 'is_date',
    'Trade union status': ['True', 'False'],
    'Trade union entry date': 'is_date',
    'Teaching title': teaching_titles,
    'Academic title': academic_titles,
    'Degree': degrees,
}

count = 0
for k, v in headers.items():
    ws1.write(xl_rowcol_to_cell(0, count), k, header_format)
    if isinstance(v, list):
        ws1.data_validation(xl_rowcol_to_cell(1, count),
                            {
                                'validate': 'list',
                                'source': v
                            })
    if k == 'Ethnics':
        ws1.data_validation(xl_rowcol_to_cell(1, count),
                            {
                                'validate': 'list',
                                'source': f'=DAN_TOC!$B$1:$B$56'
                            })
    if v == 'is_date':
        ws1.data_validation(xl_rowcol_to_cell(1, count),
                            {
                                'validate': 'date',
                                'criteria': 'between',
                                'minimum': date(1910, 1, 1),
                                'maximum': date(2021, 12, 12)
                            })
    count += 1

with open('data/vietnam_nested.json', 'r') as f:
    raw_data = json.load(f)
    provinces = utils.process_provinces(raw_data)
    districts = utils.process_districts(raw_data)

with open('data/vietnam_flat.json', 'r') as f:
    raw_data = json.load(f)
    wards = utils.process_wards(raw_data)

province_headers = ['Mã Tỉnh/TP', 'Tên Tỉnh/TP']
district_headers = [
    'Mã Quận/ Huyện',
    'Mã Tỉnh/ TP',
    'Tên Quận/ Huyện',
    'Tên Tỉnh/ TP'
]
ward_headers = [
    'Mã Phường/ Xã',
    'Mã Quận/ Huyện',
    'Mã Tỉnh/TP',
    'Tên Phường/ Xã',
    'Tên Quận/ Huyện',
    'Tên Tỉnh/TP'
]

ws2.set_column(0, 40, 20)
ws2.set_row(0, 40)
for col_num, data in enumerate(province_headers):
    ws2.write(0, col_num, data, header_format)

ws3.set_column(0, 40, 20)
ws3.set_row(0, 40)
for col_num, data in enumerate(district_headers):
    ws3.write(0, col_num, data, header_format)

ws4.set_column(0, 40, 20)
ws4.set_row(0, 40)
for col_num, data in enumerate(ward_headers):
    ws4.write(0, col_num, data, header_format)

count = 1
for province in provinces:
    ws2.write_row(count, 0, province)
    count += 1
count = 1
for district in districts:
    ws3.write_row(count, 0, district)
    count += 1
count = 1
for ward in wards:
    ws4.write_row(count, 0, ward)
    count += 1
count = 1
for eth in ethnics:
    ws5.write_row(count, 0, eth)
    count += 1

workbook.close()

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

workbook = xlsxwriter.Workbook('output/data.xlsx')
worksheet = workbook.add_worksheet()

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
    'halign': 'hcenter',
    'indent': 1,
})

worksheet.set_column(0, 40, 20)
worksheet.set_row(0, 40)

headers = {
    'Last name': None,
    'Middle name': None,
    'First name': None,
    'Staff ID': None,
    'Date of Birth': None,
    'Work email': None,
    'Phone number': None,
    'Tax code': None,
    'Social code': None,
    'Government ID': None,
    'Government issued date': None,
    'Government issued place': None,
    'Passport ID': None,
    'Passport issued date': None,
    'Passport issued place': None,
    'Working status': working_status,
    'Start working date': None,
    'End working date': None,
    'User type': ['Staff', 'Teacher'],
    'Gender': ['Male', 'Female', 'Others'],
    'Permission profile': ['Default profile', 'Admin profile'],
    'Employment contract': contract_types,
    'Birthplace': None,
    'Hometown': None,
    'Ethnics': None,
    'Religion': religions,
    'Communist party status': ['True', 'False'],
    'Communist party entry date': None,
    'Trade union status': ['True', 'False'],
    'Trade union entry date': None,
    'Teaching title': teaching_titles,
    'Academic title': academic_titles,
    'Degree': degrees,
}

count = 0
for k, v in headers.items():
    worksheet.write(xl_rowcol_to_cell(0, count), k, header_format)
    if isinstance(v, list):
        worksheet.data_validation(xl_rowcol_to_cell(1, count),
                                  {'validate': 'list',
                                   'source': v})
    count += 1

workbook.close()

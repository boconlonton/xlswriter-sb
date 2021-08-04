from datetime import date, time
import xlsxwriter

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

# Set up layout of the worksheet.
worksheet.set_column('A:A', 68)
worksheet.set_column('B:B', 15)
worksheet.set_column('D:D', 15)
worksheet.set_row(0, 36)

# Write the header cells and some data that will be used in the examples.
heading1 = 'Some examples of data validation in XlsxWriter'
heading2 = 'Enter values in this column'
heading3 = 'Sample Data'

worksheet.write('A1', heading1, header_format)
worksheet.write('B1', heading2, header_format)
worksheet.write('D1', heading3, header_format)

worksheet.write_row('D3', ['Integers', 1, 10])
worksheet.write_row('D4', ['List data', 'open', 'high', 'close'])
worksheet.write_row('D5', ['Formula', '=AND(F5=50,G5=60)', 50, 60])

# Example 6. Limiting input to a value in a dropdown list.
#
txt = 'Select a value from a drop down list'

worksheet.write('A13', txt)
worksheet.data_validation('B13', {'validate': 'list',
                                  'source': ['Nam', 'Nu', 'Khac']*4})

# Example 10. Limiting input to a string greater than a fixed length.
#
txt = 'Enter a string longer than 3 characters'

worksheet.write('A21', txt)
worksheet.data_validation('B21', {'validate': 'length',
                                  'criteria': '>',
                                  'value': 3})

# Example 14. Displaying and modifying data validation messages.
#
txt = "Display a custom info message when integer isn't between 1 and 100"

worksheet.write('A29', txt)
worksheet.data_validation('B29', {'validate': 'integer',
                                  'criteria': 'between',
                                  'minimum': 1,
                                  'maximum': 100,
                                  'input_title': 'Enter an integer:',
                                  'input_message': 'between 1 and 100',
                                  'error_title': 'Input value is not valid!',
                                  'error_message':
                                  'It should be an integer between 1 and 100',
                                  'error_type': 'information'})

workbook.close()

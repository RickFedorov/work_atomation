import os
from pathlib import Path
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import tesseract4
import xlsxwriter

work_dir_path = Path(__file__).parent / 'work_dir'
# file_name = "invoice-test.pdf"
#file_name = "58001915442019.tiff"

#file_path = work_dir_path / "original" / file_name

invoice_folder = work_dir_path / "original"
templates = read_templates(work_dir_path / "templates")


# result = extract_data(str(file_path), templates=templates, input_module=tesseract4)
# print(result)

#Excel setting
def no_change(val):
    return val


def to_number(val):
    return float(val.replace(',', ''))


workbook = xlsxwriter.Workbook('invoices.xlsx')
worksheet = workbook.add_worksheet()

results = []
headers = {
    "invoice_number": (worksheet.write, no_change),
    "date":  (worksheet.write_datetime, no_change),
    "foreign_base":  (worksheet.write_number, to_number),
    "foreign_vat": (worksheet.write_number, to_number),
    "foreign_bruto": (worksheet.write_number, to_number),
    "local_base": (worksheet.write_number, to_number),
    "local_vat": (worksheet.write_number, to_number),
    "local_bruto":(worksheet.write_number, to_number),
    "exchange_rate":  (worksheet.write_number, to_number)
}

#OCR
count = 1
total = len([f for f in invoice_folder.iterdir()])
for invoice in invoice_folder.iterdir():
    print("{} / {}  invoices ...".format(count, total))
    result = extract_data(str(invoice), templates=templates, input_module=tesseract4)
    results.append(result)
    count += 1

#Export output
row = 0
col = 0

for header in headers:
    worksheet.write(row, col, header)
    col += 1
row += 1

for result in results:
    col = 0
    for header in headers:
        if header in result:
            val = result[header]
            ins = headers[header][1](val)
            headers[header][0](row, col, ins)
        col += 1
    row += 1

workbook.close()

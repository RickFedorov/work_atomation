import os
from pathlib import Path
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import tesseract4
import xlsxwriter
from my_logger import logger

logger.name = "FX"
work_dir_path = Path(__file__).parent / 'work_dir'
invoice_folder = work_dir_path / "original"
templates = read_templates(work_dir_path / "templates")

# file_name = "invoice-test.pdf"
#file_name = "57001194492019.tiff"
#file_path = work_dir_path / "original" / file_name
#result = extract_data(str(file_path), templates=templates, input_module=tesseract4)
#print(result)


#Excel setting
def no_change(val):
    return val


def to_number(val):
    return float(val.replace(',', ''))


workbook = xlsxwriter.Workbook('invoices.xlsx')
worksheet = workbook.add_worksheet()

results = []
headers = {
    "document_number": (worksheet.write, no_change),
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
    try:
        logger.info(" {} Processing ... {} / {}".format(invoice.name, count, total))
        result = extract_data(str(invoice), templates=templates, input_module=tesseract4)
        if not result:
            result = {"document_number": str(invoice.name)}
            logger.info(" {} - No template".format(invoice.name))
        else:
            result["document_number"] = invoice.name

        results.append(result)
        count += 1
    except Exception as e:
        print('Error:', e)
        logger.exception(" {} - Exception occurred...".format(invoice.name))
        continue


try:
    #Export output
    row = 0
    col = 0

    for header in headers:
        worksheet.write(row, col, header)
        col += 1
    row += 1

    val_log = 0
    for result in results:
        col = 0
        for header in headers:
            try:
                if header in result:
                    val = result[header]
                    val_log = val
                    ins = headers[header][1](val)
                    headers[header][0](row, col, ins)
            except Exception as e:
                print('Error:', e)
                logger.info(" {} - Error in processing".format(val_log))
                logger.exception(" [{},{}] - Exception occurred...".format(row, col))
                continue
            finally:
                col += 1
        row += 1
except Exception as e:
    print('Error:', e)
    logger.exception(" Excel error!")

finally:
    workbook.close()

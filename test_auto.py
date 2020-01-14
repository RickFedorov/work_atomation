from pdf_auto import pdf2text
import re
import chardet

file_name = "invoice-test.pdf"
file_path = pdf2text(file_name, "-layout")

# detect encoding
detector = chardet.UniversalDetector()
for line in open(file_path, 'rb'):
    detector.feed(line)
    if detector.done:
        break
detector.close()

# https://www.programiz.com/python-programming/regex
# https://www.w3schools.com/python/python_regex.asp
# https://docs.python.org/3/howto/regex.html
pattern = re.compile(r"(DOKLAD|INVOICE)(\D*)(?P<invoice_number>[0-9]+)", re.IGNORECASE)

for i, line in enumerate(open(file_path, encoding=detector.result['encoding'])):
    for match in re.finditer(pattern, line):
        print(str(file_path.name) + " : " + match.group("invoice_number"))

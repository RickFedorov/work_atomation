import os
from pathlib import Path
from invoice2data import extract_data
from invoice2data.extract.loader import read_templates
from invoice2data.input import tesseract4




work_dir_path = Path(__file__).parent / 'work_dir'
#file_name = "invoice-test.pdf"
file_name = "Example.tif"

file_path = work_dir_path / "original" / file_name
templates = read_templates(work_dir_path / "templates")

#result = extract_data(str(file_path), templates=templates)

result = extract_data(str(file_path), templates=templates, input_module=tesseract4)

print(result)
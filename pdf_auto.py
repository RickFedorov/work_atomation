import os
from pathlib import Path

poppler_path = Path(__file__).parent / 'poppler' / 'bin'
work_dir_path = Path(__file__).parent / 'work_dir'


def pdf2text(file_name, *args):
    separator = " "

    original_file = work_dir_path / 'original' / file_name
    new_file = (work_dir_path / 'temp' / file_name).with_suffix(".txt")

    cmd = separator.join((str(poppler_path / 'pdftotext.exe'),
                          separator.join(args),
                          str(original_file),
                          str(new_file)))

    print(cmd)
    print(os.popen(cmd))
    return new_file


file_name = "invoice-test.pdf"
pdf2text(file_name, "-layout")

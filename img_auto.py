# import the necessary packages
from pathlib import Path
import os

work_dir_path = Path(__file__).parent / 'work_dir'
tesseract_path = Path(__file__).parent / 'tesseract' / 'tesseract.exe'
file_name = "Example1.tiff"

file_path = work_dir_path / 'original' / file_name
new_file = (work_dir_path / 'temp' / file_name).with_suffix("")
separator = " "

cmd = separator.join((str(tesseract_path),
                      #separator.join(args),
                      str(file_path),
                      str(new_file)))

print(cmd)
print(os.popen(cmd))


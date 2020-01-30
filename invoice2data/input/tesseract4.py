# -*- coding: utf-8 -*-
def to_text(path, language='eng'):
    """Wraps Tesseract 4 OCR with custom language model.

    Parameters
    ----------
    path : str
        path of electronic invoice in JPG or PNG format

    Returns
    -------
    extracted_str : str
        returns extracted text from image in JPG or PNG format

    """
    import subprocess
    from distutils import spawn
    import tempfile
    import time

    tess_cmd = [r'.\tesseract\tesseract.exe', '-l', language, '--oem', '1', '--psm', '3', path,
                'stdout']
    p2 = subprocess.Popen(tess_cmd, shell=True, stdout=subprocess.PIPE)

    out, err = p2.communicate()

    extracted_str = out

    return extracted_str

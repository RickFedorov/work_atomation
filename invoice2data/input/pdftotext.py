# -*- coding: utf-8 -*-
def to_text(path):
    """Wrapper around Poppler pdftotext.

    Parameters
    ----------
    path : str
        path of electronic invoice in PDF

    Returns
    -------
    out : str
        returns extracted text from pdf

    Raises
    ------
    EnvironmentError:
        If pdftotext library is not found
    """
    import subprocess
    from distutils import spawn  # py2 compat


    out, err = subprocess.Popen(
        [r"C:\Users\lords\Documents\Python\App\Scripts\poppler\bin\pdftotext.exe", '-layout', '-enc', 'UTF-8', path, '-'],
        shell=True,
        stdout=subprocess.PIPE
    ).communicate()
    return out


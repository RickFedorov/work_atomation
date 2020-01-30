import pywinauto
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
import shelve
import time
import win32api

d = shelve.open("test.shelve")
app = pywinauto.application.Application().connect(path=r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplgpad.exe")
dlg = None

if "handle" in d:
    if app.window(handle=d["handle"]).exists(timeout=2):
        dlg = app.window(handle=d["handle"])
    else:
        dlg = app.window(title_re=".*Easy Access*")
        d["handle"] = dlg.handle
else:
    dlg = app.window(title_re=".*Easy Access*")
    d["handle"] = dlg.handle

d.close()

dlg.Edit.type_keys("/NVA03{ENTER}")
time.sleep(1)
send_keys("60210197")
menu = dlg.menu_select("Sales document->Issue Output To")
time.sleep(1)
#click(coords=(2015, 592))

for location in output_locations:
    print(location.left)

    time.sleep(1)
    #send_keys("^+{VK_F1}")



# test = app.Outputoutput.print_control_identifiers()
#test = app.Outputoutput.child_window(class_name="Afx:03860000:b").print_control_identifiers()


# send_keys("+{VK_F5}")

# test = app.window(title_re=".*Find variant*").wait('visible', timeout=5, retry_interval=1)
# test.Edit.click()

# dlg.AppToolbar.Button2.click()


# menu = dlg.menu_select("Menu->Business Workplace")

# print("sleep")
# time.sleep(3)
# print("weak")

# dlg = app.window(title_re=".*Business Workplace*").wait('visible', timeout=20, retry_interval=1)
# menu = dlg.menu_select("Folder->Find")


def main():
    pass


if __name__ == '__main__':
    main()

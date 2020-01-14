import pywinauto
import time

app = pywinauto.application.Application().connect(process=15968)
dlg = app.window(title_re=".*Easy Access*")
menu = dlg.menu_select("Menu->Business Workplace")

#print("sleep")
#time.sleep(3)
#print("weak")

dlg = app.window(title_re=".*Business Workplace*").wait('visible', timeout=20, retry_interval=1)
menu = dlg.menu_select("Folder->Find")



def main():
    pass

if __name__ == '__main__':
    main()

from display import *

from classManage import ClassManage

if __name__ == "__main__":
    welcome()
    classmanage = ClassManage()
    while True:
        classmanage.class_update()
        choice_menu()

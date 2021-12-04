from cardManage import *
from classManage import *
from studentManage import *
import os

classmanage = ClassManage()
studentManage = StudentManage()


# 欢迎词
def welcome():
    print("-- " * 2 + "欢迎使用班级小码币管理系统" + " --" * 2)
    input("please enter continue")


# 主菜单选项
def choice_menu():
    print("-- " * 2 + "输入1班级管理" + " --" * 2)
    print("-- " * 2 + "输入2学生管理" + " --" * 2)
    print("-- " * 2 + "输入3积分管理" + " --" * 2)
    print("-- " * 2 + "输入4小工具" + " --" * 2)
    print("-- " * 2 + "输入0退出系统" + " --" * 2)
    choice = int(input("请输入:"))
    if choice == 1:
        # 班级管理
        manage_class()
    elif choice == 2:
        # 学生管理
        manage_student()
    elif choice == 3:
        # 积分管理
        manage_Card()
    elif choice == 4:
        # 小工具
        tools()
    elif choice == 0:
        exit()
    else:
        os.system("cls")
        print("输入错误请重新输入!")
        choice_menu()

# 实用小工具
def tools():
    os.system('cls')
    print()
    print("\t" + "-- " * 2 + "输入1点名器" + " --" * 2)
    print("\t" + "-- " * 2 + "输入2进制转换器" + " --" * 2)
    print("\t" + "-- " * 2 + "输入3计时器" + " --" * 2)
    print("\t" + "-- " * 2 + "输入0返回主菜单" + " --" * 2)
    choice = int(input("请输入:"))
    if choice == 1:
        # 点名器
        os.system(r"gift_window.py")
    elif choice == 2:
        # 进制转换器:
        os.system(r"x_to_y_window.py")
    elif choice == 3:
        # 计时器
        os.system(r"clock_window.py")
    elif choice == 0:
        choice_menu()
    else:
        os.system("cls")
        print("输入错误请重新输入!")
        tools()

# 积分管理
def manage_Card():
    os.system('cls')
    print()
    print("\t" + "-- " * 2 + "输入1查询班级全部积分" + " --" * 2)
    print("\t" + "-- " * 2 + "输入2查询个人积分" + " --" * 2)
    print("\t" + "-- " * 2 + "输入3添加积分" + " --" * 2)
    print("\t" + "-- " * 2 + "输入4减少积分" + " --" * 2)
    print("\t" + "-- " * 2 + "输入0返回主菜单" + " --" * 2)
    choice = int(input("请输入:"))
    if choice == 1:
        # 查询班级全部积分
        select_all_Card()
        # manage_Card()
    elif choice == 2:
        # 查新个人积分
        select_student_Card()
        # manage_Card()
    elif choice == 3:
        # 添加积分
        add_Card()
        # manage_Card()
    elif choice == 4:
        # 减少积分
        del_Card()
        # manage_Card()
    elif choice == 0:
        choice_menu()
    else:
        os.system("cls")
        print("输入错误请重新输入!")
        manage_Card()


# 班级管理选项
def manage_class():
    os.system('cls')
    print()
    print("\t" + "-- " * 2 + "输入1查询全部班级" + " --" * 2)
    print("\t" + "-- " * 2 + "输入2根据班级编号查询" + " --" * 2)
    print("\t" + "-- " * 2 + "输入3添加班级" + " --" * 2)
    print("\t" + "-- " * 2 + "输入4修改班级信息" + " --" * 2)
    print("\t" + "-- " * 2 + "输入5删除班级" + " --" * 2)
    print("\t" + "-- " * 2 + "输入0返回主菜单" + " --" * 2)
    choice = int(input("请输入:"))
    if choice == 1:
        # 查询全部班级
        classmanage.select_all_class()
        # manage_class()
    elif choice == 2:
        # 根据班级编号查询
        classmanage.select_num_class()
        # manage_class()
    elif choice == 3:
        # 添加班级
        classmanage.class_add()
        # manage_class()
    elif choice == 4:
        # 修改班级信息
        classmanage.modify_class(manage_class)
        # manage_class()
    elif choice == 5:
        # 删除班级信息
        classmanage.delete_class()
        # manage_class()
    elif choice == 0:
        choice_menu()
    else:
        os.system("cls")
        print("输入错误请重新输入!")
        manage_class()


# 学生管理
def manage_student():
    os.system('cls')
    print()
    print("\t" + "-- " * 2 + "输入1查询全部学生" + " --" * 2)
    print("\t" + "-- " * 2 + "输入2添加学生" + " --" * 2)
    print("\t" + "-- " * 2 + "输入3删除学生" + " --" * 2)
    print("\t" + "-- " * 2 + "输入4转移学生" + " --" * 2)
    print("\t" + "-- " * 2 + "输入0返回主菜单" + " --" * 2)
    choice = int(input("请输入:"))
    if choice == 1:
        # 查询全部学生
        studentManage.select_all_student()
        pass
    elif choice == 2:
        # 添加学生
        pass
    elif choice == 3:
        # 删除学生
        pass
    elif choice == 4:
        # 转移学生
        pass
    elif choice == 0:
        choice_menu()
    else:
        os.system("cls")
        print("输入错误请重新输入!")
        manage_student()

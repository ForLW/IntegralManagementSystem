from classManage import *

classmanage = ClassManage()


# 查询班级中全部学生的积分
def select_all_Card(class_num=0):
    os.system('cls')
    print()
    classmanage.class_update()
    student_dict = {}
    if class_num == 0:
        class_num = input("请输入要查询的班级编号:")
    if class_num in classmanage.class_dict:
        print()
        student_dict = classmanage.class_dict[class_num]
        print(class_num)
        print("{: <5}{:　<12}{}".format("编号", "姓名", "积分"))
        print("-" * 35)
        index = 1
        for j in student_dict:
            print("{: <6}{:　<12}{}".format(index, j, student_dict[j]))
            print("-" * 35)
            index += 1
            # print( pd.DataFrame(student_dict) )
        print()


# 查询个人积分
def select_student_Card(class_num=0):
    classmanage.class_update()
    student_dict = {}
    if class_num == 0:
        class_num = input("请输入要查询的班级编号:")

    if class_num in classmanage.class_dict:
        student_dict = classmanage.class_dict[class_num]
        student_name = input("请输入要查询的学生姓名:")
        if student_name in student_dict:
            print()
            print(class_num)
            print("{:　^15}{}".format("姓名", "积分"))
            print("{:　^15}{}".format(student_name, student_dict[student_name]))
            print()


# 添加积分
def add_Card(class_num=0):
    classmanage.class_update()
    if class_num == 0:
        class_num = input("请输入要添加积分的学生班级编号:")
    if class_num in classmanage.class_dict:
        select_all_Card(class_num)
        student_dict = classmanage.class_dict[class_num]
        student_index = int(input("请输入要添加积分的学生编号:"))
        if student_index == 0:
            return
        index = 0
        for i in student_dict:
            # print(i)
            index += 1
            if index == student_index:
                add_card_num = input("请输入要添加多少积分:")
                student_dict[i] = \
                    str(int(student_dict[i]) + int(add_card_num))
                os.chdir(class_path)
                file = open(class_num, "w")
                for i in student_dict:
                    file.write("{:　<15}{}\n".format(i, student_dict[i]))
                file.close()
                os.chdir("..")
        add_Card(class_num)
        # classmanage.class_update()


# 减少积分
def del_Card(class_num=0):
    classmanage.class_update()
    if class_num == 0:
        class_num = input("请输入要减少积分的学生班级编号:")
    if class_num in classmanage.class_dict:
        select_all_Card(class_num)
        student_dict = classmanage.class_dict[class_num]
        student_index = int(input("请输入要减少积分的学生编号:"))
        if student_index == 0:
            return
        index = 0
        for i in student_dict:
            # print(i)
            index += 1
            if index == student_index:
                add_card_num = input("请输入要减少多少积分:")
                student_dict[i] = \
                    str(int(student_dict[i]) - int(add_card_num))
                os.chdir(class_path)
                file = open(class_num, "w")
                for i in student_dict:
                    file.write("{:　<15}{}\n".format(i, student_dict[i]))
                file.close()
                os.chdir("..")
        del_Card(class_num)
        # classmanage.class_update()

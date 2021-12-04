from pathlib import Path
import os

class_path = Path("班级编号")


class ClassManage():
    def __init__(self):
        self.class_num_list = []
        self.student_List = []
        self.class_dict = {}

    # 班级信息更新
    def class_update(self):
        if os.path.exists(class_path) and os.path.isfile(class_path) == False:
            os.chdir(class_path)
            if os.path.exists("班级编号") and os.path.isfile("班级编号"):
                class_num_file = open("班级编号", "r")
                class_num_list = list(class_num_file.read().split())
                self.class_num_list = class_num_list
                # print(class_num_list)
                for i in class_num_list:
                    # print(i)
                    class_file = open(i, "r")
                    student_List = list(class_file.read().split())
                    # print(student_List)
                    temp_dict = {}
                    for j in range(0, len(student_List), 2):
                        temp_dict[student_List[j]] = student_List[j + 1]

                    self.class_dict[i] = temp_dict
                    class_file.close()
                # print(class_dict)
            else:
                class_num_file = open("班级编号", "w")
                class_num_file.close()
            os.chdir("..")
        else:
            os.mkdir(class_path)
            os.chdir(class_path)
            class_num_file = open("班级编号", "w")
            class_num_file.close()
            os.chdir("..")

    # 添加班级
    def class_add(self):
        class_number = input("请输入要创建的班级编号:")
        os.chdir(class_path)
        class_num_file = open("班级编号", "a")
        class_num_file.write(class_number + "\n")
        print("班级编号添加成功")
        print("请添加学生，结束请输入0")
        student_List = []
        while True:
            student_name = input("请输入学生:")
            if student_name == "0":
                break
            if len(student_name) > 15:
                print("你这名字也太长了吧")
                continue
            student_List.append(student_name)

        os.chdir("..")
        content = ""
        for i in student_List:
            content += "{:　<15}0\n".format(i)
        self.write_class_dict(class_number, content)
        # class_file = open(class_number, "w")
        # for i in student_List:
        #     class_file.write("{:　<15}0\n".format(i))
        # class_num_file.close()
        # os.chdir("..")

    # 查询全部班级
    def select_all_class(self):
        os.system('cls')
        print()
        self.class_update()
        class_num = ""
        student_dict = {}
        print()
        for i in self.class_dict:
            class_num = i
            print(class_num)
            student_dict = self.class_dict[class_num]
            print("{: <5}{:　<12}{}".format("编号", "姓名", "积分"))
            print("-" * 35)
            index = 1
            for j in student_dict:
                print("{: <6}{:　<12}{}".format(index, j, student_dict[j]))
                print("-" * 35)
                index += 1
            # print( pd.DataFrame(student_dict) )
        print()

    # 根据编号查询班级
    def select_num_class(self):
        self.class_update()
        class_num = ""
        student_dict = {}
        class_num = input("请输入要查询的班级编号:")
        if class_num in self.class_dict:
            print()
            student_dict = self.class_dict[class_num]
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

    # 删除班级
    def delete_class(self):
        self.class_update()
        class_num = input("请输入要删除的班级编号:")
        answer = input("确认要删除{}吗？(输入y|Y确认):".format(class_num))
        if answer == "y" or answer == "Y":
            if class_num in self.class_dict:
                del self.class_dict[class_num]
                self.class_num_list.remove(class_num)
            os.chdir(class_path)
            try:
                os.remove("班级编号")
            except:
                print("删除班级编号文件失败")
            class_num_file = open("班级编号", "w")
            for i in self.class_num_list:
                class_num_file.write("{}\n".format(i))
            try:
                os.remove(class_num)
            except:
                print("删除班级文件失败")
            else:
                print("班级删除成功")
            class_num_file.close()
            os.chdir("..")

    # 修改班级
    def modify_class(self, manage_class):
        os.system('cls')
        print()
        print("\t" + "-- " * 2 + "输入1修改班级编号" + " --" * 2)
        print("\t" + "-- " * 2 + "输入0返回班级管理" + " --" * 2)
        choice = int(input("请输入:"))
        if choice == 1:
            pass
        elif choice == 0:
            manage_class()
        else:
            os.system("cls")
            print("输入错误请重新输入!")
            self.modify_class(manage_class)

    # 写入文件
    @staticmethod
    def write_class_dict(filename, content):
        os.chdir(class_path)
        file = open(filename, "w")
        file.write(content)
        file.close()
        os.chdir("..")

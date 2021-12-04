from pathlib import Path
import os

class_path = Path("班级编号")


class StudentManage():
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
                self.class_num_list = list(class_num_file.read().split())
                # print(class_num_list)
                for i in self.class_num_list:
                    # print(i)
                    class_file = open(i, "r")
                    self.student_List = list(class_file.read().split())
                    # print(student_List)
                    temp_dict = {}
                    for j in range(0, len(self.student_List), 2):
                        temp_dict[self.student_List[j]] = self.student_List[j + 1]

                    self.class_dict[i] = temp_dict
                    self.student_List = []
                    for num in self.class_dict:
                        tempDict = self.class_dict[num]
                        for name in tempDict:
                            self.student_List.append(name)

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

    def test(self):
        self.class_update()
        print(self.student_List)
        print("----")
        print(self.class_num_list)
        print("----")
        print(self.class_dict)

    def select_all_student(self):
        os.system('cls')
        print()
        self.class_update()
        count = 0
        for name in self.student_List:
            count += 1
            print("{:　<8}".format(name), end="")
            if count % 5 == 0:
                print()
        print()
import tkinter

student_dict = {"小码君": 8, "小码酱": 7}


def button_select_all_click():
    a = tkinter.Tk()
    a.title("学生信息")
    a.geometry("300x400")
    label = tkinter.Label(a)
    res = ""
    for name in student_dict:
        res = res + name + "\t\t" + str(student_dict[name]) + "\n\n"
    label["text"] = res
    label["font"] = ("楷体", 20)
    label.pack(pady=50)


class Application(tkinter.Frame):
    def __init__(self, root=None):
        master = tkinter.Tk()
        master.title("学生管理")
        master.geometry("400x600+400+100")
        super().__init__(master)
        self.master = master
        self.root = root
        self.pack()
        self.label = tkinter.Label(self.master)
        self.button_select_all = tkinter.Button(self.master)
        self.button_add = tkinter.Button(self.master)
        self.button_del = tkinter.Button(self.master)
        self.button_back = tkinter.Button(self.master)

        self.create()

    def create(self):
        self.label["text"] = "学生管理"
        self.label["font"] = ("楷体", 30)
        self.label.pack(pady=50)

        self.button_select_all["text"] = "查询全部"
        self.button_select_all["font"] = ("楷体", 20)
        self.button_select_all["width"] = 20
        self.button_select_all["command"] = button_select_all_click
        self.button_select_all.pack(pady=20)

        self.button_add["text"] = "添加学生"
        self.button_add["font"] = ("楷体", 20)
        self.button_add["width"] = 20
        self.button_add.pack(pady=20)

        self.button_del["text"] = "删除学生"
        self.button_del["font"] = ("楷体", 20)
        self.button_del["width"] = 20
        self.button_del.pack(pady=20)

        self.button_back["text"] = "返回主菜单"
        self.button_back["font"] = ("楷体", 20)
        self.button_back["width"] = 20
        self.button_back["command"] = self.button_back_click
        self.button_back.pack(pady=20)

    def button_back_click(self):
        self.master.destroy()
        self.root.deiconify()

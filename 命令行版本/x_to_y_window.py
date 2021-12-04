from tkinter import ttk
from tkinter import messagebox
from tkinter import *


# 将任意2~16进制字符串转换成10进制
def x_to_num(num, x):
    num_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
                "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
    i = 0
    res = 0
    while len(num) > 0:
        temp = num[-1]
        if temp in num_dict:
            temp = num_dict[temp]
        else:
            temp = int(temp)
        num = num[0:-1]
        res += temp * x ** i
        i += 1
    return res


# 把10进制数转换成任意2~16进制字符串
def num_to_x_str(num, x):
    res = []
    res_str = ""
    num_dict = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    if 2 <= x <= 16:
        while num > 0:
            if num % x < 10:
                res.append(num % x)
            else:
                res.append(num_dict[num % x])
            num //= x
        res.reverse()
    else:
        return None
    for i in res:
        res_str += str(i)
    return res_str


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.label1 = Label(self)
        self.frame1 = Frame(self)
        self.entryStart = Entry(self.frame1)
        self.com1 = ttk.Combobox(self.frame1)

        self.frame2 = Frame(self)
        self.entryEnd = Entry(self.frame2)
        self.com2 = ttk.Combobox(self.frame2)

        self.button1 = Button(self)

        self.label1.pack(pady=50)
        self.entryStart.pack(side=LEFT)
        self.com1.pack(side=RIGHT)
        self.frame1.pack(pady=50)
        self.entryEnd.pack(side=LEFT)
        self.com2.pack(side=RIGHT)
        self.frame2.pack(pady=50)
        self.button1.pack(pady=50)

        self.create()
        self.label1.bind("<Key>", self.test_to)

    def create(self):
        self.label1["text"] = "万能进制转换器"
        self.label1["font"] = ("楷体", 30)
        self.entryStart.config(
            bd=5, width=20, font=("楷体", 20), fg="red"
        )
        self.entryEnd.config(
            bd=5, width=20, font=("楷体", 20), fg="red"
            # , state='readonly'
        )
        values = [str(i) + "进制" for i in range(2, 17)]
        self.com1.config(
            height=10,  # 高度,下拉显示的条目数量
            width=6,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('楷体', 15),  # 字体
            textvariable=StringVar(),  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
        )
        self.com2.config(
            height=10,  # 高度,下拉显示的条目数量
            width=6,  # 宽度
            state='readonly',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('楷体', 15),  # 字体
            textvariable=StringVar(),  # 通过StringVar设置可改变的值
            values=values,  # 设置下拉框的选项
        )
        self.com1.current(8)  # 默认10进制
        self.com2.current(0)  # 默认2进制
        self.button1.config(
            text="转换", font=("楷体", 20), command=self.test_to
        )
        self.entryStart.focus_set()

    # 按钮点击事件
    def test_to(self, event=None):
        num_dict = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15,
                    "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}
        entryStartText = self.entryStart.get()
        if entryStartText == "":
            messagebox.showwarning("警告", "请输入要转换的数字")
        else:
            com1Text = self.com1.get()
            if len(com1Text) == 3:
                x1 = int(com1Text[0])
            elif len(com1Text) == 4:
                x1 = int(com1Text[0:2])
            com2Text = self.com2.get()
            if len(com2Text) == 3:
                x2 = int(com2Text[0])
            elif len(com2Text) == 4:
                x2 = int(com2Text[0:2])
            for i in entryStartText:
                if i in num_dict:
                    temp = num_dict[i]
                else:
                    temp = int(i)
                if temp >= x1:
                    messagebox.showwarning("警告", "输入的不是" + str(x1) + "进制数字")
                    break
            else:
                entryEndText = num_to_x_str(x_to_num(entryStartText, x1), x2)
                # print(entryEndText)
                self.entryEnd.delete(0, "end")
                self.entryEnd.insert("end", entryEndText)


def test(event):
    app.test_to()


if __name__ == '__main__':
    root = Tk()
    root.title("进制转换器")
    root.geometry("400x600")
    app = Application(root)
    root.bind("<Key>", test)
    app.mainloop()

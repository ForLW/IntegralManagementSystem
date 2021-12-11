import tkinter
from tkinter import ttk


class Application(tkinter.Frame):
    def __init__(self, root=None):
        self.master = tkinter.Tk()
        self.master.title("积分管理")
        self.master.geometry("400x600+400+100")
        super(Application, self).__init__(self.master)
        self.root = root
        self.pack()
        self.label_title = tkinter.Label(self)

        self.frame1 = tkinter.Frame(self)
        self.com_number = ttk.Combobox(self.frame1)
        self.button_select_class = tkinter.Button(self.frame1)

        self.button_back = tkinter.Button(self)

        self.create()

    def create(self):
        self.label_title["text"] = "积分管理"
        self.label_title["font"] = ("楷体", 30)
        self.label_title.pack(pady=50)

        self.com_number.config(
            height=10,  # 高度,下拉显示的条目数量
            width=15,  # 宽度
            state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('楷体', 20),  # 字体
            textvariable=tkinter.StringVar(),  # 通过StringVar设置可改变的值
            values="",  # 设置下拉框的选项
        )
        self.com_number.pack(side=tkinter.LEFT)
        self.button_select_class["text"] = "查询"
        self.button_select_class["font"] = ("楷体", 20)
        self.button_select_class["width"] = 5
        self.button_select_class.pack(side=tkinter.RIGHT)
        self.frame1.pack(pady=20)

        self.button_back["text"] = "返回主菜单"
        self.button_back["font"] = ("楷体", 20)
        self.button_back["width"] = 20
        self.button_back["command"] = self.button_back_click
        self.button_back.pack(pady=10)

        self.mainloop()

    def button_back_click(self):
        self.master.destroy()
        self.root.deiconify()


if __name__ == '__main__':
    Application()

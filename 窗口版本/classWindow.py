import tkinter
from tkinter import ttk


class Application(tkinter.Frame):
    def __init__(self, root=None):
        master = tkinter.Tk()
        master.title("班级管理")
        master.geometry("400x600+400+100")
        super().__init__(master)
        self.master = master
        self.root = root
        self.pack()
        self.label_title = tkinter.Label(self)

        self.button_select_all = tkinter.Button(self)

        self.frame_select = tkinter.Frame(self)
        self.com_select_num = ttk.Combobox(self.frame_select)
        self.button_select_num = tkinter.Button(self.frame_select)

        self.frame_add = tkinter.Frame(self)
        self.entry_add_num = tkinter.Entry(self.frame_add)
        self.button_add = tkinter.Button(self.frame_add)

        self.frame_modify = tkinter.Frame(self)
        self.com_modify_num = ttk.Combobox(self.frame_modify)
        self.button_modify = tkinter.Button(self.frame_modify)

        self.frame_del = tkinter.Frame(self)
        self.com_del_num = ttk.Combobox(self.frame_del)
        self.button_del = tkinter.Button(self.frame_del)

        self.button_back = tkinter.Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title["text"] = "班级管理"
        self.label_title["font"] = ("楷体", 30)
        self.label_title.pack(pady=40)
        self.label_title.pack(expand=1)

        self.button_select_all["text"] = "查询全部"
        self.button_select_all["font"] = ("楷体", 20)
        self.button_select_all["width"] = 20
        self.button_select_all["command"] = self.button1_click
        self.button_select_all.pack(pady=10)

        self.com_select_num.config(
            height=10,  # 高度,下拉显示的条目数量
            width=15,  # 宽度
            state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('楷体', 20),  # 字体
            textvariable=tkinter.StringVar(),  # 通过StringVar设置可改变的值
            values="",  # 设置下拉框的选项
        )
        self.com_select_num.pack(side=tkinter.LEFT)
        self.button_select_num["text"] = "查询"
        self.button_select_num["font"] = ("楷体", 20)
        self.button_select_num["width"] = 5
        self.button_select_num["command"] = self.button2_click
        self.button_select_num.pack(side=tkinter.RIGHT)
        self.frame_select.pack(pady=10)

        self.entry_add_num["font"] = ("楷体", 20)
        self.entry_add_num["width"] = 15
        self.entry_add_num.pack(side=tkinter.LEFT)
        self.button_add["text"] = "添加"
        self.button_add["font"] = ("楷体", 20)
        self.button_add["width"] = 5
        self.button_add["command"] = self.button3_click
        self.button_add.pack(side=tkinter.RIGHT)
        self.frame_add.pack(pady=10)

        self.com_modify_num.config(
            height=10,  # 高度,下拉显示的条目数量
            width=15,  # 宽度
            state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('楷体', 20),  # 字体
            textvariable=tkinter.StringVar(),  # 通过StringVar设置可改变的值
            values="",  # 设置下拉框的选项
        )
        self.com_modify_num.pack(side=tkinter.LEFT)
        self.button_modify["text"] = "修改"
        self.button_modify["font"] = ("楷体", 20)
        self.button_modify["width"] = 5
        self.button_modify["command"] = self.button3_click
        self.button_modify.pack(side=tkinter.RIGHT)
        self.frame_modify.pack(pady=10)

        self.com_del_num.config(
            height=10,  # 高度,下拉显示的条目数量
            width=15,  # 宽度
            state='normal',  # 设置状态 normal(可选可输入)、readonly(只可选)、 disabled
            cursor='arrow',  # 鼠标移动时样式 arrow, circle, cross, plus...
            font=('楷体', 20),  # 字体
            textvariable=tkinter.StringVar(),  # 通过StringVar设置可改变的值
            values="",  # 设置下拉框的选项
        )
        self.com_del_num.pack(side=tkinter.LEFT)
        self.button_del["text"] = "删除"
        self.button_del["font"] = ("楷体", 20)
        self.button_del["width"] = 5
        self.button_del["command"] = self.button3_click
        self.button_del.pack(side=tkinter.RIGHT)
        self.frame_del.pack(pady=10)

        self.button_back["text"] = "返回主菜单"
        self.button_back["font"] = ("楷体", 20)
        self.button_back["width"] = 20
        self.button_back["command"] = self.button_back_click
        self.button_back.pack(pady=10)

        self.mainloop()

    def button1_click(self):
        pass

    def button2_click(self):
        pass

    def button3_click(self):
        pass

    def button4_click(self):
        pass

    def button_back_click(self):
        self.master.destroy()
        self.root.deiconify()


if __name__ == '__main__':
    Application()

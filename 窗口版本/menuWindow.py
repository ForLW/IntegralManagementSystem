import tkinter
import toolsWindow
import classWindow
import studentWindow
import cardWindow


class Application(tkinter.Frame):
    def __init__(self, master=None):
        master = tkinter.Tk()
        master.title("积分管理系统")
        master.geometry("400x600+400+100")
        super().__init__(master)
        self.master = master
        self.pack()
        self.label_title = tkinter.Label(self)
        self.button1 = tkinter.Button(self)
        self.button2 = tkinter.Button(self)
        self.button3 = tkinter.Button(self)
        self.button4 = tkinter.Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title["text"] = "积分管理系统"
        self.label_title["font"] = ("楷体", 30)
        self.label_title.pack(pady=60)
        self.label_title.pack(expand=1)

        self.button1["text"] = "班级管理"
        self.button1["font"] = ("楷体", 20)
        self.button1["width"] = 20
        self.button1["command"] = self.button1_click
        self.button1.pack(pady=20)

        self.button2["text"] = "学生管理"
        self.button2["font"] = ("楷体", 20)
        self.button2["width"] = 20
        self.button2["command"] = self.button2_click
        self.button2.pack(pady=20)

        self.button3["text"] = "积分管理"
        self.button3["font"] = ("楷体", 20)
        self.button3["width"] = 20
        self.button3["command"] = self.button3_click
        self.button3.pack(pady=20)

        self.button4["text"] = "小工具"
        self.button4["font"] = ("楷体", 20)
        self.button4["width"] = 20
        self.button4["command"] = self.button4_click
        self.button4.pack(pady=20)

        self.mainloop()

    def button1_click(self):
        self.master.withdraw()
        classWindow.Application(self.master)

    def button2_click(self):
        self.master.withdraw()
        studentWindow.Application(self.master)

    def button3_click(self):
        self.master.withdraw()
        cardWindow.Application(self.master)

    def button4_click(self):
        self.master.withdraw()
        toolsWindow.Application(self.master)

# if __name__ == '__main__':
#     root = tkinter.Tk()
#     root.title("积分管理系统")
#     root.geometry("400x600")
#     app = Application(root)
#     app.mainloop()

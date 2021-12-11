import tkinter


class Application(tkinter.Frame):
    def __init__(self, root=None):
        master = tkinter.Tk()
        master.title("小工具集")
        master.geometry("400x600+400+100")
        super().__init__(master)
        self.master = master
        self.root = root
        self.pack()
        self.label_title = tkinter.Label(self)
        self.button1 = tkinter.Button(self)
        self.button2 = tkinter.Button(self)
        self.button3 = tkinter.Button(self)
        self.button4 = tkinter.Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title["text"] = "小工具集"
        self.label_title["font"] = ("楷体", 30)
        self.label_title.pack(pady=60)
        self.label_title.pack(expand=1)

        self.button1["text"] = "点名器"
        self.button1["font"] = ("楷体", 20)
        self.button1["width"] = 20
        self.button1["command"] = self.button1_click
        self.button1.pack(pady=20)

        self.button2["text"] = "进制转换器"
        self.button2["font"] = ("楷体", 20)
        self.button2["width"] = 20
        self.button2["command"] = self.button2_click
        self.button2.pack(pady=20)

        self.button3["text"] = "计时器"
        self.button3["font"] = ("楷体", 20)
        self.button3["width"] = 20
        self.button3["command"] = self.button3_click
        self.button3.pack(pady=20)

        self.button4["text"] = "返回主菜单"
        self.button4["font"] = ("楷体", 20)
        self.button4["width"] = 20
        self.button4["command"] = self.button4_click
        self.button4.pack(pady=20)

        self.mainloop()

    def button1_click(self):
        pass

    def button2_click(self):
        pass

    def button3_click(self):
        pass

    def button4_click(self):
        self.master.destroy()
        self.root.deiconify()

# if __name__ == '__main__':
#     root = tkinter.Tk()
#     root.title("小工具集")
#     root.geometry("400x600")
#     app = Application(root)
#     app.mainloop()

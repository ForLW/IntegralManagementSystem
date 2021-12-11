import tkinter
import time
from tkinter import messagebox


class Appliaction(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.label_title = tkinter.Label(self)
        self.label_time = tkinter.Label(self)
        self.button1 = tkinter.Button(self)
        self.create_widgets()

    def create_widgets(self):
        self.label_title["text"] = "计时器"
        self.label_title["font"] = ("楷体", 30)
        self.label_title.pack(pady=50)
        self.label_title.pack(expand=1)

        self.label_time["text"] = time.time()
        self.label_time["font"] = ("楷体", 20)
        self.label_time.pack(pady=20)

        self.button1["text"] = "计时"
        self.button1["font"] = ("楷体", 20)
        self.button1["command"] = self.click_thing
        self.button1.pack(pady=50)

        while True:
            self.label_time["text"] = time.time()
            self.label_time.update()
            time.sleep(0.1)

    def click_thing(self):
        messagebox.showinfo("信息", "点击事件")


root = tkinter.Tk()
root.title("计时器")
root.geometry("400x600")
app = Appliaction(root)
app.mainloop()

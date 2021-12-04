from tkinter import *
from tkinter import ttk
import time
import random
import pygame

pygame.mixer.init()
sound1 = pygame.mixer.Sound(".\\music\\gift.mp3")
sound2 = pygame.mixer.Sound(".\\music\\掌声.wav")


class My_GUI():
    def __init__(self, window, label, button):
        self.window = window
        self.label = label
        self.button = button
        self.coin = 0
        self.nameList = []
        self.number = ""
        if self.number == "":
            self.number = input("请输入班级编号:")
        self.get_name()

    def get_name(self):
        f = open(".\\班级编号\\" + self.number)
        tempList = f.readlines()
        f.close()
        for i in tempList:
            self.nameList.append(i.split("　")[0])

    def button_click(self):
        if self.coin == 0:
            self.coin = 1
            sound1.play()
            self.button.configure(text="停止")
            self.button.update()
        else:
            self.coin = 0
            self.button.forget()
            self.button.update()
            for i in range(1, random.randint(4, 7)):
                name = self.nameList[random.randint(0, len(self.nameList) - 1)]
                self.label.configure(text=name)
                time.sleep(random.randint(2, 4) / 10 * i)
                self.label.update()
            name = self.nameList.pop(random.randint(0, len(self.nameList) - 1))
            self.label.configure(text="恭喜:" + name)
            self.label.update()
            if not self.nameList:
                self.get_name()
            sound1.stop()
            sound2.play()
            self.button.configure(text="开始")
            self.button.pack(pady=100)
            self.button.update()
        while True:
            if self.coin == 0:
                break
            name = self.nameList[random.randint(0, len(self.nameList) - 1)]
            self.label.configure(text=name)
            self.label.update()
            time.sleep(0.05)


top = Tk()
top.title("点名器")
top.geometry("600x400")
label1 = Label(top, text="点击按钮开始，再点击停止", font=("楷体", 30))
label1.pack(pady=50)
button1 = Button(top, text="开始", font=("楷体", 30))
button1.pack()

gui = My_GUI(top, label1, button1)
gui.button.configure(command=gui.button_click)
top.mainloop()

from tkinter import *
from tkinter import messagebox
import time
import random

root = Tk()
root.resizable(width="False", height="False")

point = 0
count = 0
x=0
y=0
photo_1 = PhotoImage(file = "back.gif")
photo_17 = PhotoImage(file = "nether.gif")
photo_18 = PhotoImage(file = "burk.gif")
photo_19 = PhotoImage(file = "austria.gif")
photo_20 = PhotoImage(file = "aa.gif")
photo_21 = PhotoImage(file = "denmark.gif")
photo_22 = PhotoImage(file = "espa.gif")
photo_23 = PhotoImage(file = "hung.gif")
photo_24 = PhotoImage(file = "ice.gif")

def change_card_1():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_1.config(image=photo_17)
        image_1.image=photo_17
        image_1.update()
        if(count==1):
            x=1
        elif(count==2):
            y=1
            compare_card()
            count = 0

def change_card_2():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_2.config(image=photo_18)
        image_2.image=photo_18
        image_2.update()
        if(count==1):
            x=2
        elif(count==2):
            y=2
            compare_card()
            count = 0
            
def change_card_3():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_3.config(image=photo_19)
        image_3.image=photo_19
        image_3.update()
        if(count==1):
            x=3
        elif(count==2):
            y=3
            compare_card()
            count = 0

def change_card_4():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_4.config(image=photo_20)
        image_4.image=photo_20
        image_4.update()
        if(count==1):
            x=4
        elif(count==2):
            y=4
            compare_card()
            count=0

def change_card_5():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_5.config(image=photo_21)
        image_5.image=photo_21
        image_5.update()
        if(count==1):
            x=5
        elif(count==2):
            y=5
            compare_card()
            count = 0
def change_card_6():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_6.config(image=photo_22)
        image_6.image=photo_22
        image_6.update()
        if(count==1):
            x=6
        elif(count==2):
            y=6
            compare_card()
            count = 0
            
def change_card_7():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_7.config(image=photo_23)
        image_7.image=photo_23
        image_7.update()
        if(count==1):
            x=7
        elif(count==2):
            y=7
            compare_card()
            count = 0

def change_card_8():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_8.config(image=photo_24)
        image_8.image=photo_24
        image_8.update()
        if(count==1):
            x=8
        elif(count==2):
            y=8
            compare_card()
            count = 0

def change_card_9():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_9.config(image=photo_17)
        image_9.image=photo_17
        image_9.update()
        if(count==1):
            x=9
        elif(count==2):
            y=9
            compare_card()
            count = 0
        

def change_card_10():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_10.config(image=photo_18)
        image_10.image=photo_18
        image_10.update()
        if(count==1):
            x=10
        elif(count==2):
            y=10
            compare_card()
            count = 0
        

def change_card_11():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_11.config(image=photo_19)
        image_11.image=photo_19
        image_11.update()
        if(count==1):
            x=11
        elif(count==2):
            y=11
            compare_card()
            count = 0

def change_card_12():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_12.config(image=photo_20)
        image_12.image=photo_20
        image_12.update()
        if(count==1):
            x=12
        elif(count==2):
            y=12
            compare_card()
            count = 0

def change_card_13():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_13.config(image=photo_21)
        image_13.image=photo_21
        image_13.update()
        if(count==1):
            x=13
        elif(count==2):
            y=13
            compare_card()
            count = 0

def change_card_14():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_14.config(image=photo_22)
        image_14.image=photo_22
        image_14.update()
        if(count==1):
            x=14
        elif(count==2):
            y=14
            compare_card()
            count = 0
    
def change_card_15():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_15.config(image=photo_23)
        image_15.image=photo_23
        image_15.update()
        if(count ==1):
            x=15
        elif(count==2):
            y=15
            compare_card()
            count = 0

    
def change_card_16():
    global count
    global x
    global y
    global point
    if(count<2):
        count = count + 1
        image_16.config(image=photo_24)
        image_16.image=photo_24
        image_16.update()
        if(count==1):
            x=16
        elif(count==2):
            y=16
            compare_card()
            count = 0

def compare_card():
    global x, y, count, point
    exec("if image_%d['image'] == image_%d['image']:\n\tinc_point()\nelse:\n\ttime.sleep(0.5)\n\tinitialize()" % (x, y))
    if(point==8):
        messagebox.showinfo("축하합니다.", "게임에서 이기셨습니다.")
        point=0
    x=0
    y=0
    count = 0
def inc_point():
    global point
    point+=1
def init():
    initialize()
    indexs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    for i in range(1,17, 1):
        exec("image_%d.grid(row=%d, column=%d)" % (indexs.pop(random.randint(1,len(indexs))-1), (i-1)//4, (i-1)%4))
def initialize():
    global point
    for i in range(1,17, 1):
        exec("image_%d.config(image=photo_1)" % (i))
        exec("image_%d.image=photo_1" % (i))
        exec("image_%d.update()" % (i))
    point = 0

       
Reset = Button(root, text = "RESET", width = 13, command = init).grid(row= 5, column =1,columnspan = 2)

photo_1 = PhotoImage(file = "back.gif")
indexs=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
for i in range(1,17, 1):
    exec("image_%d = Button(root, image = photo_1, command=change_card_%d)" % (i, i))
for i in range(1,17, 1):
    exec("image_%d.grid(row=%d, column=%d)" % (indexs.pop(random.randint(1,len(indexs))-1), (i-1)//4, (i-1)%4))

root.mainloop()


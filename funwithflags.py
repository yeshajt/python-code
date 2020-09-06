#===Tkinter/ Python Assignment #3: Fun With Flags!===
from Tkinter import *

win = Tk()

#Step 1
c = Canvas(win, width = 800, height = 600, bg = "royal blue")
c.pack()
color = "dark violet"

#Step 3
def american():
    #Step 4
    for i in range(13):
        upper = 180 + 20.*i
        lower = 180 + 20.*(i + 1)
        if i % 2 == 0:
            color = "red"
        else:
            color = "white"

        c.create_rectangle(200, lower, 600, upper, outline = color, \
                           fill = color)
    c.create_rectangle(200,180,400,320, fill = "navy blue")
    for i in range(9):
        if i % 2 == 0:
            num = 6
            bump = 0
        else:
            num = 5
            bump = 17
        for j in range(num):
            p1x = 208 + 34*j + bump
            p1y = 196 + 14*i
            p2x = p1x + 4
            p2y = p1y - 12
            p3x = p1x + 8
            p3y = p1y
            p4x = p1x - 2
            p4y = p1y - 7
            p5x = p1x + 10
            p5y = p1y - 7
            c.create_polygon(p1x, p1y, p2x, p2y, p3x, p3y,p4x, p4y, p5x, p5y, \
                             width = 3, fill = "white")
def olympic():
    #Step 5
    lower = 440
    upper = 180
    c.create_rectangle(200,lower,600,upper, outline = "white", fill = "white")
    c.create_oval(240,225,340,325, width = 9, outline = "medium blue")
    c.create_oval(350,225,450,325, width = 9, outline = "black")
    c.create_oval(460,225,560,325, width = 9, outline = "red")
    c.create_oval(295,275,395,375, width = 9, outline = "yellow")
    c.create_oval(405,275,505,375, width = 9, outline = "lime green")

def brazilian():
    #Step 6
    lower = 440
    upper = 180
    color = "lime green"
    c.create_rectangle(200,lower,600,upper, outline = color, fill = color)
    color = "yellow"
    c.create_polygon(220,310,400, upper + 20, 580, 310, 400, lower - 20, \
                     outline = color, fill = color)
    color = "navy blue"
    c.create_oval(340,250,460,370, width = 9, outline = color, fill = color)
    color = "white"
    c.create_arc(180,290,500,560, style = ARC, start = 41.2, extent = 48.7, \
                 width = 9, outline = color, fill = color)

#Step 2
color = "dark violet"
button1 = Button(c, text = "American Flag", background = color, \
                 command = american)
button1.place(x = 160, y = 530)

button2 = Button(c, text = "Olympic Flag", backgroun = color, \
                 command = olympic)
button2.place(x = 360, y = 530)

button3 = Button(c, text = "Brazilian Flag", backgroun = color, \
                 command = brazilian)
button3.place(x = 560, y = 530)



win.lift()
win.mainloop()

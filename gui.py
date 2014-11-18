from Tkinter import *
import tkFileDialog
import os

rect_width = 100
rect_height = 50

rect_space = 200
line_space = 300
top_margin = 25
left_margin = 50

rect1_line_x = 0
rect1_line_y = 0

rect2_line_x = 0
rect2_line_y = 0

rect3_line_x = 0
rect3_line_y = 0

last_line_y = 90

d = [(0,'none'),(1,'first'),(2,'last'),(3,'both')]
test_t = [1,2,3,4,3,2,1,1,2,3,4,2,3,1,3,4]



class GuiApp():
    def __init__(self):
        self.master = Tk()
        self.master.resizable(width=FALSE, height=FALSE)
        self.frame = Frame(self.master)
        self.frame.pack()

        #s = Scrollbar(frame)
        self.canvas = Canvas(self.frame, width=800, height=600)

        #self.canvas.config(scrollregion=self.canvas.bbox(ALL))
        self.canvas.config(scrollregion=(0,0,800,2100))
        menubar = Menu(self.frame)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)
        #self.master.mainloop()

        scrollbar = Scrollbar(self.frame)
        scrollbar.config(command=self.canvas.yview)
        self.canvas.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.pack(side=TOP, fill=Y,expand=True)

    def draw_lines(self):
        global last_line_y
        for i in range(3):
            left_x_point = left_margin + i*(rect_width+rect_space)
            right_x_point = left_margin+rect_width + i*(rect_width+rect_space)
            tmp = self.canvas.create_rectangle(left_x_point,25,right_x_point,75)
            line_x_point = (left_x_point + right_x_point) / 2
            self.canvas.create_line(line_x_point,75,line_x_point,1800)
            if i is 0:
                rect1_line_x = line_x_point
            elif i is 1:
                rect2_line_x = line_x_point
            elif i is 2:
                rect3_line_x = line_x_point

        for i in test_t:
            if i is 1:
                temp_y = last_line_y
                self.canvas.create_line(rect1_line_x,temp_y,rect1_line_x+line_space,temp_y,arrow="last")
                last_line_y = temp_y + 60
            elif i is 2:
                temp_y = last_line_y
                self.canvas.create_line(rect2_line_x,temp_y,rect2_line_x+line_space,temp_y,arrow="last")
                last_line_y = temp_y + 60
            elif i is 3:
                temp_y = last_line_y
                self.canvas.create_line(rect3_line_x,temp_y,rect3_line_x-line_space,temp_y,arrow="last")
                last_line_y = temp_y + 60
            elif i is 4:
                temp_y = last_line_y
                self.canvas.create_line(rect2_line_x,temp_y,rect2_line_x-line_space,temp_y,arrow="last")
                last_line_y = temp_y + 60


    def open_file(self):
        #global filename
        filename = tkFileDialog.askopenfilename(defaultextension=".txt",filetypes =[("All Files","*.*"),("Text Documents","*.txt")])
        if filename == "": # If no file chosen.
            filename = None # Absence of file.
        else:
            print "filename is",filename
            self.draw_lines()




if __name__ == "__main__":
    a = GuiApp()
    #a.draw_lines()
    mainloop()

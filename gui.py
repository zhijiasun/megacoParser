from Tkinter import *
import tkFileDialog
import os

rect_width = 100
rect_height = 50

rect_space = 200
top_margin = 25
left_margin = 50

rect1_line_x = 0
rect1_line_y = 0

rect2_line_x = 0
rect2_line_y = 0

rect3_line_x = 0
rect3_line_y = 0

d = [(0,'none'),(1,'first'),(2,'last'),(3,'both')]



class GuiApp():
    def __init__(self):
        self.master = Tk()
        self.frame = Frame(self.master)
        self.frame.pack()

        #s = Scrollbar(frame)
        self.canvas = Canvas(self.frame, width=800, height=600)
        self.canvas.pack()
        self.canvas.config(scrollregion=self.canvas.bbox(ALL))

        menubar = Menu(self.frame)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.open_file)
        menubar.add_cascade(label="File", menu=filemenu)
        self.master.config(menu=menubar)
        #self.master.mainloop()

    def draw_lines(self):
        for i in range(3):
            left_x_point = left_margin + i*(rect_width+rect_space)
            right_x_point = left_margin+rect_width + i*(rect_width+rect_space)
            tmp = self.canvas.create_rectangle(left_x_point,25,right_x_point,75)
            line_x_point = (left_x_point + right_x_point) / 2
            self.canvas.create_line(line_x_point,75,line_x_point,800)
            if i is 0:
                rect1_line_x = line_x_point
            elif i is 1:
                rect2_line_x = line_x_point
            elif i is 2:
                rect3_line_x = line_x_point

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

from tkinter import *
import tkinter as tk
from datetime import datetime
from PIL import ImageTk, Image
from tkinter import messagebox

from searching import Searching
WINDOWWIDTH = 900
WINDOWHEIGHT = 469
BGCOLOR="#D9D9D9"
CHOOSEDCOLOR="#fc6d6d"
SIZEENTRY= [5,6,7,8,9,10]
TESTENTRY= [1,2,3,4,5,6]
ALGORENTRY=["BFS","A*"]

class UI():
        
        def chooseButton(self, index, mode):
                if(mode=='size'):
                        self.sizeindex = index
                        for btn in self.sizebtn:
                                btn.config(bg=BGCOLOR)
                        self.sizebtn[index].config(bg=CHOOSEDCOLOR)
                elif(mode=='test'):
                        self.testindex = index
                        for btn in self.testbtn:
                                btn.config(bg=BGCOLOR)
                        self.testbtn[index].config(bg=CHOOSEDCOLOR)
                else:
                        self.algorindex = index
                        for btn in self.algorbtn:
                                btn.config(bg=BGCOLOR)
                        self.algorbtn[index].config(bg=CHOOSEDCOLOR)

        def validate(self,char):
                return char.isdigit()

        def generate(self):
                self.genbtn.config(bg=BGCOLOR)
                try:
                        size = 0
                        test = 0
                        if self.sizeindex == 6:
                                size = int(self.sizeEnt.get())
                        else:
                                size = self.sizeindex
                        if self.testindex == 6:
                                test = int(self.testEnt.get())
                        else:
                                test = self.testindex
                        # run
                        self.temp = Searching(SIZEENTRY[size] if size < 6 else size, TESTENTRY[test] if test < 6 else test)
                        if self.algorindex == 0:
                                self.temp.bfs()
                        elif self.algorindex == 1:
                                self.temp.Astar() 

                        self.page2_init()
                        
                        self.list_frame[0].pack_forget()
                        self.list_frame[1].tkraise()
                        self.list_frame[1].pack(fill=BOTH, expand=True)
                        

                except AttributeError:
                        self.genbtn.config(bg=CHOOSEDCOLOR)

        def turn_to_page1(self):
                self.list_frame[1].pack_forget()
                self.list_frame[0].tkraise()
                self.list_frame[0].pack(fill=BOTH, expand=True)

        def page1_init(self):
                self.list_frame.append(Frame(self.root,width= WINDOWWIDTH,height=WINDOWHEIGHT,bg=BGCOLOR,borderwidth=0))
                self.list_frame[0].pack(fill=BOTH,expand=True)
                # title
                titleFH = WINDOWHEIGHT*0.2
                self.heading = Label(self.list_frame[0],text="Hitori puzzle",font=('verdana',40,'bold'),bg=BGCOLOR)
                self.heading.place(relx=0.5, rely=0.15, anchor="center")

                # Label
                frame1width=WINDOWWIDTH
                frame1height=WINDOWHEIGHT-titleFH
                self.frame1 = LabelFrame(self.list_frame[0],width=frame1width,height=frame1height,font=('verdana',10,'normal'),bg=BGCOLOR,borderwidth=0)
                self.frame1.place(x=0,y=titleFH)


                open = Image.open("asset/s-open.png") 
                openresize = open.resize((58,23))
                middle = Image.open("asset/s-middle.png") 
                middleresize = middle.resize((58,23))
                close = Image.open("asset/s-close.png") 
                closeresize = close.resize((68,23))
                self.openphoto = ImageTk.PhotoImage(openresize) 
                self.middlephoto = ImageTk.PhotoImage(middleresize) 
                self.closephoto = ImageTk.PhotoImage(closeresize) 

                self.sizebtn=[]
                self.testbtn=[]
                self.algorbtn=[]
                #size
                sizeplacex=0.3*frame1width + 10
                sizeplacey=0.2*frame1height
                self.size = Label(self.frame1,text="Size:",font=('verdana',16),bg=BGCOLOR)
                self.size.place(relx=0.3, rely=0.2,anchor='e')
                for i in range(6):
                        if i == 0:
                                sbtn = Button(self.frame1,image = self.openphoto, width=58, height=23,bg=BGCOLOR, border=0,font=('verdana',16),text=str(i+5),compound=CENTER, command=lambda b=i:self.chooseButton(b,"size"))
                        else:
                                sbtn = Button(self.frame1,image = self.middlephoto, width=58, height=23,bg=BGCOLOR, border=0,font=('verdana',16),text=str(i+5),compound=CENTER, command=lambda b=i:self.chooseButton(b,"size"))
                        sbtn.place(x=sizeplacex+68*i,y=sizeplacey,anchor='w')
                        self.sizebtn.append(sbtn)

                entryBg = Label(self.frame1,image=self.closephoto,bg=BGCOLOR)
                entryBg.place(x=sizeplacex+68*6,y=sizeplacey,anchor='w')
                self.sizebtn.append(entryBg)

                self.sizeEnt=Entry(self.frame1,width=8,font=('verdana',16), border=0, justify="center",validate='key', validatecommand=(self.list_frame[0].register(self.validate), "%P"))
                self.sizeEnt.bind("<KeyRelease>",lambda event:self.chooseButton(6,"size"))
                self.sizeEnt.place(x=sizeplacex+68*6+10,y=sizeplacey,anchor='w',width=58, height=23)
                # testcase
                testplacex=0.3*frame1width + 10
                testplacey=0.4*frame1height
                self.testcase = Label(self.frame1,text="Default testcase:",font=('verdana',16),bg=BGCOLOR)
                self.testcase.place(relx=0.3, rely=0.4,anchor='e')

                for i in range(6):
                        if i == 0:
                                tbtn = Button(self.frame1,image = self.openphoto, width=58, height=23,bg=BGCOLOR, border=0,font=('verdana',16),text=str(i+1),compound=CENTER, command=lambda b=i:self.chooseButton(b,"test"))
                        else:
                                tbtn = Button(self.frame1,image = self.middlephoto, width=58, height=23,bg=BGCOLOR, border=0,font=('verdana',16),text=str(i+1),compound=CENTER, command=lambda b=i:self.chooseButton(b,"test"))
                        tbtn.place(x=testplacex+68*i,y=testplacey,anchor='w')
                        self.testbtn.append(tbtn)

                testentryBg = Label(self.frame1,image=self.closephoto,bg=BGCOLOR)
                testentryBg.place(x=testplacex+68*6,y=testplacey,anchor='w')
                self.testbtn.append(testentryBg)

                self.testEnt=Entry(self.frame1,width=8,font=('verdana',16), border=0, justify="center",validate='key', validatecommand=(self.list_frame[0].register(self.validate), "%P"))
                self.testEnt.bind("<KeyRelease>",lambda event:self.chooseButton(6,"test"))
                self.testEnt.place(x=testplacex+68*6+10,y=testplacey,anchor='w',width=58, height=23)

                # Algorithm
                algoropen = Image.open("asset/b-open.png") 
                algoropenresize = algoropen.resize((238,23))
                self.alopenphoto = ImageTk.PhotoImage(algoropenresize)
                algorclose = Image.open("asset/b-close.png") 
                algorcloseresize = algorclose.resize((238,23))
                self.alclosephoto = ImageTk.PhotoImage(algorcloseresize)
                algorplacex=0.3*frame1width + 10
                algorplacey=0.6*frame1height
                self.algor = Label(self.frame1,text="Algorithm:",font=('verdana',16),bg=BGCOLOR)
                self.algor.place(relx=0.3, rely=0.6,anchor='e')

                for i in range(2):
                        if i == 0:
                                abtn = Button(self.frame1,image = self.alopenphoto, width=238, height=23,bg=BGCOLOR, border=0,font=('verdana',16),text="BFS",compound=CENTER, command=lambda b=i:self.chooseButton(b,"algor"))
                        else:
                                abtn = Button(self.frame1,image = self.alclosephoto, width=238, height=23,bg=BGCOLOR, border=0,font=('verdana',16),text="A*",compound=CENTER, command=lambda b=i:self.chooseButton(b,"algor"))
                        abtn.place(x=algorplacex+238*i,y=algorplacey,anchor='w')
                        self.algorbtn.append(abtn)

                gen = Image.open("asset/gen.png") 
                genresize = gen.resize((238,23))
                self.genphoto = ImageTk.PhotoImage(genresize)

                self.genbtn = Button(self.list_frame[0], width=238, height=23,bg=BGCOLOR,image=self.genphoto, border=0,font=('verdana',16),text="GENERATE",compound=CENTER,command=lambda : self.generate())
                self.genbtn.place(relx=0.5,rely=0.8,anchor='center')

        def page2_init(self):
                self.list_frame[1]= Frame(self.root,width= WINDOWWIDTH,height=WINDOWHEIGHT,bg=BGCOLOR,borderwidth=0)
                self.list_frame[1].pack(fill=BOTH,expand=True)
                
                Label(self.list_frame[1],text="Time executed:",font=('verdana',16),bg=BGCOLOR).place(relx=0.25, rely=0.2,anchor='e')
                Label(self.list_frame[1],text="Number of node\ngenerated:",font=('verdana',16),bg=BGCOLOR).place(relx=0.25, rely=0.4,anchor='e')
                Label(self.list_frame[1],text=str(round(self.temp.time,3))+' s',font=('verdana',16),bg=BGCOLOR).place(relx=0.3, rely=0.2,anchor='w')
                Label(self.list_frame[1],text=str(self.temp.numberNode)+' nodes',font=('verdana',16),bg=BGCOLOR).place(relx=0.3, rely=0.4,anchor='w')

                arr = Image.open("asset/arrow.png")
                arrresize = arr.resize((70,70))
                self.arrPhoto = ImageTk.PhotoImage(arrresize)
                Button(self.list_frame[1], width=70, height=70,bg=BGCOLOR,image=self.arrPhoto, border=0,font=('verdana',16),command=lambda :self.turn_to_page1(),activebackground=BGCOLOR).place(relx=0.1,rely=0.9,anchor="sw")

                matrixSize = 360
                self.matrixFrame = Frame(self.list_frame[1],width=matrixSize,height=matrixSize,bg=BGCOLOR,highlightthickness=3,highlightbackground='black')
                self.matrixFrame.place(relx=0.65,rely=0.5,anchor='center')

                size = 5

                self.canvas = Canvas(self.matrixFrame,width=matrixSize,height=matrixSize,bg=BGCOLOR,highlightthickness=0)
                
                cellsize = int(matrixSize/size)
                for i in range(size):
                        self.canvas.create_line((cellsize)*(i+1),0,(cellsize)*(i+1),matrixSize)
                        self.canvas.create_line(0,(cellsize)*(i+1),matrixSize,(cellsize)*(i+1))
                for y in range(size):
                        for x in range(size):
                                Label(self.matrixFrame,text=str(self.temp.result.matrix[y][x]),font=('verdana',18),bg=BGCOLOR).place(x = int(cellsize/2 + cellsize*x), y = int(cellsize/2 + cellsize*y),anchor='center')      
                                
                self.canvas.pack(fill = BOTH, expand = True)

        def __init__(self):
                self.root = tk.Tk()
                self.root.config(width = WINDOWWIDTH, height = WINDOWHEIGHT)
                self.root.title("Hitori")
                self.root.maxsize(WINDOWWIDTH,WINDOWHEIGHT)
                self.root.minsize(WINDOWWIDTH,WINDOWHEIGHT)
                self.root['bg'] = BGCOLOR

                self.list_frame = []
                self.page1_init()
                self.list_frame.append(Frame(self.root))
                self.list_frame[1].forget()
                

                self.root.mainloop()


if __name__ == '__main__':
        UI()
    


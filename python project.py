from tkinter import*
import time
import tkinter.messagebox
r=Tk()
r.geometry("1320x700")
r.title("CGPA Calculator")
text_input=StringVar()
text_input1=StringVar()
cgpa_input=StringVar()
#=======================Remarks===============================
lr=Label(r,font=('ariel',18,'bold'),text="Remarks",width=8,fg="Blue",bd=10,anchor='w')
lr.place(x=955,y=120)
Er=Entry(r,font=('arial',20,'bold'),insertwidth=2,width=15,bg='powder blue',justify='center')
Er.place(x=1075,y=120)
def calcgpa():
    cgpa1=eval(text_input.get())
    cgpa2=eval(text_input1.get())
    finalcgpa=(cgpa1+cgpa2)/2
    cgpa_input.set(round(finalcgpa,2))
    if(finalcgpa>=8 and finalcgpa<9):
        a="Very Good"
        Er.insert(0,a)

    if(finalcgpa>=7 and finalcgpa<8):
        b="Average"
        Er.insert(0,b)

    if(finalcgpa>4 and finalcgpa<7):
        c="Work hard"
        Er.insert(0,c)

    if(finalcgpa>9):
        d="Excellent"
        Er.insert(0,d)
#Frames
Tops=Frame(r,width=100,height=10,relief=SUNKEN)
Tops.pack(side=TOP)
Bottom=Frame(r,width=100,height=10,relief=SUNKEN)
Bottom.pack(side=BOTTOM)
Left=Frame(r,width=500,height=10,relief=SUNKEN)
Left.pack(side=LEFT)
#TIME
loctime=time.asctime(time.localtime(time.time()))
#SYSTEM INFO
l1info=Label(Tops,font=('ariel',50,'bold'),text="CGPA Calculator",fg="seagreen",bd=10,anchor='w')
l1info.grid(row=0,column=0)
l1infot=Label(Tops,font=('ariel',20,'bold'),text=loctime,fg="Blue",bd=10,anchor='w')
l1infot.grid(row=1,column=0)
#SEM 1
ls=Label(Left,font=('ariel',15,'bold'),text="SEM 1",fg="Green",bd=10,anchor='w')
ls.grid(row=0,column=0)
#Grade and Credit
lg=Label(Left,font=('ariel',10,'bold'),text="Grade",fg="red",bd=10,anchor='w')
lg.grid(row=3,column=3)
lc=Label(Left,font=('ariel',10,'bold'),text="Credit",fg="red",bd=10,anchor='w')
lc.grid(row=3,column=4)
#Subjects
ls1=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 1",fg="brown",bd=10,anchor='w')
ls1.grid(row=4,column=0)
ls2=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 2",fg="brown",bd=10,anchor='w')
ls2.grid(row=5,column=0)
ls3=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 3",fg="brown",bd=10,anchor='w')
ls3.grid(row=6,column=0)
ls4=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 4",fg="brown",bd=10,anchor='w')
ls4.grid(row=7,column=0)
ls5=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 5",fg="brown",bd=10,anchor='w')
ls5.grid(row=8,column=0)
ls6=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 6",fg="brown",bd=10,anchor='w')
ls6.grid(row=9,column=0)
ls7=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 7",fg="brown",bd=10,anchor='w')
ls7.grid(row=10,column=0)
#Grade Entry BOX
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
s6=StringVar()
s7=StringVar()
sc1=StringVar()
sc2=StringVar()
sc3=StringVar()
sc4=StringVar()
sc5=StringVar()
sc6=StringVar()
sc7=StringVar()
text_input=StringVar()
def cal():
    sc=0
    sg=0
    tgpa=0
    fg1=0
    fg2=0
    fg3=0
    fg4=0
    fg5=0
    fg6=0
    fg7=0
    g1=s1.get()
    g2=s2.get()
    g3=s3.get()
    g4=s4.get()
    g5=s5.get()
    g6=s6.get()
    g7=s7.get()
    c1=int(sc1.get())
    c2=int(sc2.get())
    c3=int(sc3.get())
    c4=int(sc4.get())
    c5=int(sc5.get())
    c6=int(sc6.get())
    c7=int(sc7.get())
    if (g1=='O' or g1=='A+' or g1=='A' or g1=='B+' or g1=='B' or g1=='C' or g1=='D' or g1=='E' ):
        if(g1=='O'):
            fg1=10
        elif(g1=='A+'):
            fg1=9
        elif(g1=='A'):
            fg1=8
        elif(g1=='B+'):
            fg1=7
        elif(g1=='B'):
            fg1=6
        elif(g1=='C'):
            fg1=5
        elif(g1=='D'):
            fg1=4
        else:
            fg1=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 1 ")
    if (g2=='O' or g2=='A+' or g2=='A' or g2=='B+' or g2=='B' or g2=='C' or g2=='D' or g2=='E' ):
        if(g2=='O'):
            fg2=10
        elif(g2=='A+'):
            fg2=9
        elif(g2=='A'):
            fg2=8
        elif(g2=='B+'):
            fg2=7
        elif(g2=='B'):
            fg2=6
        elif(g2=='C'):
            fg2=5
        elif(g2=='D'):
            fg2=4
        else:
            fg2=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 2 ")
        if (g3=='O' or g3=='A+' or g3=='A' or g3=='B+' or g3=='B' or g3=='C' or g3=='D' or g3=='E' ):
            if(g3=='O'):
                fg3=10
            elif(g3=='A+'):
                fg3=9
            elif(g3=='A'):
                fg3=8
            elif(g3=='B+'):
                fg3=7
            elif(g3=='B'):
                fg3=6
            elif(g3=='C'):
                fg3=5
            elif(g3=='D'):
                fg3=4
            else:
                fg3=0
        else:
            tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 3 ")
    if (g4=='O' or g4=='A+' or g4=='A' or g4=='B+' or g4=='B' or g4=='C' or g4=='D' or g4=='E' ):
        if(g4=='O'):
            fg4=10
        elif(g4=='A+'):
            fg4=9
        elif(g4=='A'):
            fg4=8
        elif(g4=='B+'):
            fg4=7
        elif(g4=='B'):
            fg4=6
        elif(g4=='C'):
            fg4=5
        elif(g4=='D'):
            fg4=4
        else:
            fg4=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 4 ")
    if (g5=='O' or g5=='A+' or g5=='A' or g5=='B+' or g5=='B' or g5=='C' or g5=='D' or g5=='E' ):
        if(g5=='O'):
            fg5=10
        elif(g5=='A+'):
            fg5=9
        elif(g5=='A'):
            fg5=8
        elif(g5=='B+'):
            fg5=7
        elif(g5=='B'):
            fg5=6
        elif(g5=='C'):
            fg5=5
        elif(g5=='D'):
            fg5=4
        else:
            fg5=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 5 ")
    if (g6=='O' or g6=='A+' or g6=='A' or g6=='B+' or g6=='B' or g6=='C' or g6=='D' or g6=='E' ):
        if(g6=='O'):
            fg6=10
        elif(g6=='A+'):
            fg6=9
        elif(g6=='A'):
            fg6=8
        elif(g6=='B+'):
            fg6=7
        elif(g6=='B'):
            fg6=6
        elif(g6=='C'):
            fg6=5
        elif(g6=='D'):
            fg6=4
        else:
            fg6=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 6 ")
    if (g7=='O' or g7=='A+' or g7=='A' or g7=='B+' or g7=='B' or g7=='C' or g7=='D' or g7=='E' ):
        if(g7=='O'):
            fg7=10
        elif(g7=='A+'):
            fg7=9
        elif(g7=='A'):
            fg7=8
        elif(g7=='B+'):
            fg7=7
        elif(g7=='B'):
            fg7=6
        elif(g7=='C'):
            fg7=5
        elif(g7=='D'):
            fg7=4
        else:
            fg7=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 7 ")
    sg=(fg1*c1)+(fg2*c2)+(fg3*c3)+(fg4*c4)+(fg5*c5)+(fg6*c6)+(fg7*c7)
    sc=c1+c2+c3+c4+c5+c6+c7
    tgpa=sg/sc
    text_input.set(round(tgpa,2))
def caps(event):
    s1.set(s1.get().upper())
    s2.set(s2.get().upper())
    s3.set(s3.get().upper())
    s4.set(s4.get().upper())
    s5.set(s5.get().upper())
    s6.set(s6.get().upper())
    s7.set(s7.get().upper())
    s11.set(s11.get().upper())
    s12.set(s12.get().upper())
    s13.set(s13.get().upper())
    s14.set(s14.get().upper())
    s15.set(s15.get().upper())
    s16.set(s16.get().upper())
    s17.set(s17.get().upper())
GE1=Entry(Left,font=('arial',10,'bold'),textvariable=s1,insertwidth=2,bg='White',justify='center')
GE1.grid(row=4,column=3)
GE1.bind("<KeyRelease>", caps)
GE2=Entry(Left,font=('arial',10,'bold'),textvariable=s2,insertwidth=2,bg='White',justify='center')
GE2.grid(row=5,column=3)
GE2.bind("<KeyRelease>", caps)
GE3=Entry(Left,font=('arial',10,'bold'),textvariable=s3,insertwidth=2,bg='White',justify='center')
GE3.grid(row=6,column=3)
GE3.bind("<KeyRelease>", caps)
GE4=Entry(Left,font=('arial',10,'bold'),textvariable=s4,insertwidth=2,bg='White',justify='center')
GE4.grid(row=7,column=3)
GE4.bind("<KeyRelease>", caps)
GE5=Entry(Left,font=('arial',10,'bold'),textvariable=s5,insertwidth=2,bg='White',justify='center')
GE5.grid(row=8,column=3)
GE5.bind("<KeyRelease>", caps)
GE6=Entry(Left,font=('arial',10,'bold'),textvariable=s6,insertwidth=2,bg='White',justify='center')
GE6.grid(row=9,column=3)
GE6.bind("<KeyRelease>", caps)
GE7=Entry(Left,font=('arial',10,'bold'),textvariable=s7,insertwidth=2,bg='White',justify='center')
GE7.grid(row=10,column=3)
GE7.bind("<KeyRelease>", caps)
#============Credit Entry Box===================
CE1=Entry(Left,font=('arial',10,'bold'),textvariable=sc1,insertwidth=2,bg='White',justify='center')
CE1.grid(row=4,column=4)
CE2=Entry(Left,font=('arial',10,'bold'),textvariable=sc2,insertwidth=2,bg='White',justify='center')
CE2.grid(row=5,column=4)
CE3=Entry(Left,font=('arial',10,'bold'),textvariable=sc3,insertwidth=2,bg='White',justify='center')
CE3.grid(row=6,column=4)
CE4=Entry(Left,font=('arial',10,'bold'),textvariable=sc4,insertwidth=2,bg='White',justify='center')
CE4.grid(row=7,column=4)
CE5=Entry(Left,font=('arial',10,'bold'),textvariable=sc5,insertwidth=2,bg='White',justify='center')
CE5.grid(row=8,column=4)
CE6=Entry(Left,font=('arial',10,'bold'),textvariable=sc6,insertwidth=2,bg='White',justify='center')
CE6.grid(row=9,column=4)
CE7=Entry(Left,font=('arial',10,'bold'),textvariable=sc7,insertwidth=2,bg='White',justify='center')
CE7.grid(row=10,column=4)
#==============SEM 1 TGPA======================================
def keybind(event):
    tkinter.messagebox.showinfo("Warning","You are not able to Enter TGPA directly")
LT=Label(Left,font=('ariel',15,'bold'),text="TGPA",fg="Red",bd=10,anchor='w')
LT.grid(row=6,column=10)
TE=Entry(Left,font=('arial',15,'bold'),textvariable=text_input,insertwidth=2,bg='Yellow',justify='center')
TE.grid(row=6,column=11)
TE.bind('<KeyPress>',keybind)
#==============Submit Button=================================
subbut=Button(Left,padx=16,pady=8,bd=8,fg="black",font=('arial',15,'bold'),text="Submit",
bg='powder blue',command=cal).grid(row=12,column=3,columnspan=2)
#=======================================================================
#=============================SEM 2=====================================
#=======================================================================
#================SEM 2============================
ls=Label(Left,font=('ariel',15,'bold'),text="SEM 2",fg="Green",bd=10,anchor='w')
ls.grid(row=0,column=15)
#===============Grade and Credit==================
lg1=Label(Left,font=('ariel',10,'bold'),text="Grade",fg="red",bd=10,anchor='w')
lg1.grid(row=3,column=16)
lc1=Label(Left,font=('ariel',10,'bold'),text="Credit",fg="red",bd=10,anchor='w')
lc1.grid(row=3,column=17)
#===============Subjects==========================
ls11=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 1",fg="brown",bd=10,anchor='w')
ls11.grid(row=4,column=15)
ls12=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 2",fg="brown",bd=10,anchor='w')
ls12.grid(row=5,column=15)
ls13=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 3",fg="brown",bd=10,anchor='w')
ls13.grid(row=6,column=15)
ls14=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 4",fg="brown",bd=10,anchor='w')
ls14.grid(row=7,column=15)
ls15=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 5",fg="brown",bd=10,anchor='w')
ls15.grid(row=8,column=15)
ls16=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 6",fg="brown",bd=10,anchor='w')
ls16.grid(row=9,column=15)
ls17=lg=Label(Left,font=('ariel',10,'bold'),text="Subject 7",fg="brown",bd=10,anchor='w')
ls17.grid(row=10,column=15)
#============Credit Entry Box===================
s11=StringVar()
s12=StringVar()
s13=StringVar()
s14=StringVar()
s15=StringVar()
s16=StringVar()
s17=StringVar()
sc11=StringVar()
sc12=StringVar()
sc13=StringVar()
sc14=StringVar()
sc15=StringVar()
sc16=StringVar()
sc17=StringVar()
def cal1():
    sc1=0
    sg1=0
    tgpa1=0
    fg11=0
    fg12=0
    fg13=0
    fg14=0
    fg15=0
    fg16=0
    fg17=0
    #---------------
    g11=s11.get()
    g12=s12.get()
    g13=s13.get()
    g14=s14.get()
    g15=s15.get()
    g16=s16.get()
    g17=s17.get()
    #----------------
    c11=int(sc11.get())
    c12=int(sc12.get())
    c13=int(sc13.get())
    c14=int(sc14.get())
    c15=int(sc15.get())
    c16=int(sc16.get())
    c17=int(sc17.get())
    #--------------
    if (g11=='O' or g11=='A+' or g11=='A' or g11=='B+' or g11=='B' or g11=='C' or g11=='D' or g11=='E' ):
        if(g11=='O'):
            fg11=10
        elif(g11=='A+'):
            fg11=9
        elif(g11=='A'):
            fg11=8
        elif(g11=='B+'):
            fg11=7
        elif(g11=='B'):
            fg11=6
        elif(g11=='C'):
            fg11=5
        elif(g11=='D'):
            fg11=4
        else:
            fg11=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 1 ")
    if (g12=='O' or g12=='A+' or g12=='A' or g12=='B+' or g12=='B' or g12=='C' or g12=='D' or g12=='E' ):
        if(g12=='O'):
            fg12=10
        elif(g12=='A+'):
            fg12=9
        elif(g12=='A'):
            fg12=8
        elif(g12=='B+'):
            fg12=7
        elif(g12=='B'):
            fg12=6
        elif(g12=='C'):
            fg12=5
        elif(g12=='D'):
            fg12=4
        else:
            fg12=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 2 ")
    if (g13=='O' or g13=='A+' or g13=='A' or g13=='B+' or g13=='B' or g13=='C' or g13=='D' or g13=='E' ):
        if(g13=='O'):
            fg13=10
        elif(g13=='A+'):
            fg13=9
        elif(g13=='A'):
            fg13=8
        elif(g13=='B+'):
            fg13=7
        elif(g13=='B'):
            fg13=6
        elif(g13=='C'):
            fg13=5
        elif(g13=='D'):
            fg13=4
        else:
            fg13=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 3 ")
    if (g14=='O' or g14=='A+' or g14=='A' or g14=='B+' or g14=='B' or g14=='C' or g14=='D' or g14=='E' ):
        if(g14=='O'):
            fg14=10
        elif(g14=='A+'):
            fg14=9
        elif(g14=='A'):
            fg14=8
        elif(g14=='B+'):
            fg14=7
        elif(g14=='B'):
            fg14=6
        elif(g14=='C'):
            fg14=5
        elif(g14=='D'):
            fg14=4
        else:
            fg14=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 4 ")
    if (g15=='O' or g15=='A+' or g15=='A' or g15=='B+' or g15=='B' or g15=='C' or g15=='D' or g15=='E' ):
        if(g15=='O'):
            fg15=10
        elif(g15=='A+'):
            fg15=9
        elif(g15=='A'):
            fg15=8
        elif(g15=='B+'):
            fg15=7
        elif(g15=='B'):
            fg15=6
        elif(g15=='C'):
            fg15=5
        elif(g15=='D'):
            fg15=4
        else:
            fg15=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 5 ")
    if (g16=='O' or g16=='A+' or g16=='A' or g16=='B+' or g16=='B' or g16=='C' or g16=='D' or g16=='E' ):
        if(g16=='O'):
            fg16=10
        elif(g16=='A+'):
            fg16=9
        elif(g16=='A'):
            fg16=8
        elif(g16=='B+'):
            fg16=7
        elif(g16=='B'):
            fg16=6
        elif(g16=='C'):
            fg16=5
        elif(g16=='D'):
            fg16=4
        else:
            fg16=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 6 ")
    if (g17=='O' or g17=='A+' or g17=='A' or g17=='B+' or g17=='B' or g17=='C' or g17=='D' or g17=='E' ):
        if(g17=='O'):
            fg17=10
        elif(g17=='A+'):
            fg17=9
        elif(g17=='A'):
            fg17=8
        elif(g17=='B+'):
            fg17=7
        elif(g17=='B'):
            fg17=6
        elif(g17=='C'):
            fg17=5
        elif(g17=='D'):
            fg17=4
        else:
            fg17=0
    else:
        tkinter.messagebox.showinfo("Warning","Please Enter appropriate grade in Subject 7 ")
    sg1=(fg11*c11)+(fg12*c12)+(fg13*c13)+(fg14*c14)+(fg15*c15)+(fg16*c16)+(fg17*c17)
    sc1=c11+c12+c13+c14+c15+c16+c17
    tgpa1=sg1/sc1
    text_input1.set(round(tgpa1,2))
GE11=Entry(Left,font=('arial',10,'bold'),textvariable=s11,insertwidth=2,bg='White',justify='center')
GE11.grid(row=4,column=16)
GE11.bind("<KeyRelease>", caps)
GE12=Entry(Left,font=('arial',10,'bold'),textvariable=s12,insertwidth=2,bg='White',justify='center')
GE12.grid(row=5,column=16)
GE12.bind("<KeyRelease>", caps)
GE13=Entry(Left,font=('arial',10,'bold'),textvariable=s13,insertwidth=2,bg='White',justify='center')
GE13.grid(row=6,column=16)
GE13.bind("<KeyRelease>", caps)
GE14=Entry(Left,font=('arial',10,'bold'),textvariable=s14,insertwidth=2,bg='White',justify='center')
GE14.grid(row=7,column=16)
GE14.bind("<KeyRelease>", caps)
GE15=Entry(Left,font=('arial',10,'bold'),textvariable=s15,insertwidth=2,bg='White',justify='center')
GE15.grid(row=8,column=16)
GE15.bind("<KeyRelease>", caps)
GE16=Entry(Left,font=('arial',10,'bold'),textvariable=s16,insertwidth=2,bg='White',justify='center')
GE16.grid(row=9,column=16)
GE16.bind("<KeyRelease>", caps)
GE17=Entry(Left,font=('arial',10,'bold'),textvariable=s17,insertwidth=2,bg='White',justify='center')
GE17.grid(row=10,column=16)
GE17.bind("<KeyRelease>", caps)
#============Credit Entry Box===================
CE11=Entry(Left,font=('arial',10,'bold'),textvariable=sc11,insertwidth=2,bg='White',justify='center')
CE11.grid(row=4,column=17)
CE12=Entry(Left,font=('arial',10,'bold'),textvariable=sc12,insertwidth=2,bg='White',justify='center')
CE12.grid(row=5,column=17)
CE13=Entry(Left,font=('arial',10,'bold'),textvariable=sc13,insertwidth=2,bg='White',justify='center')
CE13.grid(row=6,column=17)
CE14=Entry(Left,font=('arial',10,'bold'),textvariable=sc14,insertwidth=2,bg='White',justify='center')
CE14.grid(row=7,column=17)
CE15=Entry(Left,font=('arial',10,'bold'),textvariable=sc15,insertwidth=2,bg='White',justify='center')
CE15.grid(row=8,column=17)
CE16=Entry(Left,font=('arial',10,'bold'),textvariable=sc16,insertwidth=2,bg='White',justify='center')
CE16.grid(row=9,column=17)
CE17=Entry(Left,font=('arial',10,'bold'),textvariable=sc17,insertwidth=2,bg='White',justify='center')
CE17.grid(row=10,column=17)
#SEM 2 TGPA
def keybind1(event):
    tkinter.messagebox.showinfo("Warning","You are not able to Enter TGPA directly")
LT1=Label(Left,font=('ariel',15,'bold'),text="TGPA",fg="Red",bd=10,anchor='w')
LT1.grid(row=6,column=18)
TE1=Entry(Left,font=('arial',15,'bold'),textvariable=text_input1,insertwidth=2,bg='Yellow',justify='center')
TE1.grid(row=6,column=19)
TE1.bind('<KeyPress>',keybind)
#Submit Button
subbut2=Button(Left,padx=16,pady=8,bd=8,fg="black",font=('arial',15,'bold'),text="Submit",
bg='powder blue',command=cal1).grid(row=12,column=16,columnspan=2)
#CGPA
def keybind1(event):
    tkinter.messagebox.showinfo("Warning","You are not able to Enter CGPA directly")
lc=Label(Bottom,font=('ariel',20,'bold'),text="CGPA",fg="Blue",bd=10,anchor='w')
lc.grid(row=11,column=0)
EC=Entry(Bottom,font=('arial',20,'bold'),textvariable=cgpa_input,insertwidth=2,bg='powder blue',justify='center')
EC.grid(row=11,column=1)
EC.bind('<KeyPress>',keybind1)
#Button
Cgpabut=Button(Left,padx=16,pady=8,bd=8,fg="black",font=('arial',15,'bold'),text="CGPA",
bg='green',command=calcgpa).grid(row=12,column=19)
r.mainloop()

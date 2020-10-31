#Inteliigent traffic system
from tkinter import *
from PIL import Image, ImageTk
from tkinter import font
import sys
import tkinter
root = tkinter.Tk()

root.title("Intelligent Traffic Control System")
 # gui making

HEIGHT = 1080
WIDTH =1920

#think of the canvas as a fitter that widen the window, thats it, HOWEVER all frams still stick on root, even bg image
canvas = Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

image = Image.open('hell.jpg')

background_image = ImageTk.PhotoImage(image)
background_label = Label(root,image=background_image)
background_label.place(relheight=1,relwidth=1)



def showMsg( answer):
    # tkWindow = Tk()
    # tkWindow.geometry('1010x420')
    # tkWindow.title('PythonExamples.org - Tkinter Example')


    import sys
    stdoutOrigin=sys.stdout
    sys.stdout = open("log.txt", "w")
    frame_3 = Frame(root,bg='#66B2FF')
    frame_3.place(relx=0.35,rely=0.15,relwidth=0.655,relheight=0.55,anchor='n')
    f=open("log.txt",'r')
    if answer<20:
        data= "The current traffic level is Very Low " +str(answer)+' %'
    elif answer>=20 and answer<40:
        data= "The current traffic level is  Low " +str(answer)+' %'
    if answer>=40 and answer<60:
        data= "The current traffic level is Medium " +str(answer)+' %'
    if answer>=60 and answer<90:
        data= "The current traffic level is High " +str(answer)+' %'
    if answer>=90 and answer<101:
        data= "The current traffic level is Very High " +str(answer)+' %'

    f.close()
    Results = Label(frame_3, text = data,background = "#66B2FF" ,relief=RAISED,font=("Helvetica", 15),anchor=CENTER,foreground="black",padx = 10 , pady = 10)
    Results.grid(row = 1, column = 1)


def fuzz():
    cw = int(v1.get())
    ci = int(v2.get())
    # a=eval(input("Enter the number of cars waiting :"))
    a = cw
    b = ci

    rule_simulation.input['carsWaiting']=a
    # b=eval(input("Enter the number of incoming cars :"))
    rule_simulation.input['carsIncoming']=b

    rule_simulation.compute()
    # print("Traffic  %f "%rule_simulation.output['Traffic'],"%")
    answer = rule_simulation.output['Traffic']
    Traffic.view(sim=rule_simulation)
    showMsg(answer)




frame_1 = Frame(root,bg='#B8204E',bd=5)
frame_1.place(relx=0.5,rely=0.0,relwidth=0.6,relheight=0.1,anchor='n')


frame_4 = Frame(root,bg='#B8204E')
frame_4.place(relx=0.8,rely=0.15,relwidth=0.23,relheight=0.10,anchor='n')
name_label1=Label(frame_4,text="Cars Incoming  ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',15))
name_label1.place(relx =0,relwidth=0.7,relheight=1)
v1 = StringVar()
e = Entry(frame_4, textvariable=v1,bg='#B8204E',fg='#0D0D11',font=('Footlight MT Light',25),justify=CENTER)
e.place(relx=0.85,rely=0,relwidth=.3,relheight=1,anchor='n')


frame_5 = Frame(root,bg='#B8204E')
frame_5.place(relx=0.8,rely=0.40,relwidth=0.23,relheight=0.10,anchor='n')
name_label2=Label(frame_5,text="Cars Waiting   ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',15))
name_label2.place(relx =0,relwidth=0.7,relheight=1)
v2 = StringVar()
e = Entry(frame_5, textvariable=v2,bg='#B8204E',fg='#0D0D11',font=('Footlight MT Light',25),justify=CENTER)
e.place(relx=0.85,rely=0,relwidth=.3,relheight=1,anchor='n')


name_label=Label(frame_1,text="Intelligent Traffic Control System   ",bg='#FB2865',fg='#0D0D11',font=('Footlight MT Light',25))
name_label.place(relx =.15,relwidth=0.7,relheight=1)



default = Button(root,text="Submit",command=lambda:[fuzz()],font=('Footlight MT Light',25),bg='#15C51F',fg='black')
default.place(relwidth=.2,relx=.7,rely=.30,relheight=0.05)


import numpy as np;
import skfuzzy as sk;
from skfuzzy import control as ctrl;
carsWaiting=ctrl.Antecedent(np.arange(1,200,1),'carsWaiting')
carsIncoming =ctrl.Antecedent(np.arange(1,200,1),'carsIncoming')
Traffic=ctrl.Consequent(np.arange(1,101,1),'Traffic')

carsWaiting['Very low']=sk.trimf(carsWaiting.universe,[0,5,10])
carsWaiting['low']=sk.trimf(carsWaiting.universe,[8,13,15])

carsWaiting['medium']=sk.trimf(carsWaiting.universe,[13,18,20])


carsWaiting['high']=sk.trimf(carsWaiting.universe,[40,50,60])
carsWaiting['Very high']=sk.trimf(carsWaiting.universe,[60,70,101])
carsWaiting['high']=sk.trimf(carsWaiting.universe,[18,25,30])
carsWaiting['Very high']=sk.trimf(carsWaiting.universe,[30,70,100])



carsIncoming['Very low']=sk.trimf(carsIncoming.universe,[1,10,20])
carsIncoming['low']=sk.trimf(carsIncoming.universe,[20,30,40])

carsIncoming['medium']=sk.trimf(carsIncoming.universe,[39,50,80])

carsIncoming['high']=sk.trimf(carsIncoming.universe,[79,100,130])
carsIncoming['Very high']=sk.trimf(carsIncoming.universe,[129,155,191])


Traffic['Very low']=sk.trimf(Traffic.universe,[1,5,20])
Traffic['low']=sk.trimf(Traffic.universe,[20,30,40])

Traffic['medium']=sk.trimf(Traffic.universe,[40,50,60])

Traffic['high']=sk.trimf(Traffic.universe,[60,80,90])
Traffic['Very high']=sk.trimf(Traffic.universe,[89,95,101])

carsWaiting.view()
carsIncoming.view()
Traffic.view()

Rule1=ctrl.Rule(carsWaiting['Very low']|carsIncoming['Very low'],Traffic['Very low'])
Rule2=ctrl.Rule(carsWaiting['Very low']|carsIncoming['low'],Traffic['low'])
Rule3=ctrl.Rule(carsWaiting['Very low']|carsIncoming['medium'],Traffic['medium'])
Rule4=ctrl.Rule(carsWaiting['Very low']|carsIncoming['high'],Traffic['medium'])
Rule5=ctrl.Rule(carsWaiting['Very low']|carsIncoming['Very high'],Traffic['Very high'])


Rule6=ctrl.Rule(carsWaiting['low']|carsIncoming['Very low'],Traffic['Very low'])
Rule7=ctrl.Rule(carsWaiting['low']|carsIncoming['low'],Traffic['low'])
Rule8=ctrl.Rule(carsWaiting['low']|carsIncoming['medium'],Traffic['medium'])
Rule9=ctrl.Rule(carsWaiting['low']|carsIncoming['high'],Traffic['medium'])
Rule10=ctrl.Rule(carsWaiting['low']|carsIncoming['Very high'],Traffic['Very high'])

Rule11=ctrl.Rule(carsWaiting['medium']|carsIncoming['Very low'],Traffic['low'])
Rule12=ctrl.Rule(carsWaiting['medium']|carsIncoming['low'],Traffic['low'])
Rule13=ctrl.Rule(carsWaiting['medium']|carsIncoming['medium'],Traffic['high'])
Rule14=ctrl.Rule(carsWaiting['medium']|carsIncoming['high'],Traffic['high'])
Rule15=ctrl.Rule(carsWaiting['medium']|carsIncoming['Very high'],Traffic['Very high'])

Rule16=ctrl.Rule(carsWaiting['high']|carsIncoming['Very low'],Traffic['low'])
Rule17=ctrl.Rule(carsWaiting['high']|carsIncoming['low'],Traffic['low'])
Rule18=ctrl.Rule(carsWaiting['high']|carsIncoming['medium'],Traffic['high'])
Rule19=ctrl.Rule(carsWaiting['high']|carsIncoming['high'],Traffic['high'])
Rule20=ctrl.Rule(carsWaiting['high']|carsIncoming['Very high'],Traffic['Very high'])


Rule21=ctrl.Rule(carsWaiting['Very high']|carsIncoming['Very low'],Traffic['medium'])
Rule22=ctrl.Rule(carsWaiting['Very high']|carsIncoming['low'],Traffic['medium'])
Rule23=ctrl.Rule(carsWaiting['Very high']|carsIncoming['medium'],Traffic['high'])
Rule24=ctrl.Rule(carsWaiting['Very high']|carsIncoming['high'],Traffic['Very high'])
Rule25=ctrl.Rule(carsWaiting['Very high']|carsIncoming['Very high'],Traffic['Very high'])

rule_control_system=ctrl.ControlSystem([Rule1,Rule2,Rule3,Rule4,Rule5,Rule6,Rule7,Rule8,Rule9,Rule10,Rule11,Rule12,Rule13,Rule14,Rule15,Rule16,Rule17,Rule18,Rule19,Rule20,Rule21,Rule22,Rule23,Rule24,Rule25])
rule_simulation=ctrl.ControlSystemSimulation(rule_control_system)



root.mainloop()

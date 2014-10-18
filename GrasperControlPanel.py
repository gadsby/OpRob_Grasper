#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import Tkinter
from Servo import *
import math
import threading

class simpleapp_tk(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initializeServo()
        self.initialize()

    def initialize(self):
        self.grid()

        #Angle Entry Box
        self.angleEntryVariable = Tkinter.StringVar()
        self.angleEntry = Tkinter.Entry(self,
            textvariable=self.angleEntryVariable)
        self.angleEntry.grid(column=0,row=0,sticky='EW')
        self.angleEntry.bind("<Return>", self.OnPressEnter_Angle)
        self.angleEntryVariable.set(u"Enter Angle Here")

        #Angle Entry Button
        angleEnterButton = Tkinter.Button(self,text=u"Enter",
            command=self.OnPressButton_Angle)
        angleEnterButton.grid(column=1,row=0)

        #Angle Info Box
        self.angleLabelVariable = Tkinter.StringVar()
        angleLabel = Tkinter.Label(self,textvariable=self.angleLabelVariable,
                              anchor="w",fg="white",bg="blue")
        angleLabel.grid(column=0,row=1,columnspan=2,sticky='EW')
        self.angleLabelVariable.set(u"Angle: "+str(int(serv.read_angle()))+" Deg")

        #Angle Slider Box
#        angleSlider = Tkinter.Scale(self, from_=70, to=80)
#        angleSlider.grid(column=0,row=2,columnspan=2,sticky='EW')
#        angleSlider.pack()



        #Load Info Box
        self.loadLabelVariable = Tkinter.StringVar()
        loadLabel = Tkinter.Label(self,textvariable=self.loadLabelVariable,
                              anchor="w",fg="white",bg="red")
        loadLabel.grid(column=0,row=3,columnspan=2,sticky='EW')
        self.loadLabelVariable.set(u"Load: "+str(int(serv.read_load()))+" Units")



        #Frame Specifics
        self.grid_columnconfigure(0,weight=1)
        self.resizable(False,False)
        self.update()
        self.geometry('400x400+100+100')    
        self.angleEntry.focus_set()
        self.angleEntry.selection_range(0, Tkinter.END)

    def OnPressButton_Angle(self):
        self.angleLabelVariable.set( "Angle: "+self.angleEntryVariable.get()+" Deg")
        self.loadLabelVariable.set(u"Load: "+str(int(serv.read_load()))+" Units")
        serv.move_angle(math.radians(float(self.angleEntryVariable.get())))
        self.angleEntry.focus_set()
        self.angleEntry.selection_range(0, Tkinter.END)

    def OnPressEnter_Angle(self, event):
        self.OnPressButton_Angle()

    def initializeServo(self):
        global dyn
        # ADJUST THIS FOR YOUR OWN COM PORT
        dyn = USB2Dynamixel_Device('/dev/tty.usbserial-AH01FOYT')
        global serv
        serv = Robotis_Servo( dyn, 1, "MX")

if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('Servo Control')
    app.mainloop()
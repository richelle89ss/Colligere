from Tkinter import *
import time
from textstar import *
from autodetectserial import auto_detect_serial_unix

class TkSerialSelection(Frame):
	def __init__(self,parent=None, **kw):
		Frame.__init__(self,parent=None, **kw)
		self.ports = auto_detect_serial_unix()
		print self.ports

class StopWatch(Frame):  
    """ Implements a stop watch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self.ts = TextStar("/dev/ttyACM0",9600,1)
        #self.ts = None
        self._start = 0.0
        self.cursorStyle = 0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.sendCR = IntVar()
        self.showEcho = IntVar()             
        self.makeWidgets()
        self.counter = 10
        self.SerialSelect = TkSerialSelection(self)
        
        self._update()

    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self, text="Com Port:")
        l.grid(row=0,column=0,sticky=W)
        self.port = Label(self, text=(self.ts.port.port,self.ts.port.baudrate))
        #self.port = Label(self, text="Serial Port")
        self.port.grid(row=0,column=1,sticky=E)
        
        self.etrSend = Entry(self, textvariable="")
        self.etrSend.config(width=80)
        self.etrSend.grid(row=1,column=0,sticky=E+W)
        btnSend = Button(self,text='Send',command=self._send)
        btnSend.grid(row=1,column=1,sticky=W)
        scrollbar = Scrollbar(self)
        scrollbar.grid(row=2,column=1,sticky=N+S+W)
        self.txtTerminal = Text(self,yscrollcommand=scrollbar.set)
        self.txtTerminal.grid(row=2,column=0,sticky=E+W)
        scrollbar.config(command=self.txtTerminal.yview)
        self._setTime(self._elapsedtime)
        frame = Frame()
        frame.grid(row=3,columnspan=2)
        self.chkCR = Checkbutton(frame, text="Send CR",var=self.sendCR)
        self.chkCR.grid(row=0,column=0)
        Button(frame, text='Start', command=self.Start).grid(row=0,column=1,sticky=E+W,padx=5, pady=5)
        Button(frame, text='Stop', command=self.Stop).grid(row=0,column=2,sticky=E+W,padx=5, pady=5)
        Button(frame, text='Clear History', command=self.Reset).grid(row=0,column=3,sticky=E+W,padx=5, pady=5)
        self.chkEcho = Checkbutton(frame, text="Show Echo",var=self.showEcho)
        self.chkEcho.grid(row=1,column=0)

        Button(frame, text='Clear Screen', command=self.clearScreen).grid(row=1,column=1,sticky=E+W,padx=5, pady=5)
        self.btnCursor = Button(frame, text=('Toggle Cursor: '+str(self.cursorStyle)), command=self.toggleCursor)
        self.btnCursor.grid(row=1,column=2,sticky=E+W,padx=5, pady=5)
        Button(frame, text='Send Key States', command=self.ts.SendKeyStates).grid(row=1,column=3,sticky=E+W,padx=5, pady=5)

    def _send(self):
        if not(self.etrSend.get()==""):
            self.ts.write(self.etrSend.get())
            print self.sendCR.get()
            if (self.sendCR.get()):
                self.ts.write("\x0d")
            self.etrSend.delete(0,END)

    def clearScreen(self):
        self.ts.ClearScreen()

    def toggleCursor(self):
        self.ts.CursorStyle(self.cursorStyle)
        self.cursorStyle += 1
        if self.cursorStyle > 4:
            self.cursorStyle = 0
        self.btnCursor.config(text=('Toggle Cursor: '+str(self.cursorStyle)))
    
    def _update(self): 
        """ Update the label with elapsed time. """
        data = self.ts.read()
        if len(data):
            #print data
            data1 = hexdump(data,16)
            self.timestr.set(data1)
            self.txtTerminal.insert(END,data1+"\n")
            self.txtTerminal.yview(END)
        self._timer = self.after(200, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        pass

        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        self.counter += 1
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._transmit()
            #self._update()
            self._running = 1

    def _transmit(self):
        """ Transmit the data periodically """
        if self._running:
            text = "Hello: " + str(self.counter)
            self.ts.write(text)
            self.counter += 1
        self._timer2 = self.after(1000, self._transmit)
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self.txtTerminal.delete(1.0,END)
        
        
def main():
    root = Tk()
    root.title("TextStar Terminal")
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    serialmenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    menu.add_cascade(label="Serial Port", menu=serialmenu)
    filemenu.add_command(label="New")
    sw = StopWatch(root)
    sw.grid(row=0,padx=5,pady=5)
    root.mainloop()

if __name__ == '__main__':
    main()

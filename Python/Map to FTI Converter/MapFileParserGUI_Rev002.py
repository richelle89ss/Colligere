from Tkinter import *
from MapFileParser import *
import tkFileDialog
import tkMessageBox
import os

class FileSelect(Frame):
    def __init__(self,master,label,opensave,filetype,**kw):
        Frame.__init__(self,master)
        self.configure(**kw)
        self.file = StringVar()
        self.opensave = opensave
        self.filetypes = filetype

        self.Label = Label(self, text=label)
        self.Label.config(width=10,anchor=E)
        self.filenamebox = Entry(self,text=self.file)
        self.filenamebox.config(width=50)
        self.btnBrowse = Button(self,text='Browse',command=self.browse_file)
        self.btnBrowse.config(width=10)
        self.Label.grid(row=0,column=0,pady=5,sticky=E)
        self.filenamebox.grid(row=0,column=1,pady=5)
        self.btnBrowse.grid(row=0,column=2,pady=5,padx=5)
    def browse_file(self):
        
        filename = []
        if self.opensave == "open":
            filename = tkFileDialog.askopenfilename(filetypes=self.filetypes)
        else:
            filename = tkFileDialog.asksaveasfilename(filetypes=self.filetypes)
        #print filename
        self.file.set(filename)
        #self.filenamebox.config(text=filename)
    def get_filename(self):
        return self.file.get()

class AddRemoveBoxes(LabelFrame):
    def __init__(self,master,**kw):
        LabelFrame.__init__(self,master,**kw)
        #self.symbols = Frame(self)
        Label(self,text="Inactive").grid(row=0,column=0)
        Label(self,text="Active").grid(row=0,column=3)
        self.sb1 = Scrollbar(self, orient=VERTICAL)
        self.symbollist = Listbox(self,yscrollcommand=self.sb1.set)
        self.sb1.config(command=self.symbollist.yview)
        self.sb1.grid(row=1,column=1,sticky=N+S,rowspan=2)
        self.symbollist.grid(row=1,column=0,rowspan=2,padx=5,pady=5,sticky=W)
        
        
        #self.symbollist.bind('<Button-1>', self.add)
        self.addbutton = Button(self,text="Add >>",command=self.add)
        self.addbutton.grid(row=1,column=2,padx=5,pady=5)
        self.removebutton = Button(self,text="<< Remove",command=self.remove)
        self.removebutton.grid(row=2,column=2)
        self.sb2 = Scrollbar(self, orient=VERTICAL)
        self.activelist = Listbox(self,yscrollcommand=self.sb2.set)
        self.sb2.config(command=self.activelist.yview)
        self.sb2.grid(row=1,column=4,sticky=N+S,rowspan=2)
        self.activelist.grid(row=1,column=3,rowspan=2,padx=5,pady=5,sticky=E)
    def add(self,event=None):
        #print "Add Item"
        #index = self.symbollist.curselection()
        seltext = self.symbollist.get(ACTIVE)
        self.activelist.insert(END,seltext)
        self.symbollist.delete(ACTIVE)
        #print seltext
        #sym = list(self.symbollist.get(0,END))
        #print sym
    def remove(self):
        seltext = self.activelist.get(ACTIVE)
        self.symbollist.insert(END,seltext)
        self.activelist.delete(ACTIVE)
    def getactivelist(self):
        return list(self.activelist.get(0,END))

class MapFileCSVParser(Frame):
    def __init__(self,parent=None, **kw):
        Frame.__init__(self,parent,**kw)
        self.symbolsloaded = False
        self.inputfilebox = FileSelect(self,"Map File","open",[('Map','*.map'),('All Files','*.*')])
        self.inputfilebox.grid(row=0)
        self.symbolfilebox = FileSelect(self,"Symbol File","open",[('Text','*.txt'),('All Files','*.*')])
        self.symbolfilebox.grid(row=1)
        self.outputfilebox = FileSelect(self,"CSV Output","save",[('CSV','*.csv'),('All Files','*.*')])
        self.outputfilebox.grid(row=2)
        
        self.frmButtons = Frame(self)
        self.btnGetSymbols = Button(self.frmButtons,text="Get Symbols",command=self.process_symbols)
        self.btnGetSymbols.grid(row=0, column=0,padx=10,pady=10,sticky=E+W)
        self.btnGo = Button(self.frmButtons,text="Generate FTI File",command=self.Process)
        self.btnGo.grid(row=0,column=1,padx=10,pady=10,sticky=E+W)
        self.frmButtons.grid(row=3)
        
        self.symbols = AddRemoveBoxes(self,text="Symbols",padx=5,pady=5)
        self.symbols.grid(row=4,column=0,columnspan=3,sticky=E+W)
    def Process(self):
        infile = self.inputfilebox.get_filename()
        outfile = self.outputfilebox.get_filename()
        symfile = self.symbolfilebox.get_filename()
        if infile == "":
            tkMessageBox.showwarning("Error","No input file selected")
        elif symfile == "":
            tkMessageBox.showwarning("Error","No Symbol file selected")
        elif outfile == "":
            tkMessageBox.showwarning("Error","No output file selected")
        else:
            if self.symbolsloaded:
                outputCSV(outfile,Process(infile,self.symbols.getactivelist()))
            else:
                outputCSV(outfile,Process(infile,loadSymbols(symfile)))
            tkMessageBox.showinfo("Task Complete","Output File Generated")
    def process_symbols(self):
        print "Processing Symbols"
        symfile = self.symbolfilebox.get_filename()
        if symfile == "":
            tkMessageBox.showwarning("Error","No Symbol file selected")
        else:
            print "File Found"
            symbol_list = loadSymbols(symfile)
            for item in symbol_list:
                self.symbols.symbollist.insert(END,item)
        self.symbolsloaded = True
        

def main():
    root = Tk()
    root.title("Map File to FTI File Parser")
    MapFileCSVParser(root).grid()    
    root.mainloop()
   

if __name__ == '__main__':
    main()

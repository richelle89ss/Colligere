import serial
import struct
import time
from textstarsim import TextStarSim
#port = serial.Serial('/dev/ttyS0')

#outputStr = struct.pack('BBB',0xaa,6,255)
#port.write(outputStr)
#port.close()

CURSORSTYLE_NO = 0
CURSORSTYLE_SOLID = 1
CURSORSTYLE_FLASH_BLOCK = 2
CURSORSTYLE_SOLID_UL = 3
CURSORSTYLE_FLASH_UL = 4

def write(data):
    print hexdump(data,16)

def hexdump(src, length=8): 
    result = [] 
    digits = 4 if isinstance(src, unicode) else 2 
    for i in xrange(0, len(src), length): 
       s = src[i:i+length] 
       hexa = b' '.join(["%0*X" % (digits, ord(x))  for x in s]) 
       text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s]) 
       result.append( b"%04X   %-*s   %s" % (i, length*(digits + 1), hexa, text) ) 
    return b'\n'.join(result)

def limit(value,min,max):
    if value > max:
        value = max
    if value < min:
        value = min
    return value

class TextStar:
    def __init__(self,port,baud,quiet=0):
        ##Initialise Serial Port Here
        self.port = serial.Serial(port, baud,timeout=1)
        self.quiet = quiet
        print "Serial Port:", port, "\nBaud Rate:", baud
    def write(self,data):
        if (not self.quiet):
            write(data)
        self.port.write(data)
    def read(self,format=''):
        if format == 'hex':
            print "Echo:\n", hexdump(self.port.read(self.port.inWaiting()),16)
        else:
            return self.port.read(self.port.inWaiting())
    def CursorLeft(self):
        self.write(struct.pack('B',8))
    def CursorForward(self):
        self.write(struct.pack('B',9))
    def CursorDown(self):
        self.write(struct.pack('B',10))
    def CursorUp(self):
        self.write(struct.pack('B',11))
    def Clear(self):
        self.write(struct.pack('B',12))
    def CarriageReturn(self):
        self.write(struct.pack('B',13))
    def Delete(self):
        self.write(struct.pack('B',127))
    def UncappedBarGraph(self,width,percent):
        self.write(struct.pack('BBBB',254,66,int(width),int(limit(percent,0,100))))
    def CursorStyle(self,style):
        self.write(struct.pack('BBB',254,67,int(style)))
    def DefineCustomCharacter(self,ch,b1,b2,b3,b4,b5,b6,b7,b8):
        self.write(struct.pack('BBBBBBBBBBB',254,68,ch,b1,b2,b3,b4,b5,b6,b7,b8))
    def GoToLine(self,line):
        self.write(struct.pack('BBB',254,71,int(line)))
    def CursorHome(self):
        self.write(struct.pack('BB',254,72))
    def SendKeyStates(self):
        self.write(struct.pack('BB',254,75))
    def MoveToLineStart(self):
        self.write(struct.pack('BB',254,76))
    def ScrollWindow(self,dir):
        self.write(struct.pack('BBB',254,79,int(dir)))
    def PositionCursor(self,l,c):
        self.write(struct.pack('BBBB',254,80,int(l),int(c)))
    def ResetScreen(self):
        self.write(struct.pack('BB',254,83))
    def ClearScreen(self):
        self.write(struct.pack('BB',254,83))
    def VersionDisplay(self):
        self.write(struct.pack('BB',254,86))        
    def CappedBarGraph(self,width,percent):
        self.write(struct.pack('BBBB',254,98,int(width),int(limit(percent,0,100))))
    def DefineKeys(self,key_no,code):
        self.write(struct.pack('BBBB',254,107,int(key_no),int(code)))
    def SendVersion(self):
        self.write(struct.pack('BB',254,118))
    def LevelIndicator(self,line,label,percent):
        self.GoToLine(line)
        self.write(centre_text(label,16))
        self.GoToLine(line+1)
        self.CappedBarGraph(16,percent)

def centre_text(text,size):
    text = text.center(size)
    return text


if __name__ == "__main__":
    ts = TextStar("/dev/ttyUSB0",115200)
    tss=TextStarSim()
    ts.write("Hi\r\n")
    ts.CursorLeft()
    ts.UncappedBarGraph(0x31,0xaa)
    ts.DefineCustomCharacter(1,0x31,101,102,103,104,105,106,107)
    ts.ScrollWindow(1)
    tss.print_screen()
    ts.LevelIndicator(0,"Battery",50)
    ts.LevelIndicator(2,"Fuel",25)
    ts.LevelIndicator(4,"Oxygen",90)
    time.sleep(1)
    rx = ts.read()
    tss.write(rx)
    tss.print_screen()
    ts.ScrollWindow(1)
    ts.ScrollWindow(1)
    time.sleep(1)
    rx = ts.read()
    tss.write(rx)
    tss.print_screen()

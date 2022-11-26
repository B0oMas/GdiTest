from win32gui import *
from win32api import *
from win32ui import *
from win32con import *
from random import *
from threading import _start_new_thread as thread
import keyboard
from datetime import datetime
import time
import schedule
import subprocess
import winsound

#http://timgolden.me.uk/pywin32-docs/win32gui.html gdi testint

time = GetSystemTime() # pc laika paem metai, menuo, diena savaitej, diena, valanda, minute, sekunde, milisekund
cYear = time[0] # c reisk current
cMonth = time[1]
cWeekDay = time[2]
cDay = time[3]
cHour = time[4]
cMinute = time[5]
cSecond = time[6]
# second = time[6]
# laikas = str(second)

desk = GetDC(0) # pirma monika paem
x = GetSystemMetrics(0) # width
y = GetSystemMetrics(1) # height

def draw_rects_rgb(dc, x, y, w, h, count, dx, dy): # rgb rectangle ekrane
    for i in range(count):
        brush = CreateSolidBrush(RGB(
            randrange(255),
            randrange(255),
            randrange(255)
        )) # sukurt brush
        SelectObject(desk, brush) # brush naudojims
        PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, PATINVERT)
        DeleteObject(brush) # free memory
        
def draw_rects(dc, x, y, w, h, count, dx, dy): # rectangle ekrane
    for i in range(count):
        PatBlt(dc, x + i * dx, y + i * dy, w - 2 * i * dx, h - 2 * i * dy, PATINVERT)

def flash(): # balta ekrana spamin
    BitBlt(desk, 0, 0, x, y, desk, 0, 0, NOTSRCCOPY) # invertint screen

def tunnel(): # tunelis
    StretchBlt(desk, 0, 0, x, y, desk, -20, -20, x + 40, y + 40, SRCCOPY)

def rgbWindowSpam(): # spalvoti kvadratai ekrane random position
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255)
    )) # sukurt brush
    SelectObject(desk, brush) # brush naudojims
    PatBlt(desk, randrange(x), randrange(y), randrange(x), randrange(y), PATINVERT)
    DeleteObject(brush) # free memory

def drawIcons(): # iconus spawnin
    IconError = LoadIcon(None, IDI_ERROR)
    IconWarning = LoadIcon(None, IDI_WARNING)
    DrawIcon(desk, randrange(x), randrange(y), choice([IconError, IconWarning]))

def msg_thread(): # message spammeris
    thread(MessageBox, ("Juokiasi Jonas, kad Petras dalbajobas", "hehexd", MB_ICONWARNING | MB_OK))
    Sleep(50)

def imInsideYourPC(): # notepad atidaro ir tur parasyt kazku
    subprocess.Popen("notepad")
    keyboard.send("n")
    Sleep(700)
    keyboard.send("o")
    Sleep(700)
    keyboard.send('space')
    Sleep(700)
    keyboard.send('m')
    Sleep(700)
    keyboard.send('o')
    Sleep(700)
    keyboard.send('r')
    Sleep(700)
    keyboard.send('e')
    Sleep(700)
    keyboard.send('space')
    Sleep(700)
    keyboard.send("f")
    Sleep(700)
    keyboard.send("o")
    Sleep(700)
    keyboard.send("r")
    Sleep(700)
    keyboard.send("t")
    Sleep(700)
    keyboard.send("n")
    Sleep(700)
    keyboard.send("i")
    Sleep(700)
    keyboard.send("t")
    Sleep(700)
    keyboard.send("e")

def playSounds(): # random sounds leidinej possible earrape
    winsound.Beep(randrange(100, 1500), 3000)

def elipse():
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255)
    )) # sukurt brush
    SelectObject(desk, brush) # brush naudojims
    Ellipse(desk, 0, 0, randrange(1, 1920), randrange(1, 1080))
    DeleteObject(brush) # free memory

def line():
    LineTo(desk, randrange(0, 1920), randrange(0, 1080))

def text():
    x = randrange(1, 1920)
    y = randrange(1, 1080)
    SetTextColor(desk, RGB(randrange(255), randrange(255), randrange(255)))
    DrawText(desk, "NO MORE FORTNITE", 16, (x, y, x + 200, y + 200), SRCCOPY)

def circle():
    x = randrange(1, 1920)
    y = randrange(1, 1080)
    brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255)
    )) # sukurt brush
    SelectObject(desk, brush) # brush naudojims
    Pie(desk, 0, 0, 1920, randrange(1, 1080), randrange(x), randrange(y), x, y)
    DeleteObject(brush) # free memory
    

def do_payloads(): # reik padaryt kad pasileistu ir pradingtu ir neuzmirst kazkada gui idet kaip test tool
    schedule.every(5).seconds.do(drawIcons)
    schedule.every(15).seconds.do(rgbWindowSpam)
    schedule.every(1).minutes.do(tunnel)


#imInsideYourPC()
run = True
while run:
    # circle()
    text()
    # schedule.run_pending()
    # do_payloads()
    # rgbWindowSpam()
    # draw_rects_rgb(desk, 0, 0, 1920, 1080, 30, 15, 15) # per visa ekrana rectangle epilepsy
    # draw_rects(desk, 0, 0, 1920, 1080, randrange(15, 150), 15, 15) # 6 option keist for dankness
    # draw_rects(desk, 100, 100, 250, 250, 13, 10, 10) # rectangle
    # flash()
    # tunnel()
    #drawIcons()
    #msg_thread()
    #playSounds()
    Sleep(10)
    # if(keyboard.is_pressed('ctrl+1')):
    #     schedule.clear()
    if(keyboard.is_pressed('esc')):
        run = False

ReleaseDC(desk, GetDesktopWindow()) # release memory
DeleteDC(desk) # delete dc


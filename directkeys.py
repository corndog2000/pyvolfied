import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

U = 0xC8
D = 0xD0
L = 0xCB
R = 0xCD
LCTRL = 0x1D

# Number row
NUM1 = 0x02
NUM5 = 0x06


# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def TapKey(hexKeyCode, delay=0.025):
    PressKey(hexKeyCode)
    time.sleep(delay)
    ReleaseKey(hexKeyCode)

# Movement directions

def insert_coin():
    PressKey(NUM5)
    ReleaseKey(NUM5)

def start():
    PressKey(NUM1)
    ReleaseKey(NUM1)

def up():
    PressKey(LCTRL)
    PressKey(U)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(R)

def down():
    PressKey(LCTRL)
    PressKey(D)
    ReleaseKey(U)
    ReleaseKey(L)
    ReleaseKey(R)

def left():
    PressKey(LCTRL)
    PressKey(L)
    ReleaseKey(D)
    ReleaseKey(U)
    ReleaseKey(R)

def right():
    PressKey(LCTRL)
    PressKey(R)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(U)

def stop():
    ReleaseKey(LCTRL)
    ReleaseKey(U)
    ReleaseKey(D)
    ReleaseKey(L)
    ReleaseKey(R)

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

if __name__ == '__main__':
    while (True):
        PressKey(0x11)
        time.sleep(1)
        ReleaseKey(0x11)
        time.sleep(1)
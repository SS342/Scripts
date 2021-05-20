from ctypes import windll, Structure, c_long, byref
import  time


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}


pos = queryMousePosition()
while True:
    pos = queryMousePosition()
    print(pos)
    time.sleep(0.7)
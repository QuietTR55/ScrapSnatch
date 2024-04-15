import tkinter as tk
from tkinter import *
import screenshot_proccesor

def button_event(event : Event):
    type(event)
    checkstring = f'{event}'
    #print(checkstring)
    if "ButtonPress" in checkstring:
        print(f'click at {event.x} {event.y}')
        global start_point_x
        global start_point_y

        global start_point_x_root
        global start_point_y_root

        start_point_x_root, start_point_y_root = event.x, event.y

        start_point_x, start_point_y = event.x, event.y
        canvas.coords(rectangle,start_point_x,start_point_y,start_point_x,start_point_y)

    if "Motion" in checkstring:
        global end_point_x
        global end_point_y

        global end_point_x_root
        global end_point_y_root

        end_point_x_root = event.x_root
        end_point_y_root = event.y_root

        end_point_x, end_point_y = event.x,event.y
        #print(f'new coords {start_point_x}, {start_point_y}, {end_point_x}, {end_point_y}')
        canvas.coords(rectangle,start_point_x,start_point_y,event.x,event.y)

    if "ButtonRelease" in checkstring:
        window.quit()
        window.destroy()
        screenshot_proccesor.get_screenshot(start_point_x_root,start_point_y_root,end_point_x_root,end_point_y_root)
        pass

def start_gui():

    print("starting gui")
    global window
    window = tk.Tk()
    h = window.winfo_screenheight()
    w = int(window.winfo_screenwidth() / 2)
    window.overrideredirect(True)
    window.geometry(f"{w}x{h}+0+0")
    window.configure(background="black")
    window.title("Copier")
    window.wait_visibility(window)
    window.attributes('-topmost',True)
    window.attributes('-fullscreen',True)
    window.attributes('-alpha',0.4)
    global canvas
    canvas = Canvas(window,width= w, height= h,bg='black')
    canvas.size()
    canvas.pack()
    global rectangle
    rectangle = canvas.create_rectangle((0,0,0,0),fill='white',outline = 'white')

    

    canvas.bind("<Button-1>",button_event)
    canvas.bind("<B1-Motion>", button_event)
    canvas.bind("<ButtonRelease-1>",button_event)
    window.mainloop()
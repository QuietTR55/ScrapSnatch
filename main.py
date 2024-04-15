import tkinter as tk
from tkinter import *
import sys
import PIL.Image
import pystray
import screenshot_gui
tray_image = PIL.Image.open("./Assets/Icon_test.png")

icon = pystray.Icon("Neural",tray_image,menu = pystray.Menu(
    pystray.MenuItem("get screenshot",screenshot_gui.start_gui)
))

icon.run()
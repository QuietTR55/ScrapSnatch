from PIL import ImageGrab
from PIL import Image
import easyocr
def get_screenshot(x0,y0,x1,y1):
    reader = easyocr.Reader(['ch_sim','en'])
    if y1 < y0:
        screenshot = ImageGrab.grab(bbox=(x1,y1,x0,y0))
    else:
        screenshot = ImageGrab.grab(bbox=(x0,y0,x1,y1))

    screenshot.save("result.png")
    screenshot.close()
    print("printing result")
    print(reader.readtext('result.png'))
    pass
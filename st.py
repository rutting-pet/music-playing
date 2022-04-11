import tkinter as tk
from PIL import ImageGrab, Image, ImageDraw, ImageTk
import shutil, time, os, configparser

os.makedirs("./export")

width = 700
height = 1000
root = tk.Tk()

pos = 0
lastpos = 0
tag = 0

image_name = Image.open("1.jpg")
cv = tk.Canvas(root, width = width, height = height)
cv.focus_set()
ratio = image_name.size[0]/float(width)
image_resized = image_name.resize((width, int( image_name.size[1] / ratio) ), Image.ANTIALIAS)
image_obj = ImageTk.PhotoImage(image_resized)

img = cv.create_image(width/2, pos, image = image_obj, anchor = "n")

def drag(event):
    cv.coords(line, 0,event.y, width, event.y)
    split = event.y
    
def cut(event):
    global pos, lastpos, tag
    lastpos = pos
    pos += event.y
    tag += 1
    print(pos, "," , lastpos)
    cv.move(img, 0, -event.y)
    image_name.crop((0,int(lastpos*ratio),image_name.size[0],int(pos*ratio))).save("./export/{:03d}.jpg".format(tag))


line = cv.create_line(0,0,width,0, fill = "red")

cv.bind("<B1-Motion>", drag)
mv = cv.bind('<ButtonRelease-1>', cut)

cv.pack()

root.mainloop()

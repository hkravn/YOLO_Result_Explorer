##########################################################
# Source: https://pythonguides.com/python-tkinter-image/ #
##########################################################

from tkinter import *
from  tkinter import Button, Canvas, Label, filedialog
from PIL import Image, ImageTk
import os

window = Tk()
v = IntVar()
window.title('Result Viewer')
window.geometry('1920x1280')

image_list = []
image_matrix = ["tp", "tn", "fp", "fn", "Total"]
global img
global pos
count = [0 for i in range(5)]


percent = 0
max = 0

def fileupdate(filedir):

    global image_list
    image_list = []

    with os.scandir(filedir) as files:
        for file in files:
            if file.name.find("jpg")!=-1 or file.name.find("png")!=-1:
                if file.name.find("boxxed")!=-1:
                    if file.name.find(image_matrix[0])!=-1 or file.name.find(image_matrix[1])!=-1 or file.name.find(image_matrix[2])!=-1 or file.name.find(image_matrix[3])!=-1:
                        pass
                    else:
                        image_list.append(file.name)


def imageopen(no=0):

    v.set(5)
    global pos
    global image_list

    pos = no
    imag = os.path.join(filedir, image_list[no])
    image = Image.open(imag)
    resize_img = image.resize((1024, 500))
    img = ImageTk.PhotoImage(resize_img)
    disp_img.config(image=img)
    disp_img.image = img

    if no==max-1:
        button_open_next["state"] = "disabled"
    elif no==0:
        button_open_prev["state"] = "disabled"
    else:
        button_open_next["state"] = "active"
        button_open_prev["state"] = "active"
    
    percent = (no/max)*100
    percent = str(percent)[:5]
    st = "Result Viewer - " + str(max) + " files, Status = " + percent + "%"

    window.title(st)


def setfolder():

    global filedir
    global max
    global pos
    pos = 0
    
    filedir = filedialog.askdirectory(
        initialdir='/'
    )

    fileupdate(filedir)

    # staten = "active"

    max = len(image_list)
    st = "Result Viewer - " + str(max) + " files"

    window.title(st)


def rcounter(val):
    global count

    if val==1:
        count[0] += 1
    elif val==2:
        count[1] += 1
    elif val==3:
        count[2] += 1
    elif val==4:
        count[3] += 1
    else:
        print("Error!!!!")


def summarizer():

    countb = 0
    
    with os.scandir(filedir) as files:
        for file in files:
            if file.name.find("jpg")!=-1 or file.name.find("png")!=-1:
                if file.name.find("boxxed")!=-1:
                    countb += 1

    for i in range(5):
        print("{0} : {1}".format(image_matrix[i], count[i]))
    print(countb)


frame = Frame(window)
frame.pack()

button_set_folder = Button(
    window,
    text="Select Folder",
    command=setfolder
)
button_open_image = Button(
    window,
    text='Open Image',
    command=lambda: imageopen(pos)
)
button_open_prev = Button(
    window,
    text="Previous Image",
    command=lambda: imageopen(pos-1)
)
button_open_next = Button(
    window,
    text="Next Image",
    command=lambda: imageopen(pos+1)
)
button_summarizer = Button(
    window,
    text="Summarize the Results",
    command=summarizer,
)
#tn
button_tp = Radiobutton(
    window,
    text="Hai. Mila",
    variable=v,
    value=1,
    command=lambda: rcounter(1)
)
#tn
button_tn = Radiobutton(
    window,
    text="Nai Hai. Nai Mila",
    variable=v,
    value=2,
    command=lambda: rcounter(2)
)
#fp
button_fp = Radiobutton(
    window,
    text="Nai Hai. But Mila",
    variable=v,
    value=3,
    command=lambda: rcounter(3)
)
#fn
button_fn = Radiobutton(
    window,
    text="Hai. But nai Mila",
    variable=v,
    value=4,
    command=lambda: rcounter(4)
)

button_set_folder.pack(side=TOP, padx=20)

disp_img = Label()
disp_img.pack(padx=20,pady=20, expand=True)

button_open_image.pack(side=RIGHT, padx=20)
button_open_prev.pack(side=LEFT, padx=20)
button_tp.pack(side=LEFT, padx=20)
button_tn.pack(side=LEFT, padx=20)  
button_fp.pack(side=LEFT, padx=20)
button_fn.pack(side=LEFT, padx=20)
button_open_next.pack(side=LEFT, padx=20)
button_summarizer.pack(side=LEFT, padx=50)

window.mainloop()

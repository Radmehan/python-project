import tkinter
import cv2      #pip install opencv-python
import PIL.Image, PIL.ImageTk  #pip install pillow
from functools import partial
import threading    #save window from hang
import imutils
import time

stream=cv2.VideoCapture('clip.mp4')
flag=True

def play(speed):
    global flag
    print(f"You clicked on play. Speed is {speed}")

    # play the video in reversed mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed,frame=stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="white", font="Times 26 italic bold", text="Decision pending")
    flag= not flag





def pending(decision):
    # 1. Display decision pending image
    frame= cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 2. Wait for 1 seconds
    time.sleep(1)

    # 3. Display sponser image
    frame = cv2.cvtColor(cv2.imread("sponsor.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 4. Wait for 1.5 seconds
    time.sleep(1.5)

    # 5. Display out/notout image
    if decision=="out":
        decisionImg="out.png"
    else:
        decisionImg="not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image=frame, anchor=tkinter.NW)

    # 6. Wait for 1 seconds


def out():
    thread=threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()
    print("player is out")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")


#width and hight our main screen
SET_WIDTH=650
SET_HEIGHT=338

#Tkinter gui starts
window=tkinter.Tk()
window.title("CodewithHarry Third Umpire Decision Review Kit")
cv_img=cv2.cvtColor(cv2.imread("welcome.png"), cv2.COLOR_BGR2RGB)
canvas=tkinter.Canvas(window, widt=SET_WIDTH, height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas= canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


#button to control palyback
btn=tkinter.Button(window,text="<< Previous (fast)", width=50, command=partial(play, -25))
btn.pack()

btn=tkinter.Button(window,text="<< Previous (slow)", width=50, command=partial(play, -2))
btn.pack()

btn=tkinter.Button(window,text="Next (slow) >>", width=50, command=partial(play, 2))
btn.pack()

btn=tkinter.Button(window,text="Next (fast) >>", width=50, command=partial(play, 25))
btn.pack()

btn=tkinter.Button(window,text="Give Out", width=50, command=out)
btn.pack()

btn=tkinter.Button(window,text="Give Not Out", width=50, command=not_out)
btn.pack()


window.mainloop()

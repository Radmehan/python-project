import pyautogui    # pip install pyautogui
from PIL import Image, ImageGrab   # pip install pillow
from numpy import asarray
import time

# while True:
#     pyautogui.keyDown('h')
#     pyautogui.keyDown('a')
#     pyautogui.keyDown('r')
#     pyautogui.keyDown('r')
#     pyautogui.keyDown('y')

def hit(key):
    pyautogui.keyDown(key)


def isCollide(data):
   # draw the rectangle for birds
    for i in range(400, 422):
        for j in range(245, 340):
            if data[i, j] < 100:
                hit('down')
                return True

    # draw the rectangle for cactus
    for i in range(400,445):  # 435,490
        for j in range(340,395):
            if data[i, j] < 100:
                hit('up')
                return True
    return False



if __name__ == '__main__':
    print("Hey...Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit("up")
    while True:
        image = ImageGrab.grab().convert('L')
        data=image.load()
        isCollide(data)

        # print(asarray(image))

        # draw the rectangle for cactus
'''
        for i in range(400,445):        #435,490
            for j in range(340,395):
                data[i,j]=0

        # draw the rectangle for birds
        for i in range(400,422):
            for j in range(245, 340):
                data[i, j] = 171

        image.show()
        break
'''

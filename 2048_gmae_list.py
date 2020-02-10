from PIL import ImageGrab, ImageOps
import pyautogui
import time

up =100
left = 101
down = 102
right = 103

#while True:
#    print(pyautogui.displayMousePosition())

currentgrid = [0,0,0,0,
               0,0,0,0,
               0,0,0,0,
               0,0,0,0]

#scoregrid = [135, 121, 102 , 99,
#             72, 76, 99, 88,
#             60, 56,  37, 16,
#             12,  9,  5, 3]

scoregrid = [12, 9, 5 , 3,
             60, 56, 37, 16,
             72, 76,  88, 99,
             135,  121,  102, 99]

class Cords():
    cord11 = (540,350)
    cord12 = (650,350)
    cord13 = (760,350)
    cord14 = (870,350)
    cord21 = (540,460)
    cord22 = (650,460)
    cord23 = (760,460)
    cord24 = (870,460)
    cord31 = (540,570)
    cord32 = (650,570)
    cord33 = (760,570) 
    cord34 = (870,570)
    cord41 = (540,680)
    cord42 = (650,680)
    cord43 = (760,680)
    cord44 = (870,680)
    
    cordArray = [cord11, cord12, cord13, cord14,
                 cord21, cord22, cord23, cord24,
                 cord31, cord32, cord33, cord34,
                 cord41, cord42, cord43, cord44
                 ]
class Values():
    empty = [195]
    two = [229, 228]
    four = [225, 224]
    eight = [190,191]
    sixteen = [172, 173]
    thirtytwo = [157,158, 159]
    sixtyfour = [135, 137, 138, 139, 143, 136]
    onetwentyeight = [205]
    twofiftysix = [201]
    fiveonwtwo = [197]
    onezerotwofour = [193] 
    twozerofoureight = [189]
    
    valuearray = [empty, two, four, eight,
              sixteen, thirtytwo, sixtyfour,
              onetwentyeight, twofiftysix, fiveonwtwo,
              onezerotwofour, twozerofoureight]
def getgrid():
#    time.sleep(2)
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    for index, cord in enumerate(Cords.cordArray):
        pixel = grayImage.getpixel(cord)
#        print(pixel)

        for i in Values.valuearray:
            if pixel in i:
                pos = Values.valuearray.index(i)
#        pos = Values.valuearray.index(pixel)
        if pos == 0:
            currentgrid[index] = 0
        else:
            currentgrid[index] = pow(2, pos)

def printgrid(grid):
    for i in range(16):
        if i%4 == 0:
            print("[" + str(grid[i]) + " " + str(grid[i+1]) + " " + str(grid[i+2]) + " " + str(grid[i+3]) + "]" )
            
def swiperow(row):
    prev = -1 #previous non zero element
    i=0
    temp = [0,0,0,0]
    
    for element in row:
        if element != 0:
            if prev == -1:
                prev = element
                temp[i] = element
                i += 1
            elif prev == element:
                temp[i-1] = 2*prev
                prev = -1
            else:
                prev = element
                temp[i] = element
                i += 1
                
    return temp


def getnextgrid(grid,move):
    temp = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]
    
    if move == up:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i +4*j])
            row= swiperow(row)
            for j, val in enumerate(row):
                temp[i+4*j] = val
        return temp
    elif move == left:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4*i +j])
            row= swiperow(row)
            for j, val in enumerate(row):
                temp[4*i+j] = val
        return temp
    elif move == down:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i +4*(3-j)])
            row= swiperow(row)
            for j, val in enumerate(row):
                temp[i+4*(3-j)] = val
        return temp
    elif move == right:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4*i + (3-j)])
            row= swiperow(row)
            for j, val in enumerate(row):
                temp[4*i + (3-j)] = val
        return temp
        

def getscore(grid):
    score = 0
    for i in range(4):
        for j in range(4):
             score +=  grid[i+4*j]+scoregrid[i+4*j]    
        return score
    
def getbestmove(grid):
    scoreup = getscore(getnextgrid(grid,up))
    scoredown = getscore(getnextgrid(grid,down))
    scoreleft = getscore(getnextgrid(grid,left))
    scoreright = getscore(getnextgrid(grid,right))
    
    if not ismovevalid(grid,up):
        scoreup = 0
    if not ismovevalid(grid,down):
        scoredown = 0
    if not ismovevalid(grid,right):
        scoreright = 0
    if not ismovevalid(grid,left):
        scoreleft = 0
    
    maxscore = max(scoreup,scoredown, scoreleft, scoreright)
    
    if scoredown == maxscore:
        return down
    elif scoreright == maxscore:
        return right
    elif scoreleft == maxscore:
        return left
    elif scoreup == maxscore:
        return up
    
def performmove(move):
    if move == up:
        pyautogui.keyDown("up")
        print("up")
        time.sleep(0.05)
        pyautogui.keyUp("up")
    elif move == down:
        pyautogui.keyDown("down")
        print("down")
        time.sleep(0.05)
        pyautogui.keyUp("down")
    elif move == right:
        pyautogui.keyDown("right")
        print("right")
        time.sleep(0.05)
        pyautogui.keyUp("right")
    else:
        pyautogui.keyDown("left")
        print("left")
        time.sleep(0.05)
        pyautogui.keyUp("left")
        
def ismovevalid(grid, move):
    if getnextgrid(grid,move) == grid:
        return False
    else:
        return True

        
def main():
    time.sleep(3)
    while True:
        getgrid()
        performmove(getbestmove(currentgrid))
        time.sleep(0.1)
    
if __name__ == "__main__":
    time.sleep(2)
    main()

#print(swiperow([0,2,4,4]))
#getgrid()
#printgrid(getnextgrid(currentgrid, up))

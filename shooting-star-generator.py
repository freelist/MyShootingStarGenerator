import cv2
import numpy as np
import pygame

def playShooting():
  pygame.mixer.init()
  pygame.mixer.music.load("data/shooting-star.mp3")
  pygame.mixer.music.play()
def transparentOverlay(src, overlay, pos=(0,0)):
    h,w,_ = overlay.shape  
    rows,cols,_ = src.shape
    y,x = pos[0],pos[1]
    
    for i in range(h):
        for j in range(w):
            if x+i >= rows or y+j >= cols:
                continue
            alpha = float(overlay[i][j][3]/255.0) 
            src[x+i][y+j] = alpha*overlay[i][j][:3]+(1-alpha)*src[x+i][y+j]
    return src

# play music
playShooting()
# load and work with images
bImg = cv2.imread("data/background.png")
pngImage = cv2.imread("data/foreground.png" , cv2.IMREAD_UNCHANGED)
i = 0
while pygame.mixer.music.get_busy() == True:
  print i
  result = transparentOverlay(np.copy(bImg), pngImage, (i, i))
  #Display the result
  cv2.imshow("Result", result)
  cv2.waitKey(10)
  i = i + 1
  

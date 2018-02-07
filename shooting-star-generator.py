import cv2
import numpy as np
import pygame

def playShooting():
  pygame.mixer.init()
  pygame.mixer.music.load("data/shooting-star.mp3")
  pygame.mixer.music.play()
def transparentOverlay(src, overlay, posx, posy, alpha_level = 0.4):
  (h_src, w_src) = image.shape[:2]
  overlay = np.zeros((h_src, w_src, 4), dtype="uint8")
  overlay[posy:wH + posy, posx:wW + posx] = pngImage
  result = image.copy()
  cv2.addWeighted(overlay, alpha_level, result, 1.0, 1.0, result)
  return result

# play music
playShooting()
# load and work with images
image = cv2.imread("data/background.png")
(h,w) = image.shape[:2]
image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
# reading mirko png
pngImage = cv2.imread("data/foreground_res.png" , cv2.IMREAD_UNCHANGED)
(wH, wW) = pngImage.shape[:2]
(B, G, R, A) = cv2.split(pngImage)
B = cv2.bitwise_and(B, B, mask=A)
G = cv2.bitwise_and(G, G, mask=A)
R = cv2.bitwise_and(R, R, mask=A)
pngImage = cv2.merge([B, G, R, A])

i = 0
while pygame.mixer.music.get_busy() == True:
  if i == w-wW:
    i = 0
  cy = 0
  cx = i
  result = transparentOverlay(image, pngImage, cx, cy, 1.0)
  #Display the result
  cv2.imshow("Result", result)
  cv2.waitKey(10)
  i = i + 1
  

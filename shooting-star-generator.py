import cv2
import numpy as np
import pygame

def playShooting():
  pygame.mixer.init()
  pygame.mixer.music.load("data/shooting-star.mp3")
  pygame.mixer.music.play()

def transparentOverlay(src, foreground, posx, posy, alpha_level = 0.4):
  (h_src, w_src) = src.shape[:2]
  (h_o, w_o) = foreground.shape[:2]

  reshaped = False
  new_pos_x = posx
  new_pos_y = posy
  if posx<0:
    reshaped = True
    new_pos_x = 0
  if posy<0:
    reshaped = True
    new_pos_y = 0

  overlay = np.zeros((h_src, w_src, 4), dtype="uint8")
  if not reshaped:
    overlay[posy:h_o + posy, posx:w_o + posx] = foreground
  else:
    foreground = foreground[-(h_o - abs(posy)):, -(w_o - abs(posx)):]
    (new_h_o, new_w_o) = foreground.shape[:2]
    cv2.imshow("foreground", foreground)
    cv2.waitKey(0)
    overlay[new_pos_y:new_h_o + new_pos_y, new_pos_x:new_w_o + new_pos_x] = foreground

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

cy = 50
cx = 50
speed = 2
while pygame.mixer.music.get_busy() == True:
  result = transparentOverlay(image, pngImage, cx, cy, 1.0)
  #Display the result
  cv2.imshow("Result", result)
  key = cv2.waitKey(0)
  # for debug uncomment the following
  print "Pressed:", key
  if key == 81:
    cx -= speed
  if key == 82:
    cy -= speed
  if key == 83:
    cx += speed
  if key == 84:
    cy += speed

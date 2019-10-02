import numpy as np
import cv2

image = cv2.imread('sample/rose.jpg')
print(image.shape)
print(image[:,:,[0]])
image_rgb = (image[:,:,[2, 1, 0]] * 1.0 / 255).astype(np.float32)
print(image_rgb.shape)
image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2Lab)
print(image.shape)
print(image[:,:,0].shape)
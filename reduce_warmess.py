import cv2
import argparse
import os
from scipy.interpolate import UnivariateSpline
import numpy as np 

parser = argparse.ArgumentParser(description='reduce warmness')
parser.add_argument('--input', help='path to image')
args = parser.parse_args()

if args.input == None:
    print("Please give input image")
    print('Usage: $ python3 reduce_warmness.py --input inputImage.jpg')
    exit()

if os.path.isfile(args.input) == 0:
    print('Input file does not exist')

def create_LUT_8UC1(x, y):
    spl = UnivariateSpline(x, y)
    return spl(range(256))

incr_ch_lut = create_LUT_8UC1([0, 64, 128, 192, 256],
    [0, 70, 140, 210, 256])
# decr_ch_lut = create_LUT_8UC1([0, 64, 128, 192, 256],
#     [0, 30, 80, 120, 192])
decr_ch_lut = create_LUT_8UC1([0, 64, 128, 192, 256],
    [0, 50, 100, 160, 230])

img_bgr_in = cv2.imread(args.input);

c_b, c_g, c_r = cv2.split(img_bgr_in)
c_r = cv2.LUT(c_r, decr_ch_lut).astype(np.uint8)
c_b = cv2.LUT(c_b, incr_ch_lut).astype(np.uint8)
img_bgr_cold = cv2.merge((c_b, c_g, c_r))

c_h, c_s, c_v = cv2.split(cv2.cvtColor(img_bgr_cold,
    cv2.COLOR_BGR2HSV))
c_s = cv2.LUT(c_s, decr_ch_lut).astype(np.uint8)
img_bgr_cold = cv2.cvtColor(cv2.merge(
    (c_h, c_s, c_v)),
    cv2.COLOR_HSV2BGR)

#cv2.imshow("frame", img_bgr_cold)
cv2.imwrite("out_image.jpg", img_bgr_cold)
print('image saved as '+'ou_image')
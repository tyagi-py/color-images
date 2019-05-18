import numpy as np
import cv2 as cv
import argparse
import os.path

parser = argparse.ArgumentParser(description='Colorize GreyScale Image')
parser.add_argument('--input', help='Please give path to image')
args = parser.parse_args()

if args.input==None:
    print('Please give the input greyscale image name.')
    print('Usage example: python fill_color.py --input greyscaleImage.png')
    exit()

if os.path.isfile(args.input)==0:
    print('Input file does not exist')
    exit()

frame = cv.imread(args.input)

protoFile = "./models/model_prototext.prototxt"
weightsFile = "./models/model.caffemodel"
pts_in_hull = np.load('./models/pts_in_hull.npy')

net = cv.dnn.readNetFromCaffe(protoFile, weightsFile)

pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)
net.getLayer(net.getLayerId('class8_ab')).blobs = [pts_in_hull.astype(np.float32)]
net.getLayer(net.getLayerId('conv8_313_rh')).blobs = [np.full([1, 313], 2.606, np.float32)]

W_in = 224
H_in = 224

img_rgb = (frame[:,:,[2, 1, 0]] * 1.0 / 255).astype(np.float32)
img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
img_l = img_lab[:,:,0]

img_l_rs = cv.resize(img_l, (W_in, H_in)) #
img_l_rs -= 50 

net.setInput(cv.dnn.blobFromImage(img_l_rs))
ab_dec = net.forward()[0,:,:,:].transpose((1,2,0)) 

(H_orig,W_orig) = img_rgb.shape[:2]
ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))
img_lab_out = np.concatenate((img_l[:,:,np.newaxis],ab_dec_us),axis=2)
img_bgr_out = np.clip(cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR), 0, 1)

outputFile = args.input[:-4]+'_colored.png'
cv.imwrite(outputFile, (img_bgr_out*255).astype(np.uint8))
print('image saved as '+outputFile)



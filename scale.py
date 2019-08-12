# USAGE
# python scale.py --images images/ --output result/ --width 300

# import the necessary packages
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", type=str, required=True,
	help="path to input directory of images to stitch")
ap.add_argument("-o", "--output", type=str, required=True,
	help="path to the output images")
ap.add_argument("-w", "--width", type=int, required=True,
	help="width of new image")
args = vars(ap.parse_args())

# grab the paths to the input images and initialize our images list
print("[INFO] loading images...")
imagePaths = sorted(list(paths.list_images(args["images"])))
images = []

# loop over the image paths, load each one, and add them to our
# images to stich list
i = 0
for imagePath in imagePaths:
	print(imagePath)
	image = cv2.imread(imagePath)
	image = imutils.resize(image, width=args["width"])
	print("[INFO] Resized")
	i += 1
	cv2.imwrite(args["output"] + "image" + str(i) + ".jpg", image)
	print("[INFO] Saved")

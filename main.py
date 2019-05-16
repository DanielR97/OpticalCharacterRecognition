from PIL import Image
import pytesseract
import cv2
import os

# Specify input image
inputImage = 'media/ocr.png'

# load the example image and convert it to grayscale
image = cv2.imread(inputImage)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)

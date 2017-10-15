from scipy import misc
import numpy
import cv2

#read image
img = cv2.imread('noisylena.png')

#median blur the image
median = cv2.medianBlur(img, 5)
#plot the image
import matplotlib.pyplot as pyplot

f, a = pyplot.subplots(1, 2)
a[0].imshow(img, cmap=pyplot.get_cmap('gray'))
a[0].set_title('Original Noisy Image')

a[1].imshow(median, cmap=pyplot.get_cmap('gray'))
a[1].set_title('Restored Image')

pyplot.show()

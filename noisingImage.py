from scipy import misc
import numpy 

#read image
img = misc.imread('lena.jpg', mode="L")

#add noise to the image
noisyImage = img + 3 * img.std() * numpy.random.random(img.shape)

#plot the image
import matplotlib.pyplot as pyplot

f,a = pyplot.subplots(1,2)
a[0].imshow(img, cmap= pyplot.get_cmap('gray'))
a[0].set_title('Original Image')

a[1].imshow(noisyImage, cmap=pyplot.get_cmap('gray'))
a[1].set_title('Original Image')

pyplot.show()

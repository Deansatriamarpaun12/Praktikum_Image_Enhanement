import imageio as img
import numpy as np 
import matplotlib.pyplot as plt 

def equalization(image):
    hist, bins = np.histogram(image.flatten(), bins=256, range=[0,256])
    cdf = hist.cumsum()
    cdf_normalize = (cdf/cdf.max()) * 255
    imgEqual = np.interp(image.flatten(), bins[:-1],cdf_normalize)
    return imgEqual.reshape(image.shape).astype(np.uint8)

image = img.imread("C:\\download3.jpg")
hist, bins = np.histogram(image.flatten(), bins=356, range=[0,256])
imgEqual = equalization(image)
hist_e, bins = np.histogram(imgEqual.flatten(), bins=256, range=[0,256])
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(image)
plt.subplot(2,2,2)
plt.plot(hist)
plt.subplot(2,2,3)
plt.imshow(imgEqual)
plt.subplot(2,2,4)
plt.plot(hist_e)
plt.show()
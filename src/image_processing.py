import cv2
import matplotlib.pyplot as plt

def read_img(path_to_img):
   return cv2.imread(path_to_img)

def showByCv2(image):
    cv2.imshow('Image', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def showByPlt(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

def splitByChannels(image):
    b, g, r = cv2.split(image)
    return [b, g, r]

def conversionByColorModel(image, model):
    return cv2.cvtColor(image, model)
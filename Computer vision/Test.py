import cv2
import numpy as np
import matplotlib.pyplot as plt
#import tensorflow as tf


print("opencv",cv2.__version__)
print("numpy",np.__version__)
#print("tensorflow",tf.__version__)


img=np.zeros((30,30,3),dtype=np.uint8)
img1=np.zeros((30,30,3),dtype=np.uint8)
new=cv2.add(img,img1)
print(new)





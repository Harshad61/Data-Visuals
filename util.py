import cv2
import json
import numpy as np
from operator import le
import random
from numpy import array

def DataVisualisation(str1,str2):

    f = open(str1)
    data = json.load(f)
    x = []
    y = []
    img2 = []

    img = cv2.imread(str2)
    img1 = np.copy(img) 
    img3 = np.copy(img)


    for j in range(1,len(data)):
         for i in range(len(data[j]["value"]["points"])):
             x.append(((data[j]["value"]["points"][i][0] * data[1]["original_width"])/100))
             y.append(((data[j]["value"]["points"][i][1] * data[1]["original_height"])/100))
         data[j]["id"] = []
         for i in range(len(x)):
              data[j]["id"].append([x[i],y[i]])



    for j in range(1,len(data)):
               pts = np.array(data[j]["id"][len(data[j-1]["id"]):len(data[j]["id"])],np.int32)
               isClosed = True
               color = (1,152,255)
               thickness = 2
               img1 = cv2.polylines(img1,[pts],isClosed,color,thickness)
               img2.append(img1)

               for i in range(len(img2)):
                     img1 = cv2.addWeighted(img1,0.5,img2[i],0.5,0)

    cv2.imshow("image",img1)
    cv2.waitKey(0)



DataVisualisation("Data/1.json","images/1.jpg")
DataVisualisation("Data/2.json","images/2.jpg")
DataVisualisation("Data/3.json","images/3.jpg")
DataVisualisation("Data/4.json","images/4.jpg")
DataVisualisation("Data/5.json","images/5.jpg")
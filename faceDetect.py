import cv2
# Load some pre-trained data on face frontals from opencv (haar cascade Classifier)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#  Choose an imge to Detect Faces
img = cv2.imread('RDJ.png')
# Must convert to gray scale 
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Show off
cv2.imshow('clever Donald',img)
cv2.waitkey()
print("Code Completed !")

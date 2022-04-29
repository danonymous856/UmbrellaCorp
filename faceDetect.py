import cv2
# Load some pre-trained data on face frontals from opencv (haar cascade Classifier)
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#  Choose an imge to Detect Faces
img = cv2.imread('RDJ.png')
# Must convert to gray scale 
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# Draw Rectangle Around Faces
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(w+x,y+h),(0,255,0),2)


print(img)

# Show off
cv2.imshow('clever Donald',grayscaled_img)
cv2.waitKey()
print("Code Completed !")

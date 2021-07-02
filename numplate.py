import cv2
import numpy as np
import easyocr
frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
minArea = 500

cap =cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,franeHeight)
cap.set(10,150)
count = 0

while True:
    success , img  = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("images/image"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
        cap.release()
        cv2.destroyAllWindows()
        break;

image=cv2.imread('images/image0.jpg',0)
nump=np.asarray(image)
reader = easyocr.Reader(['en'])
result = reader.readtext(nump)
print(result)
import requests
import xmltodict
import json

def user_details(number, user):

	r = requests.get(f”http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={number}&username={user}")
	data = xmltodict.parse(r.content)
	jdata = json.dumps(data)
	df = json.loads(jdata)
	df1 = json.loads(df[‘Vehicle’][‘vehicleJson’])

	return [df1[“Description”],
	df1[“RegistrationYear”],
	df1[“EngineSize”][“CurrentTextValue”],
	df1[“NumberOfSeats”][“CurrentTextValue”],
	df1[“VechileIdentificationNumber”],
	df1[“EngineNumber”],
	df1[“FuelType”][“CurrentTextValue”],
	df1[“RegistrationDate”],
	df1[“Location”]]

user=”your username”
number=result[0][0][1]

user_details(number, user)



from ultralytics import YOLO
import cv2
from sort import *
import numpy as np
from util import *
import cvzone
import torch
from mongodb import *

device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

# booth = input("Enter the booth RC CODE")

coco_model = YOLO("./models/yolov8n.pt")
license_plate_detector = YOLO("./models/license_plate_detector.pt")
mot_tracker = Sort()
cap = cv2.VideoCapture("./videos/Untitled2.mp4")
# cap = cv2.VideoCapture(0)
# cap.set(2,340)
# cap.set(3,720)
frame = -1
frameresult = {}
vehicals = [2, 3, 5, 7]
# edh basic ala img frame boxes taruk mattte cvzone use madi bounding box na display madud
while True:
    frame += 1
    frameresult[frame] = {}
    status, img = cap.read()
    if not status:
        break
    if True:
        results = coco_model(img)[0]
        detections_ = []
        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = result
            if int(cls) in vehicals:
                detections_.append([x1, y1, x2, y2, conf])

        # cars na track maduke
        track_ids = mot_tracker.update(np.asarray(detections_))

        license_plates = license_plate_detector(img)[0]
        prevPlate =""
        currPlate = " "
        distance =None
        for plates in license_plates.boxes.data.tolist():
            x1, y1, x2, y2, conf, cls = plates
            # get car na number palte and car na match madukke.. x,y coridnates match madi car id sikatde
            xcar1, ycar1, xcar2, ycar2, carid = get_car(plates, track_ids)
            if carid != -1:
                cropedplate = img[int(y1):int(y2), int(x1):int(x2), :]

                # filter na apply madud to read the data
                cropedplategray = cv2.cvtColor(cropedplate, cv2.COLOR_BGR2GRAY)
                _, cropedplatetresh = cv2.threshold(cropedplategray, 64, 255, cv2.THRESH_BINARY_INV)
                # cropedplatetresh = preprocess_plate(cropedplate)
                cv2.imshow("image", cropedplatetresh)

                # cv2.imshow("0gimg",cropedplate)
                # cv2.imshow("treshimg",cropedplatetresh)

                plate_text, plate_text_conf = read_license_plate(cropedplatetresh)

                if plate_text is not None:
                    currPlate = plate_text
                    # if True:
                    # frameresult[frame][carid] = {
                    #     'car': {'bbox': [xcar1, ycar1, xcar2, ycar2]},
                    #     'license_plate': {
                    #         'bbox': [x1, y1, x2, y2],
                    #         'text': plate_text,
                    #         'bbox_score': conf,
                    #         'text_score': plate_text_conf
                    #     }
                    # }
                    if prevPlate != currPlate:
                        distance = findDist(plate_text)

                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                    xcar1, ycar1, xcar2, ycar2 = int(xcar1), int(ycar1), int(xcar2), int(ycar2)

                    cvzone.cornerRect(img, (xcar1, ycar1, xcar2 - xcar1, ycar2 - ycar1), l=15)
                    cvzone.putTextRect(img, f' {plate_text}', (max(0, x1), max(35, y1)),
                                       scale=2, thickness=3, offset=10)
                    if distance == None:
                        cvzone.putTextRect(img, 'failed to find distance ', (max(0, xcar1), max(35, ycar1)),
                                           scale=2, thickness=3, offset=10)
                    elif distance <= 20:
                        cvzone.putTextRect(img, 'Toll Exempted distance ' + str(distance), (max(0, xcar1), max(35, ycar1)),
                                           scale=2, thickness=3, offset=10)
                    else:
                        cvzone.putTextRect(img, 'Collect toll ' + str(distance), (max(0, xcar1), max(35, ycar1)),
                                           scale=2, thickness=3, offset=10)

                    cvzone.cornerRect(img, (x1, y1, x2 - x1, y2 - y1), l=15)

                    prevPlate = currPlate

                    # print(frameresult)

    img_resized = cv2.resize(img, (1280, 720))
    cv2.imshow("Image", img_resized)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# write_csv(frameresult, './test.csv')
# print('done')

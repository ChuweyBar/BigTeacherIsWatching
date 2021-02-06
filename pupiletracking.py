import time

import cv2
import numpy as np


# init part
from pygame import event

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
detector_params = cv2.SimpleBlobDetector_Params()
detector_params.filterByArea = True
detector_params.maxArea = 1500
detector = cv2.SimpleBlobDetector_create(detector_params)


def detect_faces(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    coords = cascade.detectMultiScale(gray_frame, 1.3, 5)
    if len(coords) > 1:
        biggest = (0, 0, 0, 0)
        for i in coords:
            if i[3] > biggest[3]:
                biggest = i
        biggest = np.array([i], np.int32)
    elif len(coords) == 1:
        biggest = coords
    else:
        return None
    for (x, y, w, h) in biggest:
        frame = img[y:y + h, x:x + w]
    return frame


def detect_eyes(img, cascade):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = cascade.detectMultiScale(gray_frame, 1.3, 5)  # detect eyes
    width = np.size(img, 1)  # get face frame width
    height = np.size(img, 0)  # get face frame height
    left_eye = None
    right_eye = None
    for (x, y, w, h) in eyes:
        if y > height / 2:
            pass
        eyecenter = x + w / 2  # get the eye center
        if eyecenter < width * 0.5:
            left_eye = img[y:y + h, x:x + w]
        else:
            right_eye = img[y:y + h, x:x + w]
    return left_eye, right_eye


def cut_eyebrows(img):
    height, width = img.shape[:2]
    eyebrow_h = int(height / 4)
    img = img[eyebrow_h:height, 0:width]  # cut eyebrows out (15 px)

    return img


def blob_process(img, threshold, detector):
    gray_frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(gray_frame, threshold, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, None, iterations=2)
    img = cv2.dilate(img, None, iterations=4)
    img = cv2.medianBlur(img, 5)
    keypoints = detector.detect(img)
    #print(keypoints)
    return keypoints


def nothing(x):
    pass


def main():
    cap = cv2.VideoCapture(1)
    cv2.namedWindow('image')
    cv2.createTrackbar('threshold', 'image', 0, 255, nothing)

    count = 0
    sum = 0
    msg = 0
    while True:
        _, frame = cap.read()
        face_frame = detect_faces(frame, face_cascade)
        if face_frame is not None:
            eyes = detect_eyes(face_frame, eye_cascade)
            for eye in eyes:
                if eye is not None:
                    threshold = r = cv2.getTrackbarPos('threshold', 'image')
                    eye = cut_eyebrows(eye)
                    #print(eye)
                    keypoints = blob_process(eye, threshold, detector)
                    h,w = eye.shape[:2]
                    cv2.rectangle(eye,(0,0),(h+10,w -20),(255,255,255),2)
                    eye = cv2.drawKeypoints(eye, keypoints, eye, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
                    coord_pts_x = ([keypoints[idx].pt[0] for idx in range(0, len(keypoints))])
                    coord_pts_y = ([keypoints[idx].pt[1] for idx in range(0, len(keypoints))])
                    #print(coord_pts_y)
                    """
                    if coord_pts_x != []:
                        if coord_pts_x[0] >= 26:
                            print("LOOKING LEFT")
                            cv2.putText(frame, 'LOOKING LEFT', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (200, 255, 255), 2, cv2.LINE_AA)
                        elif coord_pts_x[0] <= 26 and coord_pts_x[0] >= 20:
                            print("LOOKING STRAIGHT")
                            cv2.putText(frame, 'LOOKING STRAIGHT', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (200, 255, 255), 2, cv2.LINE_AA)
                        else:
                            print("LOOKING RIGHT")
                            cv2.putText(frame, 'LOOKING RIGHT', (50, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (200, 255, 255), 2, cv2.LINE_AA)
                    """
                    if coord_pts_x!=[]:

                        count += 1
                        sum+= coord_pts_x[0]
                        #print(coord_pts_x)
                        if count == 20:
                            avg = sum / 20
                            print(avg)
                            count = 0
                            sum = 0
                            if avg >= 30 or avg <= 24:
                                cv2.putText(frame, 'Not Paying Attention', (50, 75), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2,
                                            (255, 255, 255), 2, cv2.LINE_AA)
                            #if msg > 0:

                        #if coord_pts_x[0] >= 30 or coord_pts_x[0] <= 19:
                        #    print("Not looking straight")
                        #    cv2.putText(frame, 'Pay Attention', (50,75), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        cv2.imshow('image', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
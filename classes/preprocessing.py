import cv2

import numpy as np

capture = cv2.VideoCapture('C:\\Users\\Magda\\Downloads\\box.MP4')
video_output = cv2.VideoWriter('C:\\Users\\Magda\\Downloads\\box.MP4',
                               cv2.VideoWriter_fourcc(*'mp4v'),
                               10,
                               (640, 480))
frameNr = 0

while True:
    success, frame = capture.read(0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    light_blue = np.array([110, 50, 50])
    dark_blue = np.array([130, 255, 255])
    mask = cv2.inRange(hsv, light_blue, dark_blue)
    output = cv2.bitwise_and(frame, frame, mask=mask)
    video_output.write(output)
    cv2.imshow('output', output)
    if cv2.waitKey(1) & 0xFF == ord('Q'):
        break

    # if success:
    #     # cv2.imwrite(f"C:\\Users\\Magda\\Downloads\\pythonBox\\frame_{frameNr}.jpg", frame)
    # else:
    #     break

    frameNr += 1

# capture.release()
video_output.release()
cv2.destroyAllWindows()
print("The video was successfully saved")


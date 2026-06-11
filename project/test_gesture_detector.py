import cv2

from hand_tracker import HandTracker
from gesture_detector import GestureDetector

tracker = HandTracker(
    #"../models/hand_landmarker.task"
    r"C:\Users\DELL\Desktop\VirtualMouseProject\models\hand_landmarker.task"
)

detector = GestureDetector()

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    result = tracker.detect(frame)

    if result.hand_landmarks:

        hand_landmarks = result.hand_landmarks[0]

        if detector.detect_click(hand_landmarks):

            cv2.putText(
                frame,
                "CLICK",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

    cv2.imshow(
        "Gesture Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
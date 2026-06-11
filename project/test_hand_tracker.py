import cv2
from hand_tracker import HandTracker

# Load model
tracker = HandTracker(
    #"../models/hand_landmarker.task"
    r"C:\Users\DELL\Desktop\VirtualMouseProject\models\hand_landmarker.task"
)

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    result = tracker.detect(frame)

    h, w, _ = frame.shape

    if result.hand_landmarks:

        for hand_landmarks in result.hand_landmarks:

            for landmark in hand_landmarks:

                x = int(landmark.x * w)
                y = int(landmark.y * h)

                cv2.circle(
                    frame,
                    (x, y),
                    5,
                    (0, 255, 0),
                    -1
                )

    cv2.imshow(
        "Hand Tracking",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
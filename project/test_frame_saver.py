import cv2
from frame_saver import FrameSaver

cap = cv2.VideoCapture(0)

saver = FrameSaver(
    save_interval=10
)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(
        frame,
        1
    )

    saver.save_frame(
        frame
    )

    cv2.imshow(
        "Frame Saver",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()

cv2.destroyAllWindows()
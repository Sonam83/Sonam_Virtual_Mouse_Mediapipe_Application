import cv2
from frame_processor import FrameProcessor

processor = FrameProcessor()

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = processor.resize_frame(frame)

    frame = processor.flip_frame(frame)

    frame = processor.blur_frame(frame)

    cv2.imshow(
        "Frame Processor",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
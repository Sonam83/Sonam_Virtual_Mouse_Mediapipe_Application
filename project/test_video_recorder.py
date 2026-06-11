import cv2

from video_recorder import VideoRecorder

cap = cv2.VideoCapture(0)

width = int(cap.get(3))
height = int(cap.get(4))

recorder = VideoRecorder(
    "saved_videos/output.mp4",
    width,
    height
)

while True:

    success, frame = cap.read()

    if not success:
        break

    recorder.write_frame(frame)

    cv2.imshow(
        "Video Recorder Test",
        frame
    )

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()

recorder.release()

cv2.destroyAllWindows()
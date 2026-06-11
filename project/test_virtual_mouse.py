import cv2

from hand_tracker import HandTracker
from virtual_mouse import VirtualMouse
from gesture_detector import GestureDetector


tracker = HandTracker(
    r"C:\Users\DELL\Desktop\VirtualMouseProject\models\hand_landmarker.task"
)

mouse = VirtualMouse()

detector = GestureDetector()

dragging = False

cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    h, w, _ = frame.shape

    result = tracker.detect(frame)

    if result.hand_landmarks:

        hand_landmarks = result.hand_landmarks[0]

        # Index finger tip
        index_tip = hand_landmarks[8]

        # Convert to screen coordinates
        screen_x = int(index_tip.x * mouse.screen_width)
        screen_y = int(index_tip.y * mouse.screen_height)

        # Move cursor
        mouse.move_cursor(screen_x, screen_y)

        # Draw cursor point
        x = int(index_tip.x * w)
        y = int(index_tip.y * h)

        cv2.circle(
            frame,
            (x, y),
            10,
            (0, 255, 0),
            -1
        )

        ##################################
        # LEFT CLICK
        ##################################
        if detector.detect_click(hand_landmarks):

            mouse.left_click()

            cv2.putText(
                frame,
                "LEFT CLICK",
                (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

        ##################################
        # RIGHT CLICK
        ##################################
        elif detector.detect_right_click(hand_landmarks):

            mouse.right_click()

            cv2.putText(
                frame,
                "RIGHT CLICK",
                (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (255, 0, 0),
                2
            )

        ##################################
        # DRAG
        ##################################
        elif detector.detect_drag(hand_landmarks):

            if not dragging:

                mouse.drag_start()

                dragging = True

            cv2.putText(
                frame,
                "DRAGGING",
                (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2
            )

        else:

            if dragging:

                mouse.drag_stop()

                dragging = False

    cv2.imshow(
        "Virtual Mouse",
        frame
    )

    if cv2.waitKey(10) & 0xFF == 27:
        break

cap.release()

cv2.destroyAllWindows()
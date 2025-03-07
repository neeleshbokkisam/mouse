import cv2
import pyautogui
from camera.stream import start_camera
from tracking.hands import HandTracker
from tracking.landmarks import LandmarkProcessor
from gestures.detect import GestureDetector
from control.actions import MouseController

# Initialize components
screen_width, screen_height = pyautogui.size()
tracker = HandTracker()
processor = LandmarkProcessor(screen_width, screen_height)
detector = GestureDetector()
controller = MouseController(screen_width, screen_height)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Detect hands and landmarks
    frame, hand_landmarks = tracker.detect_hands(frame)
    
    if hand_landmarks:
        landmarks = processor.extract_landmarks(hand_landmarks[0])  # Only handling one hand
        fingers = processor.get_finger_positions(landmarks)
        
        if fingers["index_tip"]:
            controller.move_cursor(fingers["index_tip"])
        
        if detector.detect_click(fingers["index_tip"], fingers["thumb_tip"]):
            controller.click()
        
        if detector.detect_drag(fingers["index_tip"], fingers["thumb_tip"], prev_distance=None):
            controller.drag(fingers["index_tip"])
    
    cv2.imshow("Mouse Control", frame)
    
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

cap.release()
cv2.destroyAllWindows()
tracker.close()
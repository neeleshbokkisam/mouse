import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        """
        Initializes the MediaPipe Hand tracking model.
        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=max_hands,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence
        )
        self.mp_draw = mp.solutions.drawing_utils

    def detect_hands(self, frame):
        """
        Detects hands and returns landmark positions.
        """
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb_frame)
        hand_landmarks = []

        if results.multi_hand_landmarks:
            for hand_landmark in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(frame, hand_landmark, self.mp_hands.HAND_CONNECTIONS)
                hand_landmarks.append(hand_landmark)

        return frame, hand_landmarks

    def close(self):
        self.hands.close()

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    tracker = HandTracker()
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        frame, landmarks = tracker.detect_hands(frame)
        cv2.imshow("Hand Tracking", frame)
        
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
            break
    
    cap.release()
    cv2.destroyAllWindows()
    tracker.close()

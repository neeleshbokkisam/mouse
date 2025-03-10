class GestureDetector:
    def __init__(self, click_threshold=40, drag_threshold=50):
        """
        Initializes the gesture detector with distance thresholds.
        """
        self.click_threshold = click_threshold
        self.drag_threshold = drag_threshold

    def detect_click(self, middle_tip, thumb_tip):
        """
        Detects a click gesture when the middle finger tip and thumb tip are close.
        """
        if middle_tip is None or thumb_tip is None:
            return False
        
        distance = ((middle_tip[0] - thumb_tip[0]) ** 2 + (middle_tip[1] - thumb_tip[1]) ** 2) ** 0.5
        return distance < self.click_threshold

    def detect_drag(self, middle_tip, thumb_tip, prev_distance):
        """
        Detects a drag gesture when the thumb and middle finger pinch and maintain a small distance.
        """
        if middle_tip is None or thumb_tip is None:
            return False

        distance = ((middle_tip[0] - thumb_tip[0]) ** 2 + (middle_tip[1] - thumb_tip[1]) ** 2) ** 0.5
        return distance < self.drag_threshold and prev_distance is not None and distance < prev_distance

if __name__ == "__main__":
    detector = GestureDetector()
    
    # Example test
    middle_tip = (300, 400)
    thumb_tip = (310, 410)
    print("Click detected:", detector.detect_click(middle_tip, thumb_tip))

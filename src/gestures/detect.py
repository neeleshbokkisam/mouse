class GestureDetector:
    def __init__(self, click_threshold=40, drag_threshold=50):
        """
        Initializes the gesture detector with distance thresholds.
        """
        self.click_threshold = click_threshold
        self.drag_threshold = drag_threshold

    def detect_click(self, index_tip, thumb_tip):
        """
        Detects a click gesture when the index and thumb fingertips are close.
        """
        if index_tip is None or thumb_tip is None:
            return False
        
        distance = ((index_tip[0] - thumb_tip[0]) ** 2 + (index_tip[1] - thumb_tip[1]) ** 2) ** 0.5
        return distance < self.click_threshold

    def detect_drag(self, index_tip, thumb_tip, prev_distance):
        """
        Detects a drag gesture when the thumb and index pinch and maintain a small distance.
        """
        if index_tip is None or thumb_tip is None:
            return False

        distance = ((index_tip[0] - thumb_tip[0]) ** 2 + (index_tip[1] - thumb_tip[1]) ** 2) ** 0.5
        return distance < self.drag_threshold and prev_distance is not None and distance < prev_distance

if __name__ == "__main__":
    detector = GestureDetector()
    
    # Example test
    index_tip = (300, 400)
    thumb_tip = (310, 410)
    print("Click detected:", detector.detect_click(index_tip, thumb_tip))

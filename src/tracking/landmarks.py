import numpy as np
import cv2
from mediapipe.framework.formats.landmark_pb2 import NormalizedLandmarkList

class LandmarkProcessor:
    def __init__(self, frame_width, frame_height):
        """
        Initializes the landmark processor with the frame dimensions.
        """
        self.frame_width = frame_width
        self.frame_height = frame_height
    
    def extract_landmarks(self, hand_landmarks: NormalizedLandmarkList):
        """
        Extracts and converts key hand landmarks from normalized coordinates to pixel coordinates.
        """
        landmarks = {}
        if hand_landmarks:
            for idx, landmark in enumerate(hand_landmarks.landmark):
                pixel_x = int(landmark.x * self.frame_width)
                pixel_y = int(landmark.y * self.frame_height)
                landmarks[idx] = (pixel_x, pixel_y)
        
        return landmarks

    def get_finger_positions(self, landmarks):
        """
        Returns the coordinates of key finger landmarks.
        """
        if not landmarks:
            return None
        
        return {
            "index_tip": landmarks.get(8),
            "thumb_tip": landmarks.get(4),
            "middle_tip": landmarks.get(12),
            "ring_tip": landmarks.get(16),
            "pinky_tip": landmarks.get(20)
        }

    def calculate_distance(self, point1, point2):
        """
        Calculates the Euclidean distance between two points.
        """
        if point1 is None or point2 is None:
            return None
        return np.linalg.norm(np.array(point1) - np.array(point2))

if __name__ == "__main__":
    # Test with dummy values
    processor = LandmarkProcessor(frame_width=640, frame_height=480)
    dummy_landmarks = {4: (100, 200), 8: (300, 400)}
    distance = processor.calculate_distance(dummy_landmarks[4], dummy_landmarks[8])
    print("Distance between thumb and index finger:", distance)

import cv2

def start_camera():
    """
    Initializes the webcam and displays the video feed.
    Press 'ESC' to exit.
    """
    cap = cv2.VideoCapture(0)  # Open default camera
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        cv2.imshow("Mouse - Camera Stream", frame)  # Display video feed

        # Press ESC to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_camera()

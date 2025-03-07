import pyautogui
import numpy as np

class MouseController:
    def __init__(self, screen_width, screen_height, smooth_factor=5):
        """
        Initializes the mouse controller with screen dimensions and smoothing factor.
        """
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.smooth_factor = smooth_factor
        self.prev_x, self.prev_y = 0, 0

    def move_cursor(self, index_tip):
        """
        Moves the cursor based on the index finger's position.
        """
        if index_tip is None:
            return
        
        x = np.interp(index_tip[0], [0, self.screen_width], [0, self.screen_width])
        y = np.interp(index_tip[1], [0, self.screen_height], [0, self.screen_height])
        
        # Apply smoothing
        smoothed_x = self.prev_x + (x - self.prev_x) / self.smooth_factor
        smoothed_y = self.prev_y + (y - self.prev_y) / self.smooth_factor
        
        pyautogui.moveTo(smoothed_x, smoothed_y)
        self.prev_x, self.prev_y = smoothed_x, smoothed_y

    def click(self):
        """
        Simulates a mouse left-click.
        """
        pyautogui.click()
    
    def drag(self, index_tip):
        """
        Simulates a drag motion while moving the cursor.
        """
        if index_tip is None:
            return
        
        pyautogui.mouseDown()
        self.move_cursor(index_tip)
        pyautogui.mouseUp()

if __name__ == "__main__":
    screen_width, screen_height = pyautogui.size()
    controller = MouseController(screen_width, screen_height)
    
    # Example test values
    index_tip = (300, 400)
    controller.move_cursor(index_tip)
    controller.click()

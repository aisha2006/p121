# Import the cv2 and numpy libraries.
import cv2
# Start the video capture.
# Read the image which will be shown when the black object will get masked and save it in an “image” variable.
# Start reading the frames of the video.
# Resize the image and the video to 640, 480.
# Create an array of RGB of faint black color shade and dark shade of black and store in the l_black and u_black respectively.
# Create a mask using cv’s inRange() function and pass the frame , l_black and u_black as the parameters.
# Using np.where() function to return frame or image if the value of f is 0.
# Show the real video and masked video.
# Break the loop if the user presses “Esc” or “Q”.
# Release the video and close the video windows.
# Run and test the code.

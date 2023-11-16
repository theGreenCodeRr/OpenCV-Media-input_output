import cv2, numpy as np, matplotlib.pyplot as plt

# for img I/O                   
img = cv2.imread("img/Parrots.bmp")             # Load image into img
img.shape                                       # Height x Width x Color
cv2.imshow("Color", img)                        # Output an Image
img_gray=cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow("Grayscale", img_gray)               # Grayscale conversion
cv2.waitKey(500)                               # Wait for key input
cv2.destroyAllWindows()             
cv2.imwrite("output.jpg", img)                  # Save an image

#window size
cv2.namedWindow("window_resize", cv2.WINDOW_NORMAL)  # Create a window
cv2.resizeWindow("window_resize", 1280, 720)           # Resize a window
cv2.imshow("window_resize", img)                         # Output an Image
cv2.waitKey(500)                                # Wait for key input
cv2.destroyAllWindows()

# for video reading
cap = cv2.VideoCapture("video/Parrots.mp4")  # Load video into cap

while(cap.isOpened()):                       # Check if cap is opened
    ret, frame = cap.read()                  # Read frame from cap
    if ret == True:                          # Check if frame is read
        cv2.imshow("Video", frame)           # Output a frame
    if cv2.waitKey(30) == 27:                # Wait for key input
        break
    else:
        break
cap.release()                               # Release cap
cv2.destroyAllWindows()                     # Destroy all windows

# for video writing
cap = cv2.VideoCapture("video/Parrots.mp4")  # Load video into cap
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')     # Define codec
out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480)) # Define output

while(cap.isOpened()):                       # Check if cap is opened
    ret, frame = cap.read()                  # Read frame from cap
    if ret == True:                          # Check if frame is read
        out.write(frame)                     # Write frame to output
        cv2.imshow("Video", frame)           # Output a frame
        if cv2.waitKey(30) == 27:            # Wait for key input
            break
    else:
        break
cap.release()                               # Release cap
out.release()                               # Release output
cv2.destroyAllWindows()                     # Destroy all windows
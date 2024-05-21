import cv2

# Initialize the USB camera (usually the first camera is at 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('frame', frame)
        
        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
finally:
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
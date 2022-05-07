import cv2


vid_path ='../resources/videos/video_1.mp4'
save_path = '../resources/videos/video_test.mp4'
save_vid = True

# Create video capture instance using cv2.VideoCapture()
###
vid_cap = cv2.VideoCapture(0)
###
#Get needed video info if we are going to record video
if save_vid:
    fps = vid_cap.get(cv2.CAP_PROP_FPS)
    
    w = int(vid_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(vid_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(w)
    print(h)
    #w,  h = 1280, 720
    #Create video writer instance
    vid_writer = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'mp4v'), int(fps), (w, h))

while(vid_cap.isOpened()):
    # Capture frame-by-frame
    ret, frame = vid_cap.read()
    # Display video 
    if ret:
        print(frame.shape)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Show frame using cv2.imshow()
        ###
        cv2.imshow("Image", frame)
        cv2.imshow("Gray", img_gray)
        ###
        # Close window when you press q
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
        
        # Record if save_vid == True using .write() method
        ###
        img_gray = cv2.cvtColor(img_gray,cv2.COLOR_GRAY2BGR)
        if save_vid==True: 
            vid_writer.write(img_gray)
        ###
    else:
        break

if save_vid: vid_writer.release()
# When everything done, release the video capture object
vid_cap.release()
# Closes all the frames
cv2.destroyAllWindows()
    
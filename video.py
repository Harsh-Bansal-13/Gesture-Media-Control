# # import cv2

# # video_reader=cv2.VideoCapture(0) 
# # while True:
# #     success,frame=video_reader.read()
# #     if not success:
# #         break
# #     cv2.imshow("My Video",frame)
# #     key=cv2.waitKey(1)
# #     if key==ord('q'):
# #         break
# # video_reader.release()
# # cv2.destroyAllWindows()



# import cv2
# vid = cv2.VideoCapture(0);
# while(1):
#     _,frame = vid.read()
#     frame = cv2.flip(frame,1) # resolving mirror image issues
#     # For eye detection
#     fullScreenFrame=frame
    
#     frame = frame[190:, 500:]
#     # print(frame.shape)
#     cv2.imshow('video',frame)
#     key=cv2.waitKey(1)
#     if key==ord('q'):
#         break
# vid.release()
# cv2.destroyAllWindows()



# # (480, 640, 3)
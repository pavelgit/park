import cv2
import numpy as np
import youtube_dl

if __name__ == '__main__':

    video_url = 'https://www.youtube.com/watch?v=NM9HE2-I5E8'

    ydl_opts = {}

    # create youtube-dl object
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    # set video url, extract video information
    info_dict = ydl.extract_info(video_url, download=False)

    # get video formats available
    formats = info_dict.get('formats',None)

    #get the video url
    url = formats[1].get('url',None)

    # open url with opencv
    cap = cv2.VideoCapture(url)

    # check if url was opened
    if not cap.isOpened():
        print('video not opened')
        exit(-1)

    i = 0
    while True:
        # read frame
        ret, frame = cap.read()

        # check if frame is empty
        if not ret:
            break

        # display frame
        cv2.imshow('frame', frame)

        i += 1
        print(i)

        if cv2.waitKey(1000)&0xFF == ord('q'):
            break

    # release VideoCapture
    cap.release()

    cv2.destroyAllWindows()
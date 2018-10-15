import numpy as np
import cv2 as cv

fgbg = cv.createBackgroundSubtractorMOG2()
fgbg.setHistory(5000)

#fgbg.setBackgroundRatio(0.1)
#fgbg.setVarThresholdGen(100)
#fgbg.setShadowThreshold(0.9)

print('history ', fgbg.getHistory())
print('getNMixtures ', fgbg.getNMixtures())
print('getBackgroundRatio ', fgbg.getBackgroundRatio())
print('getVarThreshold ', fgbg.getVarThreshold())
print('getVarThresholdGen ', fgbg.getVarThresholdGen())
print('getVarInit ', fgbg.getVarInit())
print('getComplexityReductionThreshold ', fgbg.getComplexityReductionThreshold())
print('getShadowValue ', fgbg.getShadowValue())
print('getShadowThreshold ', fgbg.getShadowThreshold())


cap = cv.VideoCapture('orangeville.mp4')

resize_factor = 0.25
original_size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)))
resized_size = (int(cap.get(cv.CAP_PROP_FRAME_WIDTH) * resize_factor), int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) * resize_factor))

f = 0
while (True):
    cap.set(1, f*10)
    ret,frame = cap.read()  
    if ret is None:
        break

    resizedFrame = cv.resize(frame, resized_size)

    fgmask = fgbg.apply(resizedFrame)
    
    f += 1
    if f%100 == 0:
        bg = fgbg.getBackgroundImage()
        cv.imshow('frame', cv.resize(resizedFrame, original_size))
        cv.imshow('bg', cv.resize(bg, original_size))
        cv.waitKey(25)
        print(f)

input("Press Enter to continue...")

cap.release()
cv.destroyAllWindows()
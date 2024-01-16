# !/usr/bin/python2
# -*- coding: utf-8 -*-

'''
This script uses OpenCV 2.3.1 or greater to examine a webcam image for white dice with black pips being thrown into a brown box.
www.hehoe.de
'''

import cv2
import sys

HAVE_DISPLAY = True

BINARIZATION_THRESHOLD = 45 # Selects the bright white die area

# Area size definitions (the script "knows" how big a die should be)
AREA_FACTOR = 1.0 # compensate camera zoom or position
DIE_AREA_MIN = AREA_FACTOR * 900
DIE_AREA_MAX = AREA_FACTOR * 1500
PIP_AREA_MIN = AREA_FACTOR * 6
PIP_AREA_MAX = AREA_FACTOR * 45

if HAVE_DISPLAY:
    def set_factors(user):
        global BINARIZATION_THRESHOLD, AREA_FACTOR, DIE_AREA_MIN, DIE_AREA_MAX, PIP_AREA_MIN, PIP_AREA_MAX
        BINARIZATION_THRESHOLD = cv2.getTrackbarPos('THRESH','control')
        AREA_FACTOR = float(cv2.getTrackbarPos('SIZE','control'))/10.0
        DIE_AREA_MIN = AREA_FACTOR * cv2.getTrackbarPos('DIE_MIN','control')
        DIE_AREA_MAX = AREA_FACTOR * cv2.getTrackbarPos('DIE_MAX','control')
        PIP_AREA_MIN = AREA_FACTOR * cv2.getTrackbarPos('PIP_MIN','control')
        PIP_AREA_MAX = AREA_FACTOR * cv2.getTrackbarPos('PIP_MAX','control')

#img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('control')
cv2.createTrackbar('THRESH','control',BINARIZATION_THRESHOLD,255,set_factors)
cv2.createTrackbar('SIZE','control',int(AREA_FACTOR*10),50,set_factors)
cv2.createTrackbar('DIE_MIN','control',int(DIE_AREA_MIN/AREA_FACTOR),1000,set_factors)
cv2.createTrackbar('DIE_MAX','control',int(DIE_AREA_MAX/AREA_FACTOR),2000,set_factors)
cv2.createTrackbar('PIP_MIN','control',int(PIP_AREA_MIN/AREA_FACTOR),10,set_factors)
cv2.createTrackbar('PIP_MAX','control',int(PIP_AREA_MAX/AREA_FACTOR),100,set_factors)

vc = cv2.VideoCapture('./vid/short-sample2.mp4')
# vc = cv2.VideoCapture() # prepare webcam for input
vc.open(0) # open webcam
if not vc.isOpened():
  print ("Could not open camera.")
  sys.exit(1)
else:
  # high resolutions via USB do not work on the raspberry pi
  # see http://www.raspberrypi.org/phpBB3/viewtopic.php?f=37&t=11745&p=135060#p135060

  # picam, debian
  # to use the picam with OpenCV via v4l2, you need to load the bcm2835-v4l2 kernel module first
  # sudo modprobe bcm2835-v4l2
  #vc.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,720)
  #vc.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,1280)
#   vc.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH,640)
#   vc.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,1024)
#   vc.set(cv2.cv.CV_CAP_PROP_FPS,10)
  vc.set(cv2.CAP_PROP_FPS, 10)
#   vc.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS,0.5)

  # tweak record properties for different lighting
  # the semantics of these commands are dependant on opencv version, os and camera driver.
  # sometimes the values are float, sometimes integer.

  # atom, windows
  #vc.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS,0.5)
  #vc.set(cv2.cv.CV_CAP_PROP_CONTRAST,0.125)

  # pi, debian
  #vc.set(cv2.cv.CV_CAP_PROP_BRIGHTNESS,0.6)
  #vc.set(cv2.cv.CV_CAP_PROP_CONTRAST,0.130)
  #vc.set(cv2.cv.CV_CAP_PROP_SATURATION,0.130)
  #vc.set(cv2.cv.CV_CAP_PROP_GAIN,0.08)
  
  # save output to avi file
  #fps = 10
  #fourcc = -1 # show dialog
  #fourcc = cv2.cv.CV_FOURCC('D','I','B',' ') # use uncompressed
  #writer = cv2.VideoWriter('out.avi', fourcc, fps, (870, 600), 1)
  #if not writer.isOpened():
  #  print "video writer fail"
  #  sys.exit(2)
    
  dilateKernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(2,2))
  while True:
    retval, image = vc.read() # read frame from camera
    if not retval:
      print ("Could not read frame from camera.")
      sys.exit(1)
    else:
      #pass
      #cv2.imshow('input', image)
      #image = image[60:-60,40:-50] # crop picture (t,b,l,r)
      #image = image[70:-95,75:-70] # crop picture
      #width = image.shape[1] 
      #height = image.shape[0]
      #print width,height
#    def detectDice(image):
      gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) # convert to grayscale
      retval, bin = cv2.threshold(gray, BINARIZATION_THRESHOLD, 255, cv2.THRESH_BINARY) # select white die areas
      bin = cv2.dilate(bin,dilateKernel) # dilate white areas to prevent pip fraying
      if HAVE_DISPLAY:
        cv2.imshow('binary', bin)
      contours0, hierarchy = cv2.findContours( bin.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # find contours
      #contours0, hierarchy = ([],[])
      
      contours = [cv2.approxPolyDP(cnt, 2, True) for cnt in contours0] # simplify contours
      #rgbbin = cv2.cvtColor(bin, cv2.COLOR_GRAY2RGB)
      #cv2.drawContours( rgbbin, contours, -1, (64,128,64), 2 )
      #cv2.imshow('All Contours', rgbbin)

      # for all contours: check white area size (die), check area size of sub-contours (pips)
      dice = []
      for i in range(len(contours)):
        dieCnt = contours[i]
        dieArea = cv2.contourArea(dieCnt)
        if dieArea > DIE_AREA_MIN and dieArea < DIE_AREA_MAX:
          #print "Contour", i, "is a die with area", dieArea
          pipId = hierarchy[0][i][2]
          pipContours = []
          while not pipId == -1:
            pipCnt = contours[pipId]
            pipArea = cv2.contourArea(pipCnt)
            if pipArea > PIP_AREA_MIN and pipArea < PIP_AREA_MAX:
              #print "Contour", i, "is a pip with area", pipArea
              pipContours.append(pipCnt)
            #else:
              #print "Pip",pipId,"with area",pipArea,"discarded"
            pipId = hierarchy[0][pipId][0]
          dice.append( (dieCnt, pipContours) )
#        elif (dieArea > 1):
#          sys.stderr.write("Contour %04d with area %05d discarded (outside of (%d,%d)).\n"%(i, dieArea, DIE_AREA_MIN, DIE_AREA_MAX))
#      return dice

      sum = 0
    for i in range(len(dice)):
        dieCnt, pipContours = dice[i]
        sum = sum + len(pipContours)

    if HAVE_DISPLAY:
        for i in range(len(dice)):
            dieCnt, pipContours = dice[i]
            cv2.drawContours( image, [dieCnt], -1, (64,64,128), 2 )
            cv2.drawContours( image, pipContours, -1, (64,128,64), 2 )
            cv2.putText(image, "%d"%len(pipContours), (dieCnt[0][0][0],dieCnt[0][0][1]), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 64, 64), 2)
        cv2.putText(image, "%d"%(sum if sum is not None else 0), (10,50), cv2.FONT_HERSHEY_PLAIN, 3.0, (255, 255, 255), 2)
        cv2.imshow('Die and Pips', image)

    print ("%s " % ("%d" % (sum if sum is not None else 0)).rjust(3))
    sys.stdout.flush()

      #small = cv2.resize(image, None, fx=0.5, fy=0.5, cv2.INTER_NEAREST ) 
      
    if HAVE_DISPLAY:
        ch = cv2.waitKey(5)
        if ch > -1:
            sys.stderr.write("Got key %d.\n"%(ch))
        if ch == 115: # save images on s
            cv2.imwrite('bin.png',bin)
            cv2.imwrite('marked.png',image)
            sys.stderr.write("Wrote images to files.\n")
        #writer.write(image)
        if ch == 27: # exit on Esc
            print ("")
            break

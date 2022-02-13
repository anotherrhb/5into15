#!/usr/bin/env python3
import sys
from datetime import datetime
from twython import Twython #https://twython.readthedocs.io/en/latest/index.html#
from subprocess import call
from time import sleep
from picamera import PiCamera #note enable legacy camera if using bullseye os https://projects.raspberrypi.org/en/projects/camera-bullseye

import time
import picamera
import shutil
import os

from gpiozero import CPUTemperature

#prompt and confirmation

location = input("Input location: ") #if you remove this you'll need to remove it from the tweetStr text later on
cpu = CPUTemperature()
temp = cpu.temperature
print ("CPU Temp =", temp)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print ("Current Time =", current_time)
print ("Tweeting from", location)

# capturing the images

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)
   #next line can be used to flip the camera e.g. set camera.rotation = 180 if videos are upside down. I keep 2 copies of the code so I can run a flip version quickly.
   #camera.rotation = 0
    camera.start_preview()
    time.sleep(1)
    for i, filename in enumerate(camera.capture_continuous('image{counter:04d}.jpg')):
       # next line can be used to print confirmation for each image captured just remove comment hash
       # print('Captured image %s' % filename) 
        if i == 300: #total number images to capture
            break
        time.sleep(1) #delay between images in s
    camera.stop_preview()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print ("Images Capture complete at", current_time)

#create timelapse - this format is twitter friendly. not all were iirc.
cmd3 = 'ffmpeg -r 20 -loglevel error -i image%04d.jpg -r 20 -vcodec libx264 -vf scale=1280:720 -crf 17 5into15.mp4'

call ([cmd3], shell=True) #process timelapse

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print ("Timelapse in mp4 format complete at", current_time)

# twitter magic here - explained via google over a few pages, e.g. https://www.instructables.com/Raspberry-Pi-Twitterbot/:

# set the standard tweet text - it can be simpler than this if you're not adding any variables/prompts

starttweet = "Take 15 seconds of your day to enjoy 5 minutes from #" 
endtweet = ", UK. A #timelapse #project using a @raspberry_pi Zero2 and the @twitter api." 

tweetStr = starttweet + location + endtweet

# your twitter consumer and access information goes here
# note: these were garbage strings and didn't work until I added them from the apps.twitter.com info
apiKey = 'yourapiKeyhere'
apiSecret = 'yourapiSecrethere'
accessToken = 'youraccessTokenhere'
accessTokenSecret = 'youraccessTokenSecrethere'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

#old pi zero convert to h264 step - not needed for more powerful pi like 3, zero2, or 4
#cmd4 = 'ffmpeg -loglevel error -i 5into15mpeg4.mp4 -an -c:v libx264 -crf 17 5into15.mp4' #you'd need alter these filenames throughout accordingly.
#call ([cmd4], shell=True)
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")
#print ("h264 conversion complete at", current_time)

#send tweet with video

video = open('5into15.mp4', 'rb')
response = api.upload_video(media=video, media_type='video/mp4')
time.sleep(5.5)    # Pause 5.5 seconds
#confirmation it has made it to twitter - note: if twitter doesn't like the video here it'll throw out an error message. Your images and timelapse are saved so can this can be redone at a later date if required.
print('media_id', response['media_id'])
api.update_status(status=tweetStr, media_ids=[response['media_id']])

#confirm sent

print ("Tweeted: " + tweetStr)

#clear up image files for next time

cmd5 = 'rm im*.jpg'
call ([cmd5], shell=True) #delete the image files
print ("Source Image files Deleted")

#save archive copy of video date and time stamped

os.rename("5into15.mp4", time.strftime("%Y%m%d%H%M%S.mp4"))

print ("copy of video saved")

#confirm end stats

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print ("Finish Time =", current_time)

cpu = CPUTemperature()
temp = cpu.temperature
print ("CPU Temp =", temp)

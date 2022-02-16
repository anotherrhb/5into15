# 5into15 Intro
Raspberry Pi Timelapse to Twitter

Can be found at @5into15 on twitter. https://twitter.com/5into15

<img src="https://user-images.githubusercontent.com/99504166/153779085-ae81b9fd-8430-4060-80c7-e43bd4c171ad.jpg" width=25% height=25%> <img src="https://user-images.githubusercontent.com/99504166/153779589-3ab95c6e-386c-44c8-8270-993845d1ba98.jpg" width=25% height=25%>

A small project I worked on during lockdown to make and tweet a short timelapse film using a Raspberry Pi (Zero, then 3b+, now Zero2) and Zerocam Fisheye, all controlled from my mobile phone. I use JuiceSSH on Android for this. The pi is powered using an Anker Powercore Mini. 

I've uploaded a dummy version of the script for folks to use tweak for other purposes and to offer improvements upon.

Disclaimer: I know very little about computers and programming, this was mostly researched via google with some additional input from users on a Pi discussion thread on London's friendliest cycling forum. 

My motivation was to prompt me to take time to stop and enjoy my surroundings as well as to capture moments of movement that may otherwise go unnoticed. I've found good subjects are crowded spaces, public transport, clouds, and water / waves / wildlife.

The output works best on small screens as the resolution isn't great. The Zerocam Fisheye is a pain to focus when running headless, so there's a roughness to the videos that I live with. 

Future upgrade might be the RPI HQ camera module, this would be bulkier but better quality output - might need a pi4 to process it. A waterproof case would be useful too.

# How it works

On the assumption the Pi is already setup with Twython installed (https://twython.readthedocs.io/en/latest/index.html#) and camera & ssh enabled, there're essentially 5 steps to this which I researched and tested in part then put together into a single script:

1) Trigger a .py which firstly prompts for location input for use in the tweet later. 
2) Capture 300 images at 1 per second in .jpg format, using picamera. This is actually slightly slower than 5x60=300s, it usually takes about 7 minutes to complete this.
3) Convert this into a timelapse movie at 20fps via ffmpeg, using -vcodec libx264 and -vf scale=1280:720 to output an .mp4 file. This takes about 2 minutes.
4) Upload to twitter using the twitter api and twython - this was fairly straightforward to get going after I'd looked it up, there're a few instructables etc about it. This step within the script takes about a minute to complete.
5) Clean up the image files, and archive the video file so that both a copy is kept and that the working files can be created again without an overwrite prompt.

That's it really. There're some checks and balances along the way to confirm time of each stage. It was impossibly slow to process the movie on the Zero, but a matter of minutes on the 3 gifted by  and Zero2. It also confirms temperature just out of interest. I was sent a code snippet to add to collect the mediaID of the twitter upload once successful which I also included.

![juicessh](https://user-images.githubusercontent.com/99504166/153779762-a1e13fd0-bc3c-4d49-b648-1a4c8bbe9084.jpg)

# Note

The script occasionally fails to tweet. I think this is due to using mobile hotspot, but can't prove this. Often connecting to the home wifi later and running it again will be enough to push it out to twitter but once in a while even this isn't enough. In these cases if I copy the .jpg files to a new directory then remake the timelapse this is usually enough for it to tweet later on.

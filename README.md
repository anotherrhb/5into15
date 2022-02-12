# 5into15
Raspberry Pi Timelapse to Twitter

Found at @5into15 on twitter.

A small project I worked on during lockdown to make and tweet a short timelapse film using a Raspberry Pi (Zero, then 3b+, now Zero2) and Zerocam Fisheye, all controlled from my mobile phone by ssh. I use JuiceSSH on Android for this.

My motivation was to prompt me to take time to stop and enjoy my surroundings as well as to capture moments of movement that may otherwise go unnoticed. Good subjects are crowded spaces, public transport, clouds, and water / waves.

Disclaimer: I know very little about computers and programming, this was mostly researched via google with some additional input from users on a Pi discussion thread on London's friendliest cycling forum. 

On the assumption the Pi is already setup and camera & ssh enabled, there're essentially 5 steps to this which I researched and tested in part then put together into a single script:

1) Trigger a .py which firstly prompts for location input for use later. Orginally this was just set as Manchester within the script but this meant editing it on the fly if I went elsewhere. Prompt makes it easier to ensure the location is correct (I was forgetting to update it within the code at times).
2) Capture 300 images at 1 per second. This is actually slightly slower than 5x60=300s it usually takes about 7 minutes to complete this.
3) Convert this into a timelapse movie at 12fps, making this a format that twitter will be happy to receive. This takes about 2 minutes.
4) Upload to twitter using the twitter api and twython - this is all a bit out of my comfort zone now 12 motnhs has passed as I've not had to revisit it since. It was fairly straightforward to get going after I'd looked it up. This takes about a minute.
5) Clean up the image files, and archive the video file so that both a copy is kept and that the working file can be created again without an overwrite prompt.

That's it really. There's some checks and balances along the way to confirm time (it was impossibly slow on the Zero, but a matter of minutes on the 3 and Zero2) plus temperature (just out of interest). I was sent a code snippet to add to collect the mediaID of the twitter upload once successful which I then included.

The script occasionally fails. I think this is due to using mobile hotspot, but can't prove this. Often connecting to the home wifi later and running it again will be enough to push it out to twitter but once in a while even this isn't enough. In these cases I copy the img files to a new directory then remake the timelapse and this is usually enough for it to tweet.

I'll upload the latest version of the script itself in the very near future for folks to use tweak for other purposes and to offer improvements upon.

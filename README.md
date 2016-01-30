# Hack-Tell
This is my Rokkincat Hack & Tell project on Sat Jan 30, 2016

#### Overview

This project is a simple iOS and python application. The iOS application sends a string over UDP to a python UDP server that can run on (in my case) a raspberry pi 2 B. The string is the name of an mp3 file to play over the audio. As long as the python server and iOS server are on the same network, this will work no problem.

In order for the python server to know which file to play, the name of the song the iOS applicaton sends over must also be the name of the file stored on the desktop of the raspberry pi. (Because of the short time I had to work on this project, there are a lot of hard-coded values however the code should be fairly self-explanatory).


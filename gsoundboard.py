#!/usr/bin/python3
# Soundboard
# By @winkleink 2018
# Developed to use at Panto
# Uses GUIZero to make putting together the interface easier.
# This version is a work in progress and so is a bit of a mess

import os
import time
from guizero import App, Text, Box, PushButton
import pygame
pygame.init()
pygame.mixer.init
pygame.mixer.get_init


screenheight = 400
screenwidth =800

gridheight=int(screenheight/(2*20))
gridwidth=int(screenwidth/(3*10))

def pgplay(audio):
#	pygame.mixer.init
	pygame.mixer.music.load(audio)
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		pygame.time.Clock().tick(100)

def stopmusic():
	pygame.mixer.music.stop()


# Function to play an actual audio file
def do_nothing(audio):
    os.system('omxplayer -o local ' + audio)
    return 0

# When pressing the first half button it hides the second half Box 
# and shows the first half box and changes the heading
def firsthalf():
	global box1h, box2h, button1, text
	box2h.hide()
	box1h.show()
	text = Text(app, width=40, height=1, color="black", text="Babes in the Woods - First Half", grid=[0,0])

# When pressing the second half button it hides the first half Box 
# and shows the second half box and changes the heading
def secondhalf():
	global box1h, box2h, button1,text
	box1h.hide()
	box2h.show()
	text = Text(app, width=40, height=1, color="red", text="Babes in the Woods - Second Half", grid=[0,0])


# Define app to give the window
app = App(title="Babes in the Woods - Panto", height=screenheight, width=screenwidth, layout="grid")
app.tk.attributes('-fullscreen', True)
# text at the top of the page
text = Text(app, width=40, height=1, color="black", text="Babes in the Woods - First Half", grid=[0,0])

# setup box1h for the first half with all it's buttons
box0h = Box(app, layout="grid", grid=[0,1])


# top buttons to change half
buttontop1 = PushButton(box0h, command=firsthalf, text="First Half", grid=[0,0])
#buttontop2 = PushButton(box0h, command=stopmusic, text="Stop Music", grid=[1,0])
buttontop3 = PushButton(box0h, command=secondhalf, text="Second Half", grid=[2,0])

# setup box1h for the first half with all it's buttons
box1h = Box(app, layout="grid", grid=[0,2])

# individual buttons for each sound effect.  button1 before each one to show it's a first half button
button11 = PushButton(box1h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Front_Left.wav"], text="Front Left", grid=[0,2])
button12 = PushButton(box1h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Front_Center.wav"], text="Front Centre", grid=[1,2])
button13 = PushButton(box1h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Front_Right.wav"], text="Front Right", grid=[2,2])
button14 = PushButton(box1h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Rear_Left.wav"], text="Rear Left", grid=[0,3])
button15 = PushButton(box1h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Rear_Center.wav"], text="Rear Centre", grid=[1,3])
button16 = PushButton(box1h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Rear_Right.wav"], text="Rear Right", grid=[2,3])

# setup box1h for the first half with all it's buttons
box2h  = Box(app, layout="grid", grid=[0,2])
# hides it immedatelly as first half buttons will be shown first.
box2h.hide()

# individual buttons for each sound effect.  button2 before each one to show it's a second half button
button21 = PushButton(box2h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Noise.wav"], text="Noise", grid=[0,2])
button22 = PushButton(box2h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Front_Center.wav"], text="Front Centre", grid=[1,2])
button23 = PushButton(box2h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Front_Right.wav"], text="Front Right ", grid=[2,2])
button24 = PushButton(box2h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Rear_Left.wav"], text="Rear Left", grid=[0,3])
#button25 = PushButton(box2h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Rear_Center.wav"], text="5", grid=[1,3])
#button26 = PushButton(box2h, height=gridheight, width=gridwidth, command=pgplay, args=["/home/pi/Music/Rear_Right.wav"], text="6", grid=[2,3])

# this I think acutally runs the GUIZero app thing
app.display()


 

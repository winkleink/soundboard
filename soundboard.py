# Soundboard
# By @winkleink 2018
# Developed to use at Panto
# Uses GUIZero to make putting together the interface easier.
# This version is a work in progress and so is a bit of a mess

import os
import time
from guizero import App, Text, Box, PushButton

screenheight = 400
screenwidth =800

gridheight=int(screenheight/(2*20))
gridwidth=int(screenwidth/(3*10))

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

# text at the top of the page
text = Text(app, width=40, height=1, color="black", text="Babes in the Woods - First Half", grid=[0,0])


# setup box1h for the first half with all it's buttons
box1h = Box(app, layout="grid", grid=[0,1])

# top buttons to change half
buttonfirst1 = PushButton(box1h, command=firsthalf, text="First Half", grid=[0,0])
buttonsecond1 = PushButton(box1h, command=secondhalf, text="Second Half", grid=[2,0])

# individual buttons for each sound effect.  button1 before each one to show it's a first half button
button11 = PushButton(box1h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Front_Left.wav"], text="Opening Music", grid=[0,2])
button12 = PushButton(box1h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Front_Center.wav"], text="First Half 1", grid=[1,2])
button13 = PushButton(box1h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Front_Right.wav"], text="First Half 2", grid=[2,2])
button14 = PushButton(box1h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Rear_Left.wav"], text="First Half 3", grid=[0,3])
button15 = PushButton(box1h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Rear_Center.wav"], text="First Half 4", grid=[1,3])
button16 = PushButton(box1h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Rear_Right.wav"], text="First Half 5", grid=[2,3])

# setup box1h for the first half with all it's buttons
box2h  = Box(app, layout="grid", grid=[0,1])
# hides it immedatelly as first half buttons will be shown first.
box2h.hide()

# top buttons to change half
buttonfirst = PushButton(box2h, command=firsthalf, text="First Half", grid=[0,0])
buttonsecond = PushButton(box2h, command=secondhalf, text="Second Half", grid=[2,0])

# individual buttons for each sound effect.  button2 before each one to show it's a second half button
button21 = PushButton(box2h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Noise.wav"], text="Noise", grid=[0,2])
button22 = PushButton(box2h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Front_Center.wav"], text="Second Half 1", grid=[1,2])
button23 = PushButton(box2h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Front_Right.wav"], text="Second Half 2 ", grid=[2,2])
button24 = PushButton(box2h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Rear_Left.wav"], text="Second Half 4", grid=[0,3])
#button25 = PushButton(box2h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Rear_Center.wav"], text="5", grid=[1,3])
#button26 = PushButton(box2h, height=gridheight, width=gridwidth, command=do_nothing, args=["/home/pi/Music/Rear_Right.wav"], text="6", grid=[2,3])

# this I think acutally runs the GUIZero app thing
app.display()


 

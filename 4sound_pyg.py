#!/usr/bin/python3
# Import a library of functions called 'pygame'
import pygame
from time import sleep
import os
from subprocess import call

# Initialize the game engine
# pygame.mixer.pre_init(44100, -16, 2, 2048,buffer=4096)
# pygame.mixer.init
pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
pygame.init()
# Initialize the sound mixer
pygame.mixer.get_init

start = 0 

act1Text = [] # text for the buttons
act1Sound = [] # sounds for the buttons

act2Text = [] # text for the buttons
act2Sound = [] # sounds for the buttons

black = [ 0, 0, 0]
white = [255,255,255]
red = [255, 0, 0]
grey = [204, 204, 204]
yellow = [255,255,0]
blue = [0,0,255]

# read details from the file
f = open("/home/pi/panto_control/pygame/soundActs.txt", "r")
soundActs = f.read()
print(soundActs)

# start poistion of Label
labelS = soundActs.find("[")
# end position of label
labelE = soundActs.find("]")
# read substring for number of players and convert to an integer so it's a number
label = soundActs[labelS+1:labelE]
print(label)

start=labelE+1


# start position of count of 1st Act buttons
act1CountS = soundActs.find("[", start)
# end position of count of 1st Act buttons
act1CountE = soundActs.find("]", start)
# read substring for number of buttons in the 1st Act
act1Count = int(soundActs[act1CountS+1:act1CountE])
print(act1Count)

start=act1CountE+1

# start position of count of 2nd Act buttons
act2CountS = soundActs.find("[", start)
# end position of count of 2nd Act buttons
act2CountE = soundActs.find("]", start)
# read substring for number of buttons in the 2nd Act
act2Count = int(soundActs[act2CountS+1:act2CountE])
print(act2Count)

start=act2CountE+1

# get the Firt Act Button Names
for n in range(0,act1Count):
    act1ButtonS = soundActs.find("[",start)
    act1ButtonE = soundActs.find("]",start+1)
    act1Text.append(soundActs[act1ButtonS+1:act1ButtonE])
    start = act1ButtonE+1
    print(act1Text[n])

# get the Second Act Button Names
for n in range(0,act2Count):
    act2ButtonS = soundActs.find("[",start)
    act2ButtonE = soundActs.find("]",start+1)
    act2Text.append(soundActs[act2ButtonS+1:act2ButtonE])
    start = act2ButtonE+1
    print(act2Text[n])

# get the First Act Sound
for n in range(0,act1Count):
    act1SoundS = soundActs.find("[",start)
    act1SoundE = soundActs.find("]",start+1)
    act1Sound.append(soundActs[act1SoundS+1:act1SoundE])
    start = act1SoundE+1
    print(act1Sound[n])

# get the Second Act Sound
for n in range(0,act2Count):
    act2SoundS = soundActs.find("[",start)
    act2SoundE = soundActs.find("]",start+1)
    act2Sound.append(soundActs[act2SoundS+1:act2SoundE])
    start = act2SoundE+1
    print(act2Sound[n])


# Set the height and width of the screen
screenWidth=800
screenHeight=480
size=[screenWidth,screenHeight]
# screen=pygame.display.set_mode(size) # in a window 
screen=pygame.display.set_mode(size,pygame.FULLSCREEN) # fullscreen for 7" touchscreen
# Fill the screen White
screen.fill(white)
# Put something in the application Bar
pygame.display.set_caption(label)

# Set the font for the text. Windows computer so usd Ariel
myfont = pygame.font.SysFont("Ariel", 20)

# Created Variable for the text on the screen
title = myfont.render(label, 1, white)
# put the text on the screen
screen.blit(title, (10, 10))

act1Width=int((act1Count+1)/2)
print(act1Width)

act1Columns=int(act1Count/act1Width)

act1buttonWidth=int(screenWidth/act1Width)-20
print("act1buttonWidth : "+str(act1buttonWidth))


act2Width=int((act2Count+1)/2)
print(act2Width)

act2Columns=int(act2Count/act2Width)

act2buttonWidth=int(screenWidth/act2Width)-20
print("act2buttonWidth : "+str(act2buttonWidth))


def act1():
    
    act1Width=int((act1Count+1)/2)
    print(act1Width)

    act1Columns=int(act1Count/act1Width)

    act1buttonWidth=int(screenWidth/act1Width)-20
    print("act1buttonWidth : "+str(act1buttonWidth))

    screen.fill(white)

    # Act 1 Button
    pygame.draw.rect(screen, red, (10,10,100,50), 0)
    screen.blit(myfont.render("Act 1",1,black),(12,12))   

    # Act 2 Button
    pygame.draw.rect(screen, grey, (310,10,100,50), 0)
    screen.blit(myfont.render("Act 2",1,black),(312,12))   
    
    # Stop all Button
    pygame.draw.rect(screen, grey, (610,10,100,50), 0)
    screen.blit(myfont.render("Stop All",1,black),(612,12))   

    # Quit Button
    pygame.draw.rect(screen, grey, (10,420,100,50), 0)
    screen.blit(myfont.render("Quit",1,red),(12,422))   

    # Draw the 4 empty rectangles for the players
    for n in range (0, act1Count):
        pygame.draw.rect(screen, grey, (10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width))),act1buttonWidth,150), 0)
        screen.blit(myfont.render(act1Text[n],1,black),(10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width)))))   
    # show the whole thing
    pygame.display.flip()


def act2():
    
    act2Width=int((act2Count+1)/2)
    print(act2Width)

    act2Columns=int(act2Count/act2Width)

    act2buttonWidth=int(screenWidth/act2Width)-20
    print("act2buttonWidth : "+str(act2buttonWidth))

    screen.fill(white)

    # Act 1 Button
    pygame.draw.rect(screen, grey, (10,10,100,50), 0)
    screen.blit(myfont.render("Act 1",1,black),(12,12))   

    # Act 2 Button
    pygame.draw.rect(screen, red, (310,10,100,50), 0)
    screen.blit(myfont.render("Act 2",1,black),(312,12))   

    # Stop all Button
    pygame.draw.rect(screen, grey, (610,10,100,50), 0)
    screen.blit(myfont.render("Stop All",1,black),(612,12))   

    # Quit Button
    pygame.draw.rect(screen, grey, (10,420,100,50), 0)
    screen.blit(myfont.render("Quit",1,red),(12,422))   

    
    # Draw the 4 empty rectangles for the players
    for n in range (0, act2Count):
        pygame.draw.rect(screen, grey, (10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width))),act2buttonWidth,150), 0)
        screen.blit(myfont.render(act2Text[n],1,black),(10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width)))))   
    # show the whole thing
    pygame.display.flip()


def playSound(sound):
    pygame.mixer.Sound(sound).play(0,0,0)
    print("Playing : " + sound)
    
def do_nothing(audio):
    print("audio is :" + audio)
    print("playing using oxmpayer")
    os.system('omxplayer -o local ' + audio + " &")
    return 0

act2()
sleep(1)

act1()
sleep(1)

whichAct=1

print("Going into the loop") 

done=False # For the main loop

while done==False: # keep going unless I exit application
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.quit()
                done=True
                
            
            # Do the mouse down action (click)
            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse was pressed") 
                mousex, mousey = pygame.mouse.get_pos()
                print(mousex)
                print(mousey)
                
                if (mousex >10 and mousex<110) and (mousey >10 and mousey<60):
                    # Act 1 Button
                    pygame.draw.rect(screen, blue, (10,10,100,50), 0)
                    screen.blit(myfont.render("Act 1",1,black),(12,12))
                    pygame.display.flip()   
                    sleep(0.1)
                    pygame.draw.rect(screen, red, (10,10,100,50), 0)
                    screen.blit(myfont.render("Act 1",1,black),(12,12))   
                    pygame.display.flip()
                    act1()
                    whichAct=1

                if (mousex >310 and mousex<410) and (mousey >10 and mousey<60):
                    # Act 2 Button
                    pygame.draw.rect(screen, blue, (310,10,100,50), 0)
                    screen.blit(myfont.render("Act 2",1,black),(312,12))  
                    pygame.display.flip()
                    sleep(0.1)
                    pygame.draw.rect(screen, red, (310,10,100,50), 0)
                    screen.blit(myfont.render("Act 2",1,black),(312,12))  
                    pygame.display.flip()
                    act2()
                    whichAct=2

                if (mousex >610 and mousex<710) and (mousey >10 and mousey<60):
                    call (["pkill omxplayer"], shell=True)
                    print("pkill omxplayer")
                    pygame.draw.rect(screen, blue, (610,10,100,50), 0)
                    screen.blit(myfont.render("Stop All",1,black),(612,12)) 
                    pygame.display.flip()
                    sleep(0.1)
                    pygame.draw.rect(screen, grey, (610,10,100,50), 0)
                    screen.blit(myfont.render("Stop All",1,black),(612,12)) 
                    pygame.display.flip()
                    
                if (mousex >10 and mousex<110) and (mousey >420 and mousey<470):
                    pygame.draw.rect(screen, yellow, (10,420,100,50), 0)
                    screen.blit(myfont.render("Quit",1,red),(12,422))  
                    pygame.display.flip()
                    sleep(0.1)
                    pygame.mixer.stop()
                    pygame.mixer.init()
                    print("Quit")
                    done=True
               

                if whichAct==1:
                    for n in range (0, act1Count):
                        if(mousex >10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)) and mousex<act1buttonWidth+10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10))) and (mousey>100+(160*(int(n/act1Width))) and mousey<260+(160*(int(n/act1Width)))):
                            print(n)
                            pygame.draw.rect(screen, white, (750,10,100,50), 0)
                            screen.blit(myfont.render("1-"+str(n+1),1,black),(752,12))   
                            pygame.draw.rect(screen, blue, (10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width))),act1buttonWidth,150), 0)
                            screen.blit(myfont.render(act1Text[n],1,black),(10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width)))))   
                            # show the whole thing
                            pygame.display.flip()
                            doSound = "/home/pi/panto_control/pygame/"+act1Sound[n]
#                            playSound(doSound)
                            do_nothing(doSound)
                            sleep(0.1)
                            pygame.draw.rect(screen, grey, (10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width))),act1buttonWidth,150), 0)
                            screen.blit(myfont.render(act1Text[n],1,black),(10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width)))))   
                            # show the whole thing
                            pygame.display.flip()

                            print(doSound)


                            
                if whichAct==2:
                    for n in range (0, act2Count):
                        if(mousex >10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)) and mousex<act2buttonWidth+10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10))) and (mousey>100+(160*(int(n/act2Width))) and mousey<260+(160*(int(n/act2Width)))):
                            print(n)
                            pygame.draw.rect(screen, white, (750,10,100,50), 0)
                            screen.blit(myfont.render("2-"+str(n+1),1,black),(752,12))
                            pygame.draw.rect(screen, blue, (10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width))),act2buttonWidth,150), 0)
                            screen.blit(myfont.render(act2Text[n],1,black),(10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width)))))
                            # show the whole thing
                            pygame.display.flip()
                            doSound = "/home/pi/panto_control/pygame/"+act2Sound[n]
#                            playSound(doSound)
                            do_nothing(doSound)
                            sleep(0.1)
                            pygame.draw.rect(screen, grey, (10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width))),act2buttonWidth,150), 0)
                            screen.blit(myfont.render(act2Text[n],1,black),(10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width)))))
                            print(doSound)

        # Do the mouse over
            print("mouse moved") 
            mousex, mousey = pygame.mouse.get_pos()
            print(mousex)
            print(mousey)
            
            if (mousex >10 and mousex<110) and (mousey >10 and mousey<60):
                # Act 1 Button
                pygame.draw.rect(screen, yellow, (10,10,100,50), 0)
                screen.blit(myfont.render("Act 1",1,black),(12,12))   

            else:
                if whichAct == 1:
                    # Act 1 Button
                    pygame.draw.rect(screen, red, (10,10,100,50), 0)
                    screen.blit(myfont.render("Act 1",1,black),(12,12))   
                else:
                    # Act 1 Button
                    pygame.draw.rect(screen, grey, (10,10,100,50), 0)
                    screen.blit(myfont.render("Act 1",1,black),(12,12))   


            if (mousex >310 and mousex<410) and (mousey >10 and mousey<60):
                # Act 2 Button
                pygame.draw.rect(screen, yellow, (310,10,100,50), 0)
                screen.blit(myfont.render("Act 2",1,black),(312,12))   
            else:   
                if whichAct == 2:
                    # Act 2 Button
                    pygame.draw.rect(screen, red, (310,10,100,50), 0)
                    screen.blit(myfont.render("Act 2",1,black),(312,12)) 
                else:
                    # Act 2 Button
                    pygame.draw.rect(screen, grey, (310,10,100,50), 0)
                    screen.blit(myfont.render("Act 2",1,black),(312,12))   

            if (mousex >610 and mousex<710) and (mousey >10 and mousey<60):
                # Stop all Button
                pygame.draw.rect(screen, yellow, (610,10,100,50), 0)
                screen.blit(myfont.render("Stop All",1,black),(612,12))   
            else:
                # Stop all Button
                pygame.draw.rect(screen, grey, (610,10,100,50), 0)
                screen.blit(myfont.render("Stop All",1,black),(612,12))   

                
            if (mousex >10 and mousex<110) and (mousey >420 and mousey<470):
                # Quit Button
                pygame.draw.rect(screen, yellow, (10,420,100,50), 0)
                screen.blit(myfont.render("Quit",1,red),(12,422))  
            else:
                # Quit Button
                pygame.draw.rect(screen, grey, (10,420,100,50), 0)
                screen.blit(myfont.render("Quit",1,red),(12,422))  

            if whichAct==1:
                for n in range (0, act1Count):
                    if(mousex >10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)) and mousex<act1buttonWidth+10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10))) and (mousey>100+(160*(int(n/act1Width))) and mousey<260+(160*(int(n/act1Width)))):
                        pygame.draw.rect(screen, yellow, (10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width))),act1buttonWidth,150), 0)
                        screen.blit(myfont.render(act1Text[n],1,black),(10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width)))))   
                    else:
                        pygame.draw.rect(screen, grey, (10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width))),act1buttonWidth,150), 0)
                        screen.blit(myfont.render(act1Text[n],1,black),(10+((n-(int(n/act1Width)*act1Width))*(act1buttonWidth+10)),100+(160*(int(n/act1Width)))))   
                        
            if whichAct==2:
                for n in range (0, act2Count):
                    if(mousex >10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)) and mousex<act2buttonWidth+10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10))) and (mousey>100+(160*(int(n/act2Width))) and mousey<260+(160*(int(n/act2Width)))):
                        pygame.draw.rect(screen, yellow, (10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width))),act2buttonWidth,150), 0)
                        screen.blit(myfont.render(act2Text[n],1,black),(10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width)))))
                    else:
                        pygame.draw.rect(screen, grey, (10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width))),act2buttonWidth,150), 0)
                        screen.blit(myfont.render(act2Text[n],1,black),(10+((n-(int(n/act2Width)*act2Width))*(act2buttonWidth+10)),100+(160*(int(n/act2Width)))))   

    pygame.display.flip()


 
                        

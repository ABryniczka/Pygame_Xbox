'''
import sys
import pygame
from pygame.locals import *

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

deadzone = 10

#class klasa():

for joystick in joysticks:
    print(joystick.get_name())

Run = True
while Run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Run = False

        if event.type == JOYBUTTONDOWN:
             if(event.button) == 0:
                 print("A Push")
             elif (event.button) == 1:
                 print("B Push")
             elif (event.button) == 2:
                 print("X Push")
             elif (event.button) == 3:
                 print("Y Push")
             elif (event.button) == 4:
                 print("Left Bumper Push")
             elif (event.button) == 5:
                 print("Right Bumper Push")
             elif (event.button) == 6:
                 print("Back Button Push")
             elif (event.button) == 7:
                 print("Start Button Push")
             elif (event.button) == 8:
                 print("L. Stick Push")
             elif (event.button) == 9:
                 print("R. Stick Push")
             elif (event.button) == 10:
                 print("Guide Button Push")



        if event.type == JOYBUTTONUP:
            if (event.button) == 0:
                print("A Pull")
            elif (event.button) == 1:
                print("B Pull")
            elif (event.button) == 2:
                print("X Pull")
            elif (event.button) == 3:
                print("Y Pull")
            elif (event.button) == 4:
                print("Left Bumper Pull")
            elif (event.button) == 5:
                print("Right Bumper Pull")
            elif (event.button) == 6:
                print("Back Button Pull")
            elif (event.button) == 7:
                print("Start Button Pull")
            elif (event.button) == 8:
                print("L. Stick Pull")
            elif (event.button) == 9:
                print("R. Stick Pull")
            elif (event.button) == 10:
                print("Guide Button Pull")

        if event.type == JOYAXISMOTION:
            zmienna = event.value*100

            if zmienna >= deadzone or zmienna <= -deadzone:

                zmienna1 = str(zmienna)
                zmienna2 = int(zmienna1[0] + "0")

                if zmienna >= (0.1 * zmienna2) and zmienna < zmienna2 + 10:

                    if event.axis == 5:
                        print("Right trigger " + str(event.value))
                    if event.axis == 4:
                        print("Left trigger " + str(event.value))
                    if event.axis == 1:
                        print("Left Thumb Up-Down " + str(event.value)) #Dodatnie do dołu
                    if event.axis == 0:
                        print("Left Thumb Right-Left " + str(event.value)) #dodatni w prawo
                    if event.axis == 3:
                        print()
                    #print(event)


        if event.type == JOYHATMOTION:
            if (event.value) == (1, 0):
                print("Right hatmotion push")
            if (event.value) == (0, 1):
                print("Up hatmotion pull")
            if (event.value) == (-1, 0):
                print("left hatmotion push")
            if (event.value) == (0, -1):
                print("Down hatmotion pull")
            if (event.value) == (0, 0):
                print("Hatmotion released")
            #print(event)
'''

import sys
import pygame
from pygame.locals import *
import numpy as np


class klasa():
    def __init__(self, typ, wartosc, os, przycisk):
        self.typ = typ
        self.wartosc = wartosc
        self.os = os
        self.przycisk = przycisk
        self.count_kill = 0

    def awaria(self, count_kill, Run):
        if (self.typ == JOYBUTTONDOWN and self.przycisk == 7):
            count_kill += 1
            print("Count kill: " + str(count_kill))
        elif (self.typ == JOYBUTTONUP and self.przycisk == 7):
            w_pyte = 0
        else:
            count_kill = 0

        if count_kill == 3:
            print("Error 404")
            Run = False
        else:
            Run = True

        return count_kill, Run


    def obrot_manipulatora(self):
        print("obrot manipulatora")

    def pochylenie_dolne_manipulatora(self):
        print("pochylenie dolne manipulatora")

    def pochylenie_gorne_manipulatora(self):
        print("pochylenie gorne manipulatora")

    def pochylenie_chwytaka(self):
        print("pochylenie chwytaka")

    def obrot_chwytaka(self):
        print("obrot chwytaka")

    def zacisk_chwytaka(self):
        print("zacisk_chwytaka")

pygame.init()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

deadzone = 15
zmienna_comparsion = 0 #np.zeros(1)
count_kill = 0
#class klasa():

lazik = klasa(0, 0, 0, 0)

for joystick in joysticks:
    print(joystick.get_name())
i = 0

Run = True
while Run:
    for event in pygame.event.get():

        #print(event)
        if event.type == pygame.QUIT:
            Run = False

        if event.type == JOYBUTTONDOWN:
             lazik = klasa(event.type, 0, 0, event.button)
             if (event.button) == 4:
                 print(event)
                 print("Left Bumper Push")
             elif (event.button) == 5:
                 print("Right Bumper Push")
             elif (event.button) == 7:
                 print("Start Button Push")

        if event.type == JOYBUTTONUP:
            lazik = klasa(event.type, 0, 0, event.button)
            if (event.button) == 4:
                print("Left Bumper Pull") #Rozcisk chwytaka
            elif (event.button) == 5:
                print("Right Bumper Pull") #Scisk chwytaka
            elif (event.button) == 7:
                print("Start Button Pull") #Awaryjne wylaczenie laziora

        if event.type == JOYAXISMOTION:
            lazik = klasa(event.type, event.value, event.axis, 0)
            zmienna = event.value*100
            #print("zmienna: "+str(zmienna))
            if zmienna >= deadzone or zmienna <= -deadzone:
                if i == 0:

                        zmienna_comparsion = zmienna
                        print("First: "+str(zmienna_comparsion))
                        if event.axis == 5:
                            print("Right trigger " + str(event.value)) #Pochylenie samego chwytaka do gory
                        if event.axis == 4:
                            print("Left trigger " + str(event.value)) #Pochylenie samego chwytaka do dolu
                        if event.axis == 1:
                            print("Left Thumb Up-Down " + str(event.value)) #Dodatnie do dołu [predkosc]
                        if event.axis == 0:
                            print("Left Thumb Right-Left " + str(event.value)) #dodatni w prawo [kierunek jazdy]
                        if event.axis == 3:
                            print()
                            #print(event)
                        i += 1
                else:
                        if zmienna < 0:
                            zmienna_warunek = zmienna*(-1)
                            zmienna1 = str(zmienna_comparsion)
                            zmienna2 = float(zmienna1[1] + "0")

                        else:
                            zmienna_warunek = zmienna
                            zmienna1 = str(zmienna_comparsion)
                            zmienna2 = float(zmienna1[0] + "0")

                        if zmienna2 < zmienna_warunek <= zmienna2+10:
                            continue

                        else:
                            if event.axis == 5:
                                print("Right trigger " + str(event.value))
                            if event.axis == 4:
                                print("Left trigger " + str(event.value))
                            if event.axis == 1:
                                print("Left Thumb Up-Down " + str(event.value))  # Dodatnie do dołu
                            if event.axis == 0:
                                print("Left Thumb Right-Left " + str(event.value))  # dodatni w prawo
                            if event.axis == 3:
                                print("Right Thumb Up-Down" + str(event.value)) #pochylenie manipulatora
                            if event.axis == 2:
                                print("Right Thumb Left-Right" + str(event.value)) #Obrot manipulatora
                            zmienna_comparsion = zmienna
                        i += 1
            else:
                zmienna = 0
                print(zmienna)
                continue

        if event.type == JOYHATMOTION:
            lazik = klasa(event.type, event.value, 0, 0)
            if (event.value) == (1, 0):
                print("Right hatmotion push") #Obrot chwytaka w prawo
            if (event.value) == (0, 1):
                print("Up hatmotion pull") #Wybor silnika manipulatora do gory
            if (event.value) == (-1, 0):
                print("left hatmotion push") #Obrot chwytaka w lewo
            if (event.value) == (0, -1):
                print("Down hatmotion pull") #Wybor silnika manipulatora w dol
            if (event.value) == (0, 0):
                print("Hatmotion released")



        count_kill, Run = lazik.awaria(count_kill, Run)

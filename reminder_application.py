# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 22:29:03 2021

@author: Ayush
"""

from pygame import mixer
import datetime
import time

def get_time():
    return (datetime.datetime.now())

def water_reminder():
    time.sleep(10)
    mixer.init()
    mixer.music.load("water.mp3")
    mixer.music.play()
    response1=input("Please! Enter ""Done"" to stop the Alarm\n")
    if(response1=="Done" or response1=="done"):
        mixer.music.pause()
        
def eye_reminder():
    time.sleep(10)
    mixer.init()
    mixer.music.load("eyes.mp3")
    mixer.music.play()
    response2=input("Eye exercise time.Enter ""Done"" to stop the Alarm\n")
    if(response2=="Done" or response2=="done"):
        mixer.music.pause()
        with open("eyes.txt","a") as f:
            f.write(f"Eyes relaxed at {get_time()}\n")


def exercise_reminder():
    time.sleep(10)
    mixer.init()
    mixer.music.load("exercise.mp3")
    mixer.music.play()
    response3=input("Exercise time.Enter ""Done"" to stop the Alarm\n")
    if(response3=="Done" or response3=="done"):
        mixer.music.pause()
        with open("exercise.txt","a") as f:
            f.write(f"Physical Exercise done at {get_time()}\n")
water_level=0
while True :
    
    water_reminder()
    level = int(input('How much water did you drink '))
    with open("water.txt","a") as f:
        f.write(f"Water drank at {get_time()} {level} ml.\n")
    water_level=water_level+level
    if water_level>3500:
        print("Water goal Completed")
    else:
        print(f"{3500-water_level} ml remaining")
    eye_reminder()
    exercise_reminder()
        
        
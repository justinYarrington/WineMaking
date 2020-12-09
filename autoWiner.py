import math
from random import randint, uniform, choice, random
import sys
import time
import numpy as np
import pyautogui as pag
from itertools import chain
import os

def rightclickIcon(item):
    """Will use special if image is provided"""
    if not item:
        print('inif')
        return False
    r = randint(28, 32)
    t = uniform(4.8, 7)
    clicktime = t/r
    random_wait(clicktime - .04, clicktime + .04)
    center = pag.center(item)
    random_coordinate(center, item)
    pag.rightClick()
    return True

def clickIcon(item):
    """Will use special if image is provided"""
    if not item:
        print('inif')
        return False
    r = randint(28, 32)
    t = uniform(4.8, 7)
    clicktime = t/r
    random_wait(clicktime - .04, clicktime + .04)
    center = pag.center(item)
    random_coordinate(center, item)
    pag.click()
    return True

def travel_time(x2, y2):
        """Calculates cursor travel time in seconds per 240-270 pixels, based on a variable rate of movement"""
        rate = uniform(0.09, 0.15)
        x1, y1 = pag.position()
        distance = math.sqrt(math.pow(x2-x1, 2)+math.pow(y2-y1, 2))
        return max(uniform(.08, .12), rate * (distance/randint(250, 270)))

def random_coordinate(center, item):
        """Moves cursor to random locaction still above the object to be clicked"""
        x = randint(center[0], center[0]+int(item[2]/4))
        y = randint(center[1], center[1]+int(item[3]/4))
        time = travel_time(x, y)
        print('X:%s,Y:%s' % (x,y))
        return pag.moveTo(x, y, time)

def random_wait(min=0.25, max=0.50):
    """Waits a random number of seconds between two numbers (0.25 and 0.50 default) to mimic human reaction time"""
    return time.sleep(uniform(min, max))

def get_new_time_to_perform_action():
    """Used to figure out when we want to perform a random action during our while loop, such as checking fishing XP"""
    delay_minutes = (30 + random() * 30) # 30-60 minutes
    return time.time() + delay_minutes * 60

if __name__ == '__main__':
    try:
        while True:
            """Check if in inventory or not, if not open it"""
            if (pag.locateOnScreen('images\\inventoryClosed.png', confidence=0.95)):
                inventoryImage = pag.locateOnScreen('images\\inventoryClosed.png', confidence=0.95)
                clickIcon(inventoryImage)
            
            """Begin process of depositing good/bad wines"""
            # Find banker and click it
            banker = pag.locateOnScreen('images\\bankWindow.png', confidence=0.55)
            clickIcon(banker)

            # Deposit fermenting wines. 
            deposit = pag.locateOnScreen('deposit\\depositThis.png', confidence=0.9)
            clickIcon(deposit)
            random_wait(0.5, 1)
            deposit = pag.locateOnScreen('deposit\\depositThis.png', confidence=0.9)
            clickIcon(deposit)

            # Withdraw 14 jugs of water and 14 berries. 
            withdraw14jugs = pag.locateOnScreen('images\\jugOfWater.png', confidence=0.95)
            withdraw14berries = pag.locateOnScreen('images\\berries.png', confidence=0.9)
            rightclickIcon(withdraw14jugs)
            withdraw14 = pag.locateOnScreen('images\\withdraw14.png', confidence=0.95)
            clickIcon(withdraw14)
            rightclickIcon(withdraw14berries)
            withdraw14 = pag.locateOnScreen('images\\withdraw14.png', confidence=0.95)
            clickIcon(withdraw14)
            

            # close out of the bank
            closeBank = pag.locateOnScreen('images\\closeBank.png', confidence=0.9)
            clickIcon(closeBank)

            #begin process of making wines
            clickJugOfWater = pag.locateOnScreen('images\\waterInInventory.png', confidence=0.9)
            clickBerries = pag.locateOnScreen('images\\berryInInventory.png', confidence=0.9)
            clickIcon(clickJugOfWater)
            clickIcon(clickBerries)
            random_wait(1, 2)
            makeWines = pag.locateOnScreen('images\\clickWineJug.png', confidence=0.9)
            clickIcon(makeWines)
            random_wait(17, 20)

    except KeyboardInterrupt:
        sys.exit()
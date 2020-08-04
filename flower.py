# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time
import random

mc =Minecraft.create()
N=0


while N != 50:
    x,y,z=mc.player.getTilePos()
    F=random.randrange(8)
    mc.setBlock (x,y,z,38,F)
    N+=1
    time.sleep(0.2)
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time
import random
time.sleep(3)

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()


color=random.randrange(16)
mc.setBlocks(x+5,y-1,z+5,x-5,y-1,z-5,95,color)
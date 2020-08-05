# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time

mc =Minecraft.create()

x,y,z=mc.player.getTilePos()


for i in range(20):
    mc.setBlock(x+i,y-1,z+i,98,2)
    mc.setBlock(x+i+1,y-1,z+i,98,2)
    mc.setBlock(x+i-1,y-1,z+i,98,2)
    time.sleep(0.5)
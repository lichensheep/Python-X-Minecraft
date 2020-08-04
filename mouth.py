# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()

time.sleep(3)

mc.setBlock(x,y,z+1,165)
time.sleep(0.5)
mc.setBlock(x,y,z-1,165)
time.sleep(0.5)
mc.setBlock(x-1,y,z,165)
time.sleep(0.5)
mc.setBlock(x+1,y,z,165)
time.sleep(0.5)
mc.setBlock(x-1,y,z+1,165)
time.sleep(0.5)
mc.setBlock(x+1,y,z-1,165)
time.sleep(0.5)
mc.setBlock(x+1,y,z+1,165)
time.sleep(0.5)
mc.setBlock(x-1,y,z-1,165)
time.sleep(0.5)
mc.setBlock(x,y,z+2,165)
time.sleep(0.5)
mc.setBlock(x,y,z-2,165)
time.sleep(0.5)
mc.setBlock(x-2,y,z,165)
time.sleep(0.5)
mc.setBlock(x+2,y,z,165)
time.sleep(0.5)
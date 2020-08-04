# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time
time.sleep(7)

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlocks(x+8,y-1,z+8,x-8,y-1,z-8,42)
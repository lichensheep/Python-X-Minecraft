# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time

mc =Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.setBlock (x,y,z,8)
    mc.setBlock (x,y,z,19)
    time.sleep(10)
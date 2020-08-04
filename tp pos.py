# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time

mc =Minecraft.create()

time.sleep(5)

x,y,z=mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
y+=1

time.sleep(0.5)

mc.player.setTilePos(x,y,z)
y+=1

time.sleep(0.5)
mc.player.setTilePos(x,y,z)
y+=1

time.sleep(0.5)
mc.player.setTilePos(x,y,z)
y+=1

time.sleep(0.5)

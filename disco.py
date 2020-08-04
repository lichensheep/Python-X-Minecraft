# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import time
time.sleep(3)

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()

wibth=10 #寬
heith=6 #高
length=10 #長
block=5 #木材
air=0

mc.setBlocks(x,y,z,x+wibth,y+heith,z+length,block)
mc.setBlocks(x+1,y+1,z+1,x+wibth-1,y+heith-1,z+length-1,air)
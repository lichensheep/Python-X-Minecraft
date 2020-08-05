# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()
a=0

while a != 15:   
    mc.setBlocks(x-30,y-1,z,x+30,y-25,z,19)
    a+=1
    z=z+5
   
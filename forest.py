# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()


def Tree(x,y,z):
    mc.setBlocks(x-1,y+2,z-1,x+1,y+4,z+1,57)
    mc.setBlocks(x,y,z,x,y+2,z,17,1)

x,y,z=mc.player.getTilePos()

for i in range(20):
    for j in range(20):
        Tree(x+i*5,y,z+j*5)
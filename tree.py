# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlocks(x-1,y+2,z-1,x+1,y+4,z+1,56)
mc.setBlocks(x,y,z,x,y+2,z,17,1)
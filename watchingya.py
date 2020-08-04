# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("你現在的座標是:X:"+str(x)+",Y:"+str(y)+",Z:"+str(z))
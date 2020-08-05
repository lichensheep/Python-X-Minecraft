# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft
import random

mc =Minecraft.create()
pos=mc.player.getTilePos()

while True:
    x=pos.x+random.uniform(-10, 10)
    y=pos.y+20
    z=pos.z+random.uniform(-10, 10)
    
    mc.spawnEntity(x,y,z,)
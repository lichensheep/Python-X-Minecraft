`# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlock(x,y-1,z,11)
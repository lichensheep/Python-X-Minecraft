# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()
t=0

while True:
    t=t+1
    mc.postToChat("第"+str(t)+"次")
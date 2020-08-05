# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()

while True:
    hits=mc.events.pollBlockHits()
    if len(hits) > 0:
        hit=hits[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        mc.postToChat("好棒棒你獵到惹"+str(block))
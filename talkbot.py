# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from mcpi.minecraft import Minecraft

mc =Minecraft.create()
x,y,z=mc.player.getTilePos()

try:
    block=int(input("你想要放尛方塊呢??"))
    mc.setBlock(x,y,z,block)
except:
    mc.postToChat("只能輸入數字啦(〝皿〞＃)")
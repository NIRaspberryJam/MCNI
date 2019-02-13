# Northern Ireland Raspbery Jam Libary for Advanced Minecraft Projects 1.0


from mcpi import minecraft
mc = minecraft.Minecraft.create("")

import mcpi.block as block
import mcpi.minecraft as minecraft
import random
def printTree(t):
    while t>0:
        x=random.randint(-60, 60)
        y=1
        z=random.randint(-60, 60)
        mc.setBlocks(x+1, y, z, x+1, y+4, z, 17)
        mc.setBlocks(x+2, y+2, z+1, x, y+3, z-1, 18)
        mc.setBlocks(x+1, y+2, z, x+1, y+4, z, 18)
        mc.setBlocks(x, y+3, z-1, x, y+3, z-1, 0)
        mc.setBlocks(x, y+3, z+1, x, y+3, z+1, 0)
        mc.setBlocks(x+2, y+3, z-1, x+2, y+4, z-1, 0)
        mc.setBlocks(x+2, y+3, z+1, x+2, y+4, z+1, 0)
        t=t-1

    
def drawSphere(mc, x1, y1, z1, radius, blocktype, blockdata=0):
    for x in range(radius*-1,radius):
        for y in range(radius*-1,radius):
            for z in range(radius*-1,radius):
                if (x**2 + y**2 +z**2 < radius**2 and (x**2 + y**2 +z**2 > (radius-2)**2)):
                    mc.setBlock(x1 + x, y1 + y, z1 +z, blocktype, blockdata)



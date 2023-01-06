import time
import keyboard
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
bedroks = 7
air = 0
lava = 10

start_x, start_y, start_z = mc.player.getTilePos()


def game_generation(block_id: int, height_down: int, height_up: int, cluster="middle"):
    import random

    stone = 1
    air = 0

    if cluster == "big":
        size = 9
    elif cluster == "middle":
        size = 7
    elif cluster == "small":
        size = 5

    mc.setBlocks(start_x, height_down, start_z,
                 start_x+size, height_up, start_z+size, block_id)

    # идеальный баланс - big и size3*5
    air_blocks = 0
    while air_blocks <= size**1.95 *5:
        air_blocks += 1
        air_x = random.randint(start_x, start_x+size)
        air_y = random.randint(height_down, height_up)
        air_z = random.randint(start_z, start_z+size)
        mc.setBlock(air_x, air_y, air_z, stone)

    mc.setBlocks(start_x, height_down, start_z, start_x +
                 size, height_up, start_z, bedroks)
    mc.setBlocks(start_x+7, height_down, start_z+1, start_x +
                 size, height_up, start_z+7, bedroks)
    mc.setBlocks(start_x, height_down, start_z+7, start_x
                 +9, height_up, start_z+7, bedroks)

    mc.setBlocks(start_x, height_down, start_z, start_x
                 , height_up, start_z+7, bedroks)
    return [height_down, height_up, size]


def lava_generation(x, y, z):
    height = game_generation(0, 70, 100, "middle")
    print("Лава пошла")
    for stage in range(height[1] - height[0]):
        print("Лава на этапе", stage)
        mc.setBlocks(x, height[0]+stage, z, x+height[2],
                     height[0]+stage, z+height[2], lava)
        time.sleep(5)


if __name__ == "__main__":
    while True:
        if keyboard.is_pressed("q"):
            lava_generation(start_x, start_y, start_z)
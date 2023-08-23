#texture in ursina
from ursina import *


def update():
    for entities in cube:
        # if held_keys['r']:
          if key=="r":
            entities.rotation_z = entities.rotation_z + time.dt * 50


app = Ursina()
cube = []
cube1 = Entity(model="cube", color=color.red,
               rotation=(45, 45, 0), position=(0, -2, 0), texture="brick")
cube.append(cube1)
cube2 = Entity(model="cube", color=color.red,
               rotation=(45, 45, 0), position=(2, 0, 0), texture="sky_sunset")
cube.append(cube2)

cube3 = Entity(model="cube", color=color.red, rotation=(
    45, 45, 0), position=(0, 2, 0), texture="radial_gardient")
cube.append(cube3)

app.run()

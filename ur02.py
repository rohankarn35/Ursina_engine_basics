from ursina import *
from random import *
# movement in ursina engine
# def update():
#     # cube.x = cube.x-time.dt
#     # cube.y = cube.y + time.dt
#     cube.z = cube.z + time.dt #moving cube with respect to time


#rotations
# def update():
#     cube.rotation_x=cube.rotation_x + time.dt
#     cube.rotation_y=cube.rotation_y + time.dt
#     cube.rotation_z=cube.rotation_z + time.dt

def update():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0, 255)
    cube.color=color.rgb(red,green,blue)
    cube.rotation_x=cube.rotation_x + time.dt*50
    cube.rotation_y=cube.rotation_y + time.dt*50
    cube.rotation_z=cube.rotation_z + time.dt*50



app = Ursina()
cube = Entity(model="cube",color=color.red)





app.run()
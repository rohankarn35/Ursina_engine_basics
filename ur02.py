from ursina import *
# movement in ursina engine
# def update():
#     # cube.x = cube.x-time.dt
#     # cube.y = cube.y + time.dt
#     cube.z = cube.z + time.dt #moving cube with respect to time


#rotations
def update():
    cube.rotation_x=cube.rotation_x + time.dt
    cube.rotation_y=cube.rotation_y + time.dt
    cube.rotation_z=cube.rotation_z + time.dt


app = Ursina()
cube = Entity(model="cube",color=color.red)





app.run()
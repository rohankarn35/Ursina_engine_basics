# from ursina import *

# def update():
#     global speed
#     cube.x = cube.x + time.dt*speed
#     if abs(cube.x)>3:
#         speed=speed*-1
#         # cube.x = -3

# app = Ursina()
# speed = 1
# cube = Entity(model="cube", color=color.red)


# app.run()

from ursina import *

def update():
    global m
    m=m+1
    num_frame=200
    n=m%num_frame
    if n<num_frame//2: #range will be between [0,99]
        cube.rotation_z = cube.rotation_z + time.dt*100

    else:

        cube.rotation_z = cube.rotation_z - time.dt*100

    # global m
    # m=m+1
    # num_frame=200
    # n = m%num_frame
    # if n<num_frame//2:

    #     cube.x=cube.x+time.dt
    # else:
    #     cube.x=cube.x - time.dt


app=Ursina()
m=0
cube=Entity(model="cube", color=color.red)
app.run()
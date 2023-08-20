from ursina import *

app = Ursina()

# cube = Entity(model = "Cube", scale=( 3,2,2)) Creating a cube
# cube = Entity(model = "Cube", position=(3,2,1))
# cube = Entity(model = "circle")
cube = Entity(model = "sphere", color=color.red)
txt = Text(text="Ursina Engine", color=color.green, x=0.2, y=0.3)
# cube = Entity(model = "sphere")
app.run()
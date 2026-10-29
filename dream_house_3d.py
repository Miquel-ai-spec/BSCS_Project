from vpython import *

scene = canvas(
    title="Dream House 3D",
    width=1100,
    height=720,
    background=vector(0.63, 0.82, 0.96),
    center=vector(0, 4, 0),
    forward=vector(-1, -0.45, -1),
)
scene.caption = "\nDrag to orbit • Scroll to zoom • Right-drag to pan\n"


wall = vector(0.88, 0.86, 0.79)
white = vector(0.96, 0.95, 0.90)
concrete = vector(0.43, 0.46, 0.48)
dark = vector(0.12, 0.15, 0.18)
glass = vector(0.12, 0.48, 0.62)
wood = vector(0.42, 0.23, 0.12)
grass = vector(0.20, 0.43, 0.23)
leaf = vector(0.12, 0.36, 0.18)

def block(pos, size, color, opacity=1, texture=None):
    return box(pos=vector(*pos), size=vector(*size), color=color,
               opacity=opacity, texture=texture)

def tree(x, z, scale=1):
    cylinder(pos=vector(x, 0, z), axis=vector(0, 2.0*scale, 0),
             radius=0.18*scale, color=wood)
    for y, r in [(1.7, 0.85), (2.35, 0.68), (2.9, 0.48)]:
        sphere(pos=vector(x, y*scale, z), radius=r*scale,
               color=leaf, opacity=0.96)


block((0, -0.35, 0), (48, 0.6, 38), grass)
block((0, 0.02, 0), (30, 0.25, 22), concrete)
block((0, 0.17, 0), (28, 0.12, 20), vector(0.70, 0.70, 0.66))


block((0, 0.12, 12.2), (8, 0.18, 10), concrete)
for z in [8.3, 10.0, 11.7, 13.4, 15.1]:
    block((0, 0.23, z), (5.2, 0.07, 1.05), vector(0.66, 0.68, 0.67))


block((0, 2.0, 0), (18, 3.8, 10), wall)

block((-5.7, 1.9, 5.08), (6.2, 3.15, 0.16), dark)
for x in [-7.6, -5.7, -3.8]:
    block((x, 1.9, 5.19), (0.08, 2.85, 0.05), concrete)

block((2.0, 2.05, 5.09), (8.8, 3.15, 0.12), dark)
block((2.0, 2.05, 5.17), (8.35, 2.72, 0.035), glass, opacity=0.66)
for x in [-2.0, 0.2, 2.4, 4.6, 6.0]:
    block((x, 2.05, 5.21), (0.07, 2.75, 0.05), dark)
block((2.0, 0.48, 5.25), (8.4, 0.08, 0.2), white)


block((8.0, 1.7, 5.13), (1.35, 2.8, 0.18), wood)
block((8.0, 1.7, 5.24), (1.05, 2.5, 0.04), vector(0.53, 0.30, 0.17))
sphere(pos=vector(8.38, 1.65, 5.31), radius=0.08, color=vector(0.88, 0.72, 0.3))


block((1.0, 5.25, -0.15), (14.5, 2.5, 8.5), white)

block((1.0, 5.25, 4.14), (10.8, 1.75, 0.1), dark)
block((1.0, 5.25, 4.21), (10.25, 1.48, 0.035), glass, opacity=0.72)
for x in [-3.1, -0.2, 2.7, 5.6]:
    block((x, 5.25, 4.25), (0.07, 1.55, 0.05), dark)

block((1.0, 4.02, 5.05), (12.5, 0.18, 2.2), concrete)
block((1.0, 4.58, 6.08), (12.0, 0.95, 0.08), glass, opacity=0.35)
for x in [-4.8, -2.8, -0.8, 1.2, 3.2, 5.2, 6.8]:
    cylinder(pos=vector(x, 4.08, 6.08), axis=vector(0, 0.95, 0),
             radius=0.035, color=white)


block((0.8, 6.65, -0.2), (16.4, 0.32, 10.2), dark)
block((0.8, 6.84, -0.2), (15.6, 0.08, 9.5), white)


block((-6.2, 3.65, 0.5), (5.4, 0.22, 7.2), dark)
for x in [-8.5, -4.0]:
    for z in [-2.5, 3.5]:
        cylinder(pos=vector(x, 0.3, z), axis=vector(0, 3.25, 0),
                 radius=0.09, color=dark)


block((-0.2, 0.72, 10.8), (3.0, 0.75, 4.6), vector(0.13, 0.22, 0.32))
block((-0.2, 1.22, 10.7), (2.45, 0.75, 2.4), glass, opacity=0.82)
for x in [-1.45, 1.05]:
    for z in [9.3, 12.2]:
        cylinder(pos=vector(x, 0.48, z), axis=vector(0.16, 0, 0),
                 radius=0.42, color=dark)
        cylinder(pos=vector(x+0.08, 0.48, z), axis=vector(0.18, 0, 0),
                 radius=0.22, color=concrete)


block((12.5, 0.15, 0.0), (7.0, 0.22, 10.5), white)
block((12.5, 0.29, 0.0), (6.3, 0.08, 9.8), vector(0.08, 0.52, 0.78), opacity=0.9)

for z in [-2.8, 0.0, 2.8]:
    block((17.0, 0.55, z), (1.4, 0.18, 2.2), white)
    block((17.0, 0.92, z-0.65), (1.4, 0.8, 0.18), white)


block((0, 0.55, -10.0), (28, 0.8, 0.35), concrete)
for x in [-10, -6, 6, 10]:
    cylinder(pos=vector(x, 0.35, 7.0), axis=vector(0, 0.75, 0),
             radius=0.08, color=white)
    sphere(pos=vector(x, 1.12, 7.0), radius=0.16,
           color=vector(1.0, 0.83, 0.45), emissive=True)


for x, z, s in [(-13,-7,1.1), (-12,5,0.9), (13,-7,1.0),
                (19,-5,1.2), (-16,0,1.0), (15,7,0.9),
                (-10,10,0.8), (10,10,0.85)]:
    tree(x, z, s)




block((16, 0.65, 9.5), (2.4, 1.2, 2.0), wood)


roof_left = box(
    pos=vector(15.4, 1.45, 9.5),
    size=vector(1.5, 0.18, 2.3),
    color=dark
)
roof_left.rotate(
    angle=radians(-30),
    axis=vector(0, 0, 1),
    origin=vector(15.4, 1.45, 9.5)
)

roof_right = box(
    pos=vector(16.6, 1.45, 9.5),
    size=vector(1.5, 0.18, 2.3),
    color=dark
)
roof_right.rotate(
    angle=radians(30),
    axis=vector(0, 0, 1),
    origin=vector(16.6, 1.45, 9.5)
)


block((16, 0.55, 10.52), (0.8, 0.9, 0.05), dark)


dog_color = vector(0.62, 0.35, 0.16)

sphere(pos=vector(18.2, 0.65, 10), radius=0.45,
       color=dog_color)

sphere(pos=vector(18.55, 1.05, 10), radius=0.32,
       color=dog_color)

sphere(pos=vector(18.82, 1.05, 10.2), radius=0.09,
       color=dark)

for x in [17.95, 18.4]:
    for z in [9.75, 10.25]:
        cylinder(
            pos=vector(x, 0.15, z),
            axis=vector(0, 0.35, 0),
            radius=0.09,
            color=dog_color
        )


cone(pos=vector(18.4, 1.32, 9.85),
     axis=vector(0, 0.25, 0),
     radius=0.12, color=dog_color)

cone(pos=vector(18.7, 1.32, 9.95),
     axis=vector(0, 0.25, 0),
     radius=0.12, color=dog_color)

label(pos=vector(16, 2.0, 9.5),
      text="",
      height=12,
      box=False,
      color=white)

sphere(pos=vector(-18, 18, -16), radius=3.8,
       color=vector(1.0, 0.86, 0.45), emissive=True)

sphere(
    pos=vector(-18, 18, -16),
    radius=2.5,
    color=vector(1.0, 0.78, 0.15),
    emissive=True
)


sphere(
    pos=vector(-18, 18, -16),
    radius=3.2,
    color=vector(1.0, 0.72, 0.25),
    opacity=0.12,
    emissive=True
)


scene.camera.pos = vector(25, 17, 27)
scene.camera.axis = vector(-25, -10, -27)
scene.range = 25
scene.autoscale = False


while True:
    rate(30)
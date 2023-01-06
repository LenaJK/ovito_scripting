import warnings
warnings.filterwarnings('ignore', message='.*OVITO.*PyPI')
from ovito.io import *
from ovito.vis import *
from ovito.modifiers import *
import math
from math import *
import numpy as np
from numpy import linalg as LA
import ovito




####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### ####### #######
# file import
pipeline = import_file("output.xyz", columns = ["ID", "MOL", "Particle Type", "Position.X", "Position.Y", "Position.Z", "mux", "muy", "muz"], multiple_frames = True)


# pipeline.add_to_scene()
pipeline.add_to_scene()


type_list = pipeline.source.data.particles.particle_types.types
Nparticletypes = 2500
interval = (Nparticletypes - 1) / 7

pipeline.modifiers.append(SelectTypeModifier(types={1}))
pipeline.modifiers.append(AssignColorModifier(color=(0.905882353, 0.905882353, 0.905882353)))

# B1
Filament = np.arange(2, 3 * interval + 2)
Fupper = [i for i in Filament if (i-1)%3==0]
Flower = [i for i in Filament if (i-1)%3!=0]
setFilupper = set(Fupper)
setFillower = set(Flower)
pipeline.modifiers.append(SelectTypeModifier(types=setFilupper))
pipeline.modifiers.append(AssignColorModifier(color=(0.99, 1.0, 0.43)))

pipeline.modifiers.append(SelectTypeModifier(types=setFillower))
pipeline.modifiers.append(AssignColorModifier(color=(0.96, 0.78, 0.21)))


# B2
Filament = np.arange(3 * interval + 2, 4 * (interval) + 2)
Fupper = [i for i in Filament if (i-1)%3==0]
Flower = [i for i in Filament if (i-1)%3!=0]
setFilupper = set(Fupper)
setFillower = set(Flower)
pipeline.modifiers.append(SelectTypeModifier(types=setFilupper))
pipeline.modifiers.append(AssignColorModifier(color=(0.47, 0.96, 1.0)))

pipeline.modifiers.append(SelectTypeModifier(types=setFillower))
pipeline.modifiers.append(AssignColorModifier(color=(0.0, 0.62, 0.89)))

# B1
Filament = np.arange((interval) * 4 + 2, Nparticletypes + 1)
Fupper = [i for i in Filament if (i-1)%3==0]
Flower = [i for i in Filament if (i-1)%3!=0]
setFilupper = set(Fupper)
setFillower = set(Flower)
pipeline.modifiers.append(SelectTypeModifier(types=setFilupper))
pipeline.modifiers.append(AssignColorModifier(color=(0.99, 1.0, 0.43)))

pipeline.modifiers.append(SelectTypeModifier(types=setFillower))
pipeline.modifiers.append(AssignColorModifier(color=(0.96, 0.78, 0.21)))





renderer = OpenGLRenderer()
pipeline.compute()
pipeline.add_to_scene()
pipeline.source.data.cell.vis.render_cell = False

numFrames = pipeline.source.num_frames
useFrame = numFrames															# event frame to be rendered
# outName = 'testrun.png'c
data=pipeline.compute(useFrame)

print(numFrames)

pipeline.add_to_scene()
transparencyModifier = ComputePropertyModifier()
transparencyModifier.output_property = "Transparency"
transparencyModifier.expressions = ["ParticleType == 1 ? 0.85 : 0"]
pipeline.modifiers.append(transparencyModifier)

pipeline.compute()
pipeline.add_to_scene()

#
#
# type_list = pipeline.source.data.particles.particle_types.types
# Nparticletypes = 5593
# interval = (Nparticletypes-1)/(8)
#
# for i in range(Nparticletypes):
# 	if i==0:
# 		type_list[0].radius = 0.5
# 		type_list[0].color = (0.905882353, 0.905882353, 0.905882353)
# 	elif i>=1 and i<interval*3+1:
# 		type_list[i].radius = 0.5
# 		type_list[i].color = (0.39, 0.39, 0.39)
# 	elif i>=interval*3+1 and i<(interval*5)+1:
# 		type_list[i].radius = 0.5
# 		type_list[i].color = (1, 0, 0)
# 	elif i>=1+(interval*5):
# 		type_list[i].radius = 0.5
# 		type_list[i].color = (0.39, 0.39, 0.39)
# pipeline.compute()
# pipeline.add_to_scene()
# pipeline.source.data.cell.vis.render_cell = False
#
numFrames = pipeline.source.num_frames
useFrame = numFrames															# event frame to be rendered
# outName = 'testrun.png'c
data=pipeline.compute(useFrame)




pipeline.add_to_scene()
transparencyModifier = ComputePropertyModifier()
transparencyModifier.output_property = "Transparency"
transparencyModifier.expressions = ["ParticleType == 1 ? 0.85 : 0"]
pipeline.modifiers.append(transparencyModifier)

pipeline.compute()
pipeline.add_to_scene()


camPos = [0,-110,0]																# camera position
camDir =  [0,1,0]
# camPos = [0,0,-100]																# camera position
# camDir =  [0,0,1]
camDirNormed =  camDir/LA.norm(camDir)											# camera direction (normed)
data=pipeline.compute(useFrame)
# ###visualisation###
# data.particles.vis.shape = ParticlesVis.Shape.Sphere
data.particles.vis.radius = 0.5
# data.particle.vis.Transparency = 0.9
# data.cell.vis.enabled = False   
# 
data=pipeline.compute(useFrame)


vp = Viewport()
vp.type = Viewport.Type.Perspective
vp.camera_pos = (camPos[0],camPos[1],camPos[2])
vp.camera_dir = (camDir[0],camDir[1],camDir[2])
vp.fov = math.radians(55.0)

# renderer = TachyonRenderer(shadows = True ,ambient_occlusion_brightness = .8, ambient_occlusion_samples = 20 , antialiasing = True, antialiasing_samples = 20,  aperture = 0.01, depth_of_field = False,focal_length = 20)
renderer = OpenGLRenderer()
# 
# image = vp.render_image(
# filename='sequential1.png' ,  
# size=(1200, 1000), 
# alpha = True, 
# frame = 144, 
# background = (0.,0.,0.),  
# renderer=renderer)


vp = Viewport()
vp.type = Viewport.Type.Perspective
vp.camera_pos = (camPos[0],camPos[1],camPos[2])
vp.camera_dir = (camDir[0],camDir[1],camDir[2])
vp.fov = math.radians(55.0)


image = vp.render_image(
filename='1.png' ,
size=(1200, 1000),
# alpha = True,
frame =  3,
background = (1.,1.,1.),
renderer=renderer)

image = vp.render_image(
filename='2.png' ,
size=(1200, 1000),
# alpha = True,
frame =  int(numFrames*0.5),
background = (1.,1.,1.),
renderer=renderer)

image = vp.render_image(
filename='3.png' ,
size=(1200, 1000),
# alpha = True,
frame =  int(numFrames),
background = (1.,1.,1.),
renderer=renderer)


vp.render_anim(filename = './output.mov',
		size = (1000,1000),
		range = (1,pipeline.source.num_frames),
		every_nth = 4,
		fps = 12,
		background = (1.,1.,1.),
		renderer = TachyonRenderer(ambient_occlusion = True,
						ambient_occlusion_brightness = 0.7,
						ambient_occlusion_samples = 16,
						antialiasing = True,
						antialiasing_samples = 16,
						direct_light = True,
						direct_light_intensity = 2,
						shadows = True)
)

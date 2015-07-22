# -*- coding: utf-8 -*-
import os
import pylab
import numpy

from matplotlib.patches import Arrow, Ellipse, Rectangle, FancyArrowPatch, PathPatch
import matplotlib.colors as colors
import matplotlib.cm as cmx
from matplotlib import animation

from mpl_toolkits.mplot3d import Axes3D, proj3d
import mpl_toolkits.mplot3d.art3d as art3d

from time import sleep
from math import ceil, floor, sqrt

#         ---- plot 3d scatter of E vs I vs weight ----

# Major data, (x,y,z, extra_infos)
Data = [(1,1,1,1),(2,5,6,2),(3,2,4,2),(6,3,1,3)]

# Datapoints on axis x, y, z
x_data = zip(*Data)[0]
y_data = zip(*Data)[1]
z_data = zip(*Data)[2]
info_1 = zip(*Data)[3]

# set color of markers according to extra_infos

hsv = pylab.get_cmap('hsv') 
cNorm  = colors.Normalize(vmin=min(info_1), vmax=max(info_1))
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=hsv)
color = map(lambda x: scalarMap.to_rgba(x), info_1)

# set shape of markers according to extra_infos
type_adapter = {1: 3, 2: 2, 3: 1}
type_index = {1:"o", 2:"d", 3:"^"}

def get_shape(type_id):
	temp = type_adapter[type_id]
	return type_index[temp]

shape = map(get_shape, info_1)

# set plot properties
major_title = "test"
major_title_size = 25
xaxis_label = "This is x-axis"
yaxis_label = "This is y-axis"
zaxis_label = "This is z-axis"

animation_marker_opacity = 0.5	# set the transparency of markers
animation_elevation = 20.		# view angle rotation on z-axis
animation_length = 360			# set total animation frame
animation_fps = 30.				# set animation frame rate
animation_info_author = "Me"	# set metadata in the output movie
animation_filename = "output.mp4"

picture_elevation = 20.			# z axis rotation on pictures
picture_rotation = 45.			# x-y axis rotation on pictures
picture_filename = "output.png"

# clean plot area to create new plots
pylab.clf()
fig = pylab.figure(figsize=( 9, 9), dpi=96, facecolor='w')
fig.suptitle(major_title, fontsize = major_title_size)
fig.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9)

ax1 = fig.add_axes([0.2,0.2,0.6,0.6], projection='3d')
ax2 = fig.add_axes([0.02,0.02,0.96,0.6])
ax2.patch.set_facecolor('white')
ax2.patch.set_alpha(0.0)

def init():
	for i in range(len(x_data)):
		ax1.scatter(x_data[i], y_data[i], z_data[i], marker=shape[i], c=color[i], alpha=0.3,s=30)
	ax1.w_xaxis.line.set_color("red")
	ax1.w_yaxis.line.set_color("blue")
	ax1.w_zaxis.line.set_color("green")
	ax1.tick_params(axis='x', colors='red')
	ax1.tick_params(axis='y', colors='blue')
	ax1.tick_params(axis='z', colors='green')
	
	ax2.add_patch(Rectangle((0.1,0.05),0.05,0.05, facecolor="red"))
	ax2.text(0.2, 0.05, xaxis_label, fontsize=20)
	ax2.add_patch(Rectangle((0.1,0.12),0.05,0.05, facecolor="blue"))
	ax2.text(0.2, 0.12, yaxis_label, fontsize=20)
	ax2.add_patch(Rectangle((0.1,0.19),0.05,0.05, facecolor="green"))
	ax2.text(0.2, 0.19, zaxis_label, fontsize=20)
	for loc, spine in ax2.spines.items():
		spine.set_color('none')
	ax2.set_xticks([])
	ax2.set_yticks([])
	
def animate(i):
	ax1.view_init(elev=animation_elevation, azim=i)

# Animate
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=animation_length, interval=1000./animation_fps, blit=True)
# Save
# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=animation_fps, metadata=dict(artist=animation_info_author))

anim.save(animation_filename, writer=writer)

# save extra pictures
ax1.view_init(elev=30., azim=45)
pylab.savefig(picture_filename,dpi=300)

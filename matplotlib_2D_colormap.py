#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  matplotlib_2D_colormap.py
#  
#  Copyright 2014 Piece <piece@CCLoLab-No6>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pylab
import numpy as np

def main():
	title_main = "Example code for pylab colormap"
	label_x = [] # leave an empty list if no ticklabels
	label_xaxis = "Dataset X"
	label_y = []
	label_yaxis = "Dataset Y"
	label_colorbar = "What does color mean"
	filename = "name.txt"
	figure_name = "output_fig.png"
	
	f = open(filename)
	plot_data = [item.strip('\n').split(' ') for item in f.readlines()]
	f.close()
	
	max_value = max(np.array(plot_data).ravel())
	min_value = 0
		
	fig = pylab.figure(figsize=( 8, 5 ), dpi=96, facecolor='w')
	fig.suptitle(title_main, fontsize = 26)
	fig.subplots_adjust(left=0.15, bottom=0.1, right=0.95, top=0.9)
	
	ax = fig.add_axes([0.15, 0.05, 0.8, 0.7])

	dist = ax.imshow(	plot_data, vmin=min_value, vmax=max_value, 
						interpolation='none',aspect="auto")

	ax.set_xlabel(label_xaxis,fontsize=18)
	ax.set_ylabel(label_yaxis,fontsize=18)

	ax.xaxis.set_label_position('top')
	ax.xaxis.set_ticks_position('top')

	pylab.xticks(range(len(label_x)), label_x, fontsize=10)
	pylab.xlim(-0.5,len(label_x)-0.5)
	pylab.yticks(range(len(label_y)), label_y, fontsize=10)
	
	# horizontal colorbar
	cbar = fig.colorbar(dist, ticks=[0, max_value], orientation='horizontal')
	cbar.ax.set_xticklabels(['0', '%i'%max_value])
	fig.text(0.43,0.05, label_colorbar)

	for j in range(len(plot_data)):
		for i in range(len(plot_data[j])):
			fc = str(1.0 - plot_data[j][i]/max_value)
			ax.annotate("%i"%plot_data[j][i], (i-0.15, j), fontsize=10, color=fc, fontweight='heavy')
	
	pylab.savefig(figure_name,dpi=300)
	return 0

if __name__ == '__main__':
	main()


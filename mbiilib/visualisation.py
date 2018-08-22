import numpy as np
import matplotlib.pyplot as plt

def plot_gal_3d(ax, avec, centroid, pos, boxwidth=5, show_centroid=True):
	"""Takes a pylab axis, a position and a 3D shape and plots them in three dimensions"""

	# Draw in the connecting line
	ax.plot([centroid[0],pos[0]], [centroid[1],pos[1]], [centroid[2],pos[2]], ':', color='k')
	v = np.array([avec[0],avec[1],avec[2]])*0.6

	ax.plot([pos[0]], [pos[1]], [pos[2]], '.', color='purple')
	ax.plot([pos[0],pos[0]-v[0]], [pos[1],pos[1]-v[1]], [pos[2],pos[2]-v[2]], '-', color='k')

	if show_centroid:
		ax.plot([centroid[0]], [centroid[1]], [centroid[2]], 'x', color='g')
		ax.set_xlabel('x ', fontsize=16)
		ax.set_ylabel('y ', fontsize=16)
		ax.set_zlabel('z', fontsize=16)
		ax.set_zlim(centroid[2]-boxwidth, centroid[2]+boxwidth)
		ax.set_ylim(centroid[1]-boxwidth, centroid[1]+boxwidth)
		ax.set_xlim(centroid[0]-boxwidth, centroid[0]+boxwidth)

	return ax
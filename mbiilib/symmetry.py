import numpy as np

def sample_sphere(npoints, norm=1, seed=None):
    """Generates random points on a sphere of radius R"""
    if (seed!=None):
        np.random.seed(seed)
    u1 = np.random.rand(npoints)
    u2 = np.random.rand(npoints)

    # Define a vector position
    theta = np.arccos(2*u1-1)
    phi = 2 * np.pi * u2

    x = np.sin(theta)*np.cos(phi)
    y = np.sin(theta)*np.sin(phi)
    z = np.cos(theta)
    vec= np.array([x,y,z])
    vec *= norm

    return vec

def infer_rotation_angle(position0, position):
    """Work out two rotation angles that will transform one given 
    3D vector into another."""

    # Work out the unit vector orthogonal to the plane defined by the two position vectors
    rotation_axis = np.cross(position0, position)
    rotation_axis /= get_norm(rotation_axis)

    # Then calculate the angle between the two position vectors in the 2D plane defined by them
    alpha = np.arccos( np.dot(position/get_norm(position), position0/get_norm(position0)) )
    cross = np.cross(position, position0);

    #alpha = -alpha

    return rotation_axis, alpha



def build_rotation_matrix(theta=None, phi=None, alpha=None, vec=[]):
    """Generates a random rotation matrix, 
    which transforms a given 3D position vector to a random position on the sphere.
    Usage : rotated = R.unrotated"""
    u1 = np.random.rand()
    u2 = np.random.rand()

    # Use two random values from a uniform distribution to generate an axis about which to rotate
    if phi==None:
        phi = np.arccos(2*u1-1)
    if theta==None:
        theta = 2 * np.pi * u2

    # Work out a Cartesian unit vector defined by the rotation axis 
    if (len(vec)==0):
        x = np.sin(theta)*np.cos(phi)
        y = np.sin(theta)*np.sin(phi)
        z = np.cos(theta)
        vec= np.array([x,y,z])
    vec/=get_norm(vec)

    # Now generate a random rotation angle about that axis
    if alpha==None:
        alpha = np.random.rand() * 2 * np.pi
    cosa = np.cos(alpha)
    sina = np.sin(alpha)
    ux = vec[0]
    uy = vec[1]
    uz = vec[2]

    # Construct the 3x3 rotation matrix
    R = np.array([ [ (cosa + ux*ux*(1-cosa)), (ux*uy*(1-cosa) - uz*sina), (ux*uz*(1-cosa) + uy*sina)],
    [uy*ux*(1-cosa) + uz*sina, cosa + uy*uy*(1-cosa), uy*uz*(1-cosa) - ux*sina],
    [uz*ux*(1-cosa) - uy*sina, uz*uy*(1-cosa) + ux*sina, cosa + uz*uz*(1-cosa) ]] )

    return R

def get_norm(vec):
    return np.sqrt(sum([v*v for v in vec])) 

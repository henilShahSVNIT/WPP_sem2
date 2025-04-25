'''Take N (N >= 10) random 2-dimensional points represented in cartesian 
coordinate space. 
Store them in a numpy array. Convert them to polar coordinates.''' 
 
import numpy as np 
 
N = int(input("Enter number of points : ")) 
 
points = np.random.rand(N, 2) * 10 
 
x = points[:, 0] 
y = points[:, 1] 
 
r = np.sqrt(x**2 + y**2) 
theta = np.arctan2(y, x) 
 
polar_points = np.column_stack((r, theta)) 
 
print("Cartesian Coordinates:\n", points) 
print("Polar Coordinates:\n", polar_points) 
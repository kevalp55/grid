import lidar_to_grid_map as lg
map1 = np.ones((50, 50)) * 0.5
line = lg.bresenham((2, 2), (40, 30))
for l in line:
    map1[l[0]][l[1]] = 1
plt.imshow(map1)
plt.colorbar()
plt.show()
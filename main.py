import numpy as np

# Y-chromosome genotypes and their frequencies in the three populations (Icelandic, Nordic, and Irish)
y = np.array([[1, 1, 1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0, 0, 0],
              [1, 1, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 1, 1]])
freq_y = np.array([[0.41, 0.26, 0.82],
                   [0.34, 0.51, 0.15],
                   [0.23,0.18,0],
                   [0.01,0.03,0.42]])

# Mitochondrial genotypes and theif frequencies in the three populations (Icelandic, Nordic, and Irish)
m = np.array([[1,1,1,0,1,0,0,0],
              [0,0,1,1,0,1,0,0],
              [0,0,1,1,1,1,1,0],
              [0,0,0,0,1,0,0,1],
              [1,0,0,0,0,1,0,0]])
freq_m = np.array([[0.6, 0.29, 0.7],
                   [0.14, 0.52, 0.21],
                   [0.40,0.04,0.35],
                   [0.04,0.65,0.03],
                   [0.08,0.16,0.07]])

# Calculate average y-chromosome and mitochondrial genotypes for each population
avg_y =[]
avg_m =[]
for i in range(3):
    avg_y.append(freq_y[0,i]*y[0,:]+freq_y[1,i]*y[1,:]+freq_y[2,i]*y[2,:]+freq_y[3,i]*y[3,:])
    avg_m.append(freq_m[0,i]*m[0,:]+freq_m[1,i]*m[1,:]+freq_m[2,i]*m[2,:]+freq_m[3,i]*m[3,:]+freq_m[4,i]*m[4,:])
avg_y = np.array(avg_y)
avg_m = np.array(avg_m)

# Generate the two distance matrices
map_y = np.zeros((3,3))
map_m = np.zeros((3,3))
for i in range(3):
    for j in range(3):
        map_y[i,j]= np.sqrt(np.sum((avg_y[i,:]-avg_y[j,:])**2))
        map_m[i,j]= np.sqrt(np.sum((avg_m[i,:]-avg_m[j,:])**2))

print(avg_y)
print(avg_m)

import matplotlib.pyplot as plt
plt.imshow(map_y)
plt.colorbar()
plt.savefig("map_y.png")
plt.imshow(map_m)
plt.savefig("map_m.png")
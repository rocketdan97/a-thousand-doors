import numpy as np

doors = np.zeros(1000, dtype=int)
door_flips = np.zeros(1000, dtype=int)

door_dict = {0:'closed', 1: 'open'}

def count_open(arr):
    count = 0
    for i in range(len(arr)):
        if(arr[i] == 1):
            count = count + 1
    return count

for i in range(1,1001):
    for k in range(i,1000,i):
        doors[k] = (doors[k] + 1) % 2
        door_flips[k] = door_flips[k] + 1

f = open('doors.txt','w')

for i in range(1000):
    f.write('door ' + str(i) + ' is ' + door_dict[doors[i]] +\
    ' after ' + str(door_flips[i]) + ' door flips\n') 

doors = [0] * 100
for x in range (1,101):
    for y in range (x-1,100,x):
        if doors[y]== 0:
            doors[y] = 1
        elif doors[y]==1:
            doors[y] = 0
opendoors = []
for i, value in enumerate(doors):
    if value == 1:
            opendoors.append(i+1)
print('The following doors are open: ', opendoors)

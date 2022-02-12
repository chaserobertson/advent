#!/usr/bin/python3

input = []
with open('17/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

def printgrid(grid, dims):
    for h in range(dims[0][0], dims[0][1]+1):
        for i in range(dims[1][0], dims[1][1]+1):
            out = 'z=%d, w=%d' % (h, i)
            for j in range(dims[2][0], dims[2][1]+1):
                out += '\n'+str(j) 
                for k in range(dims[3][0], dims[3][1]+1):
                    out += grid['%d,%d,%d' % (i,j,k)]
        print(out)
        print()

def cycle(grid, dims):
    new_grid = {}
    dim_ranges = [range(dims[x][0]-1, dims[x][1]+2) for x in range(4)]
    for h in dim_ranges[0]:
        for i in dim_ranges[1]:
            for j in dim_ranges[2]:
                for k in dim_ranges[3]:
                    key = '%d,%d,%d,%d' % (h,i,j,k)
                    neighbors = [
                        '%d,%d,%d,%d' % (w,x,y,z) 
                        for w in range(h-1, h+2)
                        for x in range(i-1, i+2) 
                        for y in range(j-1, j+2)
                        for z in range(k-1, k+2)]
                    active_neighbors = 0
                    for n in neighbors:
                        if n in grid.keys() and grid[n] == '#' and n != key:
                            active_neighbors += 1
                    if key in grid.keys() and grid[key] == '#':
                        if active_neighbors in {2, 3}:
                            new_grid.setdefault(key, '#')
                            #print(key, 'is', '#', 'has', active_neighbors, 'gets', '#')
                        else:
                            #print(key, 'is', '#', 'has', active_neighbors, 'gets', '.')
                            new_grid.setdefault(key, '.')
                    else:
                        if active_neighbors == 3:
                            #print(key, 'is', '.', 'has', active_neighbors, 'gets', '#')
                            new_grid.setdefault(key, '#')
                        else:
                            #print(key, 'is', '.', 'has', active_neighbors, 'gets', '.')
                            new_grid.setdefault(key, '.')

    new_dims = dims.copy()
    for key, val in new_grid.items():
        if val == '.' and key not in grid.keys():
            continue
        d = key.split(',')
        for i in range(4):
            d_i = int(d[i])
            if d_i < new_dims[i][0]:
                new_dims[i][0] = d_i
            if d_i > new_dims[i][1]:
                new_dims[i][1] = d_i
    return new_grid, new_dims

grid = {}
grid_dims = [
    [0, 0],
    [0, 0],
    [0, len(input)],
    [0, len(input)]]
for i in range(0, len(input)):
    for j in range(0, len(input)):
        grid.setdefault('0,0,%d,%d' % (i, j), input[i][j])

#print('Before any cycles:\n')
#printgrid(grid, grid_dims)

cycles = 6
for c in range(cycles):
    grid, grid_dims = cycle(grid, grid_dims)
    #print('After %d cycle(s):\n' % (c+1))
    #printgrid(grid, grid_dims)

active = 0
for val in grid.values():
    active += int(val == '#')
print(active)
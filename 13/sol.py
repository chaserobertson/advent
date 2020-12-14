import pathlib

in_file = pathlib.Path.cwd().joinpath('13', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

time = int(lines[0].strip())
all_buses = lines[1].strip().split(',')

print('part 1')
buses = [int(bus) for bus in all_buses if bus != 'x']
wait_times = [bus - (time % bus) for bus in buses]
min_time = min(wait_times)
bus_index = wait_times.index(min_time)
bus_id = buses[bus_index]
result = bus_id * min_time
print(wait_times)
print(result)

print('part 2')
bus_list = [int(bus) if bus != 'x' else 'x' for bus in all_buses]

time = 1
step = 1
for bus in buses:
    offset = bus_list.index(bus)
    while (time + offset) % bus != 0:
        time += step
    step *= bus
print(time)

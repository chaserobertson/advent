#!/usr/bin/julia

f = open("2019/03/input.txt", "r")
inputs = [line for line in readlines(f)]
close(f)

#println(inputs)

function manhattan(c1, c2)
    return abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
end

function manhattan_from_zero(c)
    return abs(c[1]) + abs(c[2])
end

function collision(a, b, x, y)
    collide = false
    # ab horizontal and xy vertical
    if a[2] == b[2] && x[1] == y[1]
        #println("ab horizontal and xy vertical")
        min_x = min(a[1], b[1])
        max_x = max(a[1], b[1])
        min_y = min(x[2], y[2])
        max_y = max(x[2], y[2])
        if min_x < x[1] < max_x && min_y < a[2] < max_y
            collide = true
        end
    # ab vertical and xy horizontal
    elseif a[1] == b[1] && x[2] == y[2]
        #println("ab vertical and xy horizontal")
        min_x = min(x[1], y[1])
        max_x = max(x[1], y[1])
        min_y = min(a[2], b[2])
        max_y = max(a[2], b[2])
        if min_x < a[1] < max_x && min_y < x[2] < max_y
            collide = true
        end
    end
    return collide
end

function get_col_coords(a, b, x, y)
    # if ab horizontal and xy vertical
    if a[2] == b[2] && x[1] == y[1]
        return [x[1], a[2]]
    # if ab vertical and xy horizontal
    elseif a[1] == b[1] && x[2] == y[2]
        return[a[1], x[2]]
    end
end

function get_min_dist(coords)
    min_dist = typemax(Int)
    for c in coords
        m = manhattan_from_zero(c)
        if m < min_dist
            min_dist = m
        end
    end
    return min_dist
end

function find_col_coords(wire_points)
    collision_coords = []
    for z in collect(2:length(wire_points))
        w1 = wire_points[z-1]
        w2 = wire_points[z]
        for i in collect(2:length(w1))
            w1_1 = w1[i-1]
            w1_2 = w1[i]
            for j in collect(2:length(w2))
                w2_1 = w2[j-1]
                w2_2 = w2[j]
                #println(w1_1, ",", w1_2, " vs ", w2_1, ",", w2_2)
                if collision(w1_1, w1_2, w2_1, w2_2)
                    colcords = get_col_coords(w1_1, w1_2, w2_1, w2_2)
                    #println("Collide! At the disco ", colcords, ": ", w1_1, ",", w1_2, " ", w2_1, ",", w2_2)
                    push!(collision_coords, colcords)
                end
            end
        end
    end
    return collision_coords
end

function get_wire_points(inputs)
    wire_points = [[[0, 0]] for x in inputs]
    for i in eachindex(inputs)
        x, y = 0, 0
        for move in split(inputs[i], ",")
            dir = first(move)
            dist = parse(Int, move[2:end])
            if dir == 'D'
                y -= dist
            elseif dir == 'U'
                y += dist
            elseif dir == 'R'
                x += dist
            elseif dir == 'L'
                x -= dist
            end
            push!(wire_points[i], [x, y])
        end
    end
    return wire_points
end

function get_delays(wire_points, collision_coords)
    delays = []
    for wire in wire_points
        wire_delays = [typemax(Int) for x in collision_coords]
        wire_steps = 0
        position = [0,0]
        for i in eachindex(wire)[2:end]
            dest = wire[i]
            for z in collect(1:manhattan(position, dest))
                if position in collision_coords
                    # check for known number of steps
                    ind = findfirst(isequal(position), collision_coords)
                    if wire_steps < wire_delays[ind]
                        wire_delays[ind] = wire_steps
                    end
                end

                if position == dest
                    # destination reached
                    println(position, " reached, steps=", wire_steps+1)
                elseif position[1] == dest[1]
                    # moving in y dir
                    if position[2] < dest[2]
                        position[2] += 1
                    elseif position[2] > dest[2]
                        position[2] -= 1
                    else
                        println("pos = dest check broken")
                    end
                elseif position[2] == dest[2]
                    # moving in x dir
                    if position[1] < dest[1]
                        position[1] += 1
                    elseif position[1] > dest[1]
                        position[1] -= 1
                    else
                        println("pos = dest check broken v2")
                    end
                else
                    println("uh on spaghetti o no no no")
                end
                wire_steps += 1
            end
        end
        #println(wire_steps)
        push!(delays, wire_delays)
    end
    return delays
end

function get_min_delay(delays)
    combined = delays[1] + delays[2]
    return min(combined...)
end

wire_points = get_wire_points(inputs)

#println(wire_points)

collision_coords = find_col_coords(wire_points)
#println(collision_coords)

println("Min manhattan distance: ", get_min_dist(collision_coords))

d = get_delays(wire_points, collision_coords)
#println(d)

println("Min delay distance: ", get_min_delay(d))
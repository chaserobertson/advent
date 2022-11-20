#!/usr/bin/julia

f = open("2019/06/input.txt", "r")
inputs = [line for line in readlines(f)]
close(f)

#println(inputs)

orbitees = Set()
orbiters = Set()
orbits = Dict()
for str in inputs
    orb = split(str, ")")
    if haskey(orbits, orb[1])
        push!(orbits[orb[1]], orb[2])
    else
        orbits[orb[1]] = [orb[2]]
    end
    push!(orbitees, orb[1])
    push!(orbiters, orb[2])
end

objects = union(orbitees, orbiters)
orbitcounts = Dict(x => 0 for x in objects)

centers = collect(setdiff(orbitees, orbiters))

while length(centers) > 0
    center = pop!(centers)
    local_orbiters = get(orbits, center, [])
    for orb in local_orbiters
        orbitcounts[orb] += orbitcounts[center] + 1
        push!(centers, orb)
    end
end

println(sum(values(orbitcounts)))

#pt 2

orbits = Dict()
for str in inputs
    orb = split(str, ")")
    orbits[orb[2]] = orb[1]
end

my_orbits = Dict("YOU" => [], "SAN" => [])
for k in keys(my_orbits)
    local here = k
    while haskey(orbits, here)
        here = orbits[here]
        push!(my_orbits[k], here)
    end
end

join = first(intersect(values(my_orbits)...))

println(sum(findfirst.(x->x==join, values(my_orbits)))-2)


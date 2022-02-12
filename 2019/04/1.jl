#!/usr/bin/julia

f = open("2019/04/test.txt", "r")
inputs = [line for line in readlines(f)]
close(f)

println(inputs)

minmax = [parse(Int, x) for x in split(inputs[1], "-")]

pfirst = []
for x in collect(first(minmax):last(minmax))
    s = string(x)
    c = collect(s)
    if c == sort(c)
        push!(pfirst, s)
    end
end

println(length(pfirst))

psecond = []
for s in pfirst
    for c in s
        if count(isequal(c), s) == 2
            push!(psecond, s)
            break
        end
    end
end

println(length(psecond))

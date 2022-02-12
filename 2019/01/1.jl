f = open("2019/01/input.txt", "r")
inlines = [parse(Int, x) for x in readlines(f)]
close(f)

outlines = [[(x÷3)-2] for x in inlines]

while true
    going = false
    for l in outlines
        fuel = (last(l)÷3)-2
        if fuel > 0
            #println(fuel)
            push!(l, fuel)
            going = true
        end
    end
    if !going
        break
    end
end

println(sum([sum(l) for l in outlines]))
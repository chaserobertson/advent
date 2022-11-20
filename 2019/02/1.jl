#!/usr/bin/julia

using DelimitedFiles

inputs = readdlm("2019/02/test.txt", ',', Int)

inputs[2] = 12
inputs[3] = 2
println(inputs)

for i in eachindex(inputs)
    if i % 4 == 1
        op, i1, i2, i3 = inputs[i:i+3]
        if op == 1
            inputs[i3+1] = inputs[i1+1] + inputs[i2+1]
        elseif op == 2
            inputs[i3+1] = inputs[i1+1] * inputs[i2+1]
        elseif op == 99
            break
        end
    end
end

println(inputs)
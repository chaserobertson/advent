#!/usr/bin/julia

using DelimitedFiles

inputs = readdlm("2019/02/input.txt", ',', Int)

for x in collect(0:99)
    for y in collect(0:99)
        outputs = copy(inputs)
        outputs[2] = x
        outputs[3] = y
        for i in eachindex(outputs)
            if i % 4 == 1
                op, i1, i2, i3 = outputs[i:i+3]
                if op == 1
                    outputs[i3+1] = outputs[i1+1] + outputs[i2+1]
                elseif op == 2
                    outputs[i3+1] = outputs[i1+1] * outputs[i2+1]
                elseif op == 99
                    break
                end
            end
        end
        if first(outputs) == 19690720
            println(x, " ", y)
            println((100*x)+y)
            return
        end
    end
end

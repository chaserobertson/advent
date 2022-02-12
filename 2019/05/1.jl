#!/usr/bin/julia

using DelimitedFiles

function ind(i)
    return i+1
end

function intcode(program)
    i = 1
    while i <= length(program)
        op, i1 = program[i:i+1]

        if op == 1 || op == 2
            i2, i3 = program[i+2:i+3]
            if op == 1
                program[i3+1] = program[i1+1] + program[i2+1]
            elseif op == 2
                program[i3+1] = program[i1+1] * program[i2+1]
            end
            i += 2
        elseif op == 3
            program[i1+1] = 0 # defined as input
        elseif op == 4
            println(program[ind(i1)]) # ouput
        elseif op == 99
            i = length(program) + 1
        end
        i += 2
    end

    println(program)
end

inputs = readdlm("2019/05/test.txt", ',', Int)

intcode(inputs)

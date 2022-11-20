#!/usr/bin/julia

using DelimitedFiles

inputs = readdlm("2019/05/input.txt", ',', Int)
in_val = 5

function intcode(program)
    local i = 1
    while i <= length(program)
        instruction = program[i]
        op = mod(instruction, 10)

        # three-param operations
        if op in [1, 2, 7, 8]
            i1, i2, i3 = program[i+1:i+3]
            p1 = mod(instruction÷100,10)==1 ? i1 : program[i1+1]
            p2 = mod(instruction÷1000,10)==1 ? i2 : program[i2+1]
            if op == 1
                program[i3+1] = p1 + p2
                println(p1, "+", p2, " to ", i3)
            elseif op == 2
                program[i3+1] = p1 * p2
                println(p1, "*", p2, " to ", i3)
            elseif op == 7
                program[i3+1] = p1 < p2 ? 1 : 0
                println(p1, "<", p2, " to ", i3)
            elseif op == 8
                program[i3+1] = p1 == p2 ? 1 : 0
                println(p1, "==", p2, " to ", i3)
            end
            i += 4
        # one-param operations
        elseif op in [3, 4]
            i1 = program[i+1]
            p1 = mod(instruction÷100,10)==1 ? i1 : program[i1+1]
            if op == 3
                program[i1+1] = in_val
                println(in_val, " to ", i1)
            elseif op == 4
                toss = i1 + p1
                println("Output ", p1)
            end
            i += 2
        # two-param operations
        elseif op in [5, 6]
            i1, i2 = program[i+1:i+2]
            p1 = mod(instruction÷100,10)==1 ? i1 : program[i1+1]
            p2 = mod(instruction÷1000,10)==1 ? i2 : program[i2+1]
            i_ = i
            i += 3
            if op == 5 && p1 != 0 i = p2+1 end
            if op == 6 && p1 == 0 i = p2+1 end
            println("instptr from ", i_, ":", program[i_], " to ", i, ":", program[i])
        # no-param operations
        elseif op == 99
            println("end")
            break
        end
    end
    println(program)
end

intcode(inputs)
println("end")

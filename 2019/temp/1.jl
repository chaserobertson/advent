#!/usr/bin/julia

f = open("2019/02/test.txt", "r")
inputs = [line for line in readlines(f)]
close(f)

println(inputs)
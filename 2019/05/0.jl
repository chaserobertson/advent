#!/usr/bin/julia

f = open("2019/05/test.txt", "r")
inputs = [line for line in readlines(f)]
close(f)

println(inputs)
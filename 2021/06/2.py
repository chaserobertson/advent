#!/usr/bin/python3

input = []
with open('06/input.txt', 'r') as f:
    for line in f.readlines():
        for c in line.strip().split(','):
            input.append(int(c))

num_days = 256
cycle_days = 7
adolescence_days = 2

cohorts = [0 for x in range(0, cycle_days)]
for age in input:
    cohorts[age] += 1
adolescents = [0 for x in range(0, adolescence_days)]

for day in range(0, num_days):
    offset = day % cycle_days
    ad_cohort = day % adolescence_days
    birthed = cohorts[offset]
    cohorts[offset] += adolescents[ad_cohort]
    adolescents[ad_cohort] = birthed

print(sum(cohorts) + sum(adolescents))

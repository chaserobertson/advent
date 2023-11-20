#!/usr/bin/python3

import numpy as np

input = []
with open('2022/16/test.txt', 'r') as f:
    input = f.read().splitlines()

valve_dict = {}
for line in input:
    words = line.split()
    name = words[1]
    rate = int(words[4].split('=')[1][:-1])
    leads_to = [w.replace(',', '') for w in words[9:]]
    valve_dict[name] = (rate, leads_to)

valve_index = sorted(valve_dict.keys())
N = len(valve_index)

# Adjacency matrix
adj = np.ones((N, N), int) * np.inf
for i in range(N):
    adj[i, i] = 0
    for link in valve_dict[valve_index[i]][1]:
        adj[i, valve_index.index(link)] = 1

# Floyd-Warshall to compute distance matrix
dists = np.copy(adj)
for k in range(N):
    for i in range(N):
        for j in range(N):
            if dists[i, j] > dists[i, k] + dists[k, j]:
                dists[i, j] = dists[i, k] + dists[k, j]
#print(dists)

rates = [v[0] for v in valve_dict.values()]
#print(rates)

moves = []
def move(current, minute, rates, dists):
    if minute < 1 or sum(rates) == 0:
        return ([valve_index[current]], 0)
    expected_minute = minute - dists - 1
    expected_pressure = (rates * expected_minute)[current]
    bests = np.argsort(expected_pressure).tolist()
    best_nek = ([valve_index[current]], 0)
    for i in range(-1, -3, -1):
        best = bests[i]
        nek_minute = expected_minute[current, best]
        pressure = expected_pressure[best]
        print(f'Go to {valve_index[best]} for {pressure}')
        rates = np.copy(rates)
        rates[best] = 0
        nek_move = move(best, nek_minute, rates, dists)
        if nek_move[1] > best_nek[1]:
            best_nek = nek_move
    print()
    return (
        [valve_index[current]] + best_nek[0], 
        expected_pressure[valve_index.index(best_nek[0][-1])] + best_nek[1]
        )

print(move(0, 30, rates, dists))

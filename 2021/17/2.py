def launch(vx, vy, xl, xr, y1, y2):
    # y1, y2 denote depth below the surface
    x, y = 0, 0
    zone_reached, highest = 0, 0
    while y >= -y2 and x <= xr:
        highest = max(highest, y)
        if xl <= x <= xr and -y2 <= y <= -y1:
            zone_reached = 1

        x, y = x + vx, y + vy
        vy -= 1
        vx += 1 if vx < 0 else (-1 if vx > 0 else 0)

    return (zone_reached, highest)


def main():
    xl, xr = 235, 259
    y1, y2 = 62, 118

    besty, total = 0, 0
    for vx in range(xr + 1):
        for vy in range(-200, 200):
            reached, y = launch(vx, vy, xl, xr, y1, y2)
            total += reached
            if reached:
                besty = max(besty, y)

    print(total, besty)

main()
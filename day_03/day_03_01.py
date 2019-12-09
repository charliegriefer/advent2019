from typing import List

from shapely.geometry import LineString, MultiPoint


def main():
    with open("day_03.txt") as f:
        wires = f.readlines()

    wire_1 = LineString(get_coords(wires[0]))
    wire_2 = LineString(get_coords(wires[1]))

    intersections = wire_1.intersection(wire_2)
    closest_intersection = manhattan_distance(intersections)
    print(int(closest_intersection[0]))


def get_coords(wire_list):
    coords = [(0, 0)]
    for w in wire_list.split(","):
        direction = w[0]
        distance = int(w[1:])
        last = coords[-1]
        if direction == "R":
            coords.append((last[0] + distance, last[1]))
        elif direction == "L":
            coords.append((last[0] - distance, last[1]))
        elif direction == "U":
            coords.append((last[0], last[1] + distance))
        else:
            coords.append((last[0], last[1] - distance))
    return coords[1:]


def manhattan_distance(intersections: MultiPoint) -> List:
    manhattans = [abs(i.x) + abs(i.y) for i in intersections]
    return sorted(manhattans)


if __name__ == "__main__":
    main()

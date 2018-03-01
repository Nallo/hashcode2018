#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vehicle(object):
    def __init__(self, id):
        self.id = id
        self.time = 0
        self.position = (0,0)
        self.trips = []


def waiting_time(vehicle_time, earliest_start):
    return max(0, earliest_start-vehicle_time)


def travel_time(p0, p1):
    return abs( (p0[0]-p1[0]) + ((p0[1]-p1[1])) )


def print_sol(vehicles):
    for vehicle in sorted(vehicles, key=lambda x: x.id):
        print("{} {}".format(len(vehicle.trips), " ".join(map(str, vehicle.trips))))

    return


def solve(R, C, F, N, B, T):
    vehicles = [Vehicle(idx) for idx in range(F)]

    for ride_idx in range(N):
        vehicles.sort(key=lambda x: x.time)

        r_start, c_start, r_goal, c_goal, earliest_start, latest_finish = map(int, raw_input().split(' '))
        p_start = (r_start, c_start)
        p_goal = (r_goal, c_goal)

        time = waiting_time(vehicles[0].time, earliest_start)
        time += travel_time(vehicles[0].position, p_start)
        time += travel_time(p_start, p_goal)

        if vehicles[0].time + time > T:
            continue

        vehicles[0].time += time
        vehicles[0].position = p_goal
        vehicles[0].trips.append(ride_idx)

    print_sol(vehicles)
    return


def main():
    R, C, F, N, B, T = map(int, raw_input().split(' '))
    solve(R, C, F, N, B, T)
    return 0


if __name__ == "__main__":
    main()

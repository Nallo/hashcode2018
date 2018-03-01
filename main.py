#!/usr/bin/env python
# -*- coding: utf-8 -*-

def waiting_time(vehicle_time, earliest_start):
    return max(0, earliest_start-vehicle_time)


def travel_time(p0, p1):
    return abs( (p0[0]-p1[0]) + ((p0[1]-p1[1])) )


def print_sol(vehicle_trips):
    for trips in vehicle_trips:
        print("{} {}".format(len(trips), " ".join(map(str, trips))))
    return


def solve(R, C, F, N, B, T):
    vehicle_idx = 0
    vehicle_time = 0
    vehicle_position = (0,0)
    vehicle_trips = [[] for _ in range(F)]

    for ride_idx in range(N):
        if vehicle_idx >= F: break

        r_start, c_start, r_goal, c_goal, earliest_start, latest_finish = map(int, raw_input().split(' '))
        p_start = (r_start, c_start)
        p_goal = (r_goal, c_goal)

        time = waiting_time(vehicle_time, earliest_start)
        time += travel_time(vehicle_position, p_start)
        time += travel_time(p_start, p_goal)

        if vehicle_time + time > T:
            vehicle_idx += 1
            vehicle_time = 0
            vehicle_position = (0,0)

        if vehicle_idx < F:
            vehicle_time += time
            vehicle_position = p_goal
            vehicle_trips[vehicle_idx].append(ride_idx)

    print_sol(vehicle_trips)
    return


def main():
    R, C, F, N, B, T = map(int, raw_input().split(' '))
    solve(R, C, F, N, B, T)
    return 0


if __name__ == "__main__":
    main()

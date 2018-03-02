#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Vehicle(object):
    def __init__(self, id):
        self.id = id
        self.time = 0
        self.position = (0,0)
        self.trips = []


class Ride(object):
    def __init__(self, id):
        self.id = id
        self.p_start = (0,0)
        self.p_goal = (0,0)
        self.earliest_start = 0
        self.latest_finish = 0


def waiting_time(vehicle_time, earliest_start):
    return max(0, earliest_start-vehicle_time)


def travel_time(p0, p1):
    return abs( (p0[0]-p1[0]) + ((p0[1]-p1[1])) )


def print_sol(vehicles):
    for vehicle in sorted(vehicles, key=lambda x: x.id):
        print("{} {}".format(len(vehicle.trips), " ".join(map(str, vehicle.trips))))

    return


def ride_sorting(a, b):
    if a.latest_finish == b.latest_finish:
        return travel_time(b.p_start, b.p_goal) - travel_time(a.p_start, a.p_goal)
    else:
        return a.latest_finish - b.latest_finish


def solve(R, C, F, N, B, T):
    rides = []
    vehicles = [Vehicle(idx) for idx in range(F)]

    for ride_idx in range(N):
        r_start, c_start, r_goal, c_goal, earliest_start, latest_finish = map(int, raw_input().split(' '))
        p_start = (r_start, c_start)
        p_goal = (r_goal, c_goal)

        ride = Ride(ride_idx)
        ride.p_start = p_start
        ride.p_goal = p_goal
        ride.earliest_start = earliest_start
        ride.latest_finish = latest_finish
        rides.append(ride)

    for ride in sorted(rides, cmp=ride_sorting):
        vehicles.sort(key=lambda x: x.time)

        time = waiting_time(vehicles[0].time, ride.earliest_start)
        time += travel_time(vehicles[0].position, ride.p_start)
        time += travel_time(ride.p_start, ride.p_goal)

        if vehicles[0].time + time > T:
            continue

        vehicles[0].time += time
        vehicles[0].position = p_goal
        vehicles[0].trips.append(ride.id)

    print_sol(vehicles)
    return


def main():
    R, C, F, N, B, T = map(int, raw_input().split(' '))
    solve(R, C, F, N, B, T)
    return 0


if __name__ == "__main__":
    main()

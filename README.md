# Google Hash Code 2018
## Qualification Round - Problem Solution

This repository contains the problem solution to the Google Hash Code 2018
Qualification Round.

File `main.py` contains the script used to generate the `*.out` files based on
the `*.in` files.

## Algorithm Description

The algorithm goes through the list of rides one by one and tries to assign the
i-th ride to the j-th vehicle. In case the vehicle has no more time available for
a ride, the algorithm skip to the next vehicle and continue the assignment.

### The score of this solution is: **12,068,394**

## Further Improvements

  * Sort the rides by `latest_finish` and assign it to the i-th vehicle.
  * Sort the rides by `latest_finish` and assign it to the least busy vehicle.
  * Sort the rides by `(latest_finish, ride_tot_time)`  and assign it to the
    least busy vehicle.

## Contributors

  * [Stefano Martinallo](https://github.com/nallo)
  * [Lorenzo Dibenedetto](https://www.facebook.com/cielodipintodiblu)
  * [Alessandro Giordano](https://www.facebook.com/deimos2346)
  * [Achilles Tzimis](https://www.facebook.com/achilles.tzimis)

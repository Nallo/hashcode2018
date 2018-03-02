# Google Hash Code 2018
## Qualification Round - Problem Solution

This repository contains the problem solution to the Google Hash Code 2018
Qualification Round.

File `main.py` contains the script used to generate the `*.out` files based on
the `*.in` files.

## Algorithm Description

The algorithm sorts the rides using smallest `latest_finish` key and longest ride
distance then, it goes through the list of rides one by one and tries to assign the
i-th ride to the least busy vehicle. In case the vehicle has no more time available for
a ride, the algorithm skips to the next vehicle and continue the assignment.

### The score of this solution is: **29,318,902**

## Further Improvements

  * Sort the rides by `(latest_finish, ride_tot_time)`  and assign it to the
    least busy vehicle.

## Contributors

  * [Stefano Martinallo](https://github.com/nallo)
  * [Lorenzo Dibenedetto](https://www.facebook.com/cielodipintodiblu)
  * [Alessandro Giordano](https://www.facebook.com/deimos2346)
  * [Achilles Tzimis](https://www.facebook.com/achilles.tzimis)

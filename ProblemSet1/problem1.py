"""Problem Set 1, Problem 1: Greedy Cow Transport.

One way of transporting cows is to always pick the heaviest cow that will fit onto the spaceship first. This is an
example of a greedy algorithm. So if there are only 2 tons of free space on your spaceship, with one cow that's 3 tons
and another that's 1 ton, the 1 ton cow will get put onto the spaceship.

Implement a greedy algorithm for transporting the cows back across space in the function greedy_cow_transport. The
function returns a list of lists, where each inner list represents a trip and contains the names of cows taken on that
trip.

Note: Make sure not to mutate the dictionary of cows that is passed in!

Assumptions:
  - The order of the list of trips does not matter. That is, [[1,2],[3,4]] and [[3,4],[1,2]] are considered equivalent
    lists of trips.
  - All the cows are between 0 and 100 tons in weight.
  - All the cows have unique names.
  - If multiple cows weigh the same amount, break ties arbitrarily.
  - The spaceship has a cargo weight limit (in tons), which is passed into the function as a parameter.

Example:
  Suppose the spaceship has a weight limit of 10 tons and the set of cows to transport is
  {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}.

The greedy algorithm will first pick Jesse as the heaviest cow for the first trip. There is still space for 4 tons on
the trip. Since Maggie will not fit on this trip, the greedy algorithm picks Maybel, the heaviest cow that will still
fit. Now there is only 1 ton of space left, and none of the cows can fit in that space, so the first trip is
[Jesse, Maybel].

For the second trip, the greedy algorithm first picks Maggie as the heaviest remaining cow, and then picks Callie as
the last cow. Since they will both fit, this makes the second trip [[Maggie], [Callie]].

The final result then is [["Jesse", "Maybel"], ["Maggie", "Callie"]].
"""


# pylint: disable=C0200
def sort_dict(dict_to_sort):
    """Auxillary function for greedy_cow_transport()."""
    list_of_keys = list(dict_to_sort.keys())
    list_of_values = list(dict_to_sort.values())

    for i in range(len(list_of_values)):
        for j in range(len(list_of_values)):
            if list_of_values[j] < list_of_values[i]:
                list_of_values[i], list_of_values[j] = list_of_values[j], list_of_values[i]
                list_of_keys[i], list_of_keys[j] = list_of_keys[j], list_of_keys[i]

    return list_of_keys, list_of_values


# pylint: disable=C0200
def greedy_cow_transport(cows, limit=10):
    """Return the trips.

    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Args:
        cows (dict): a dictionary of name (string), weight (int) pairs
        limit (int, optional): weight limit of the spaceship, defualts to 10


    Returns:
        list: A list of lists, with each inner list containing the names of cows transported on a particular trip and
        the overall list containing all the trips
    """
    list_of_trips = []
    list_of_keys, list_of_values = sort_dict(cows.copy())

    for _ in range(len(cows)):
        total_weight_of_the_trip = 0
        trip = []

        loop_variable = True
        while loop_variable:
            key = 0
            for i in range(len(list_of_keys)):
                if list_of_values[i] == max(list_of_values) and list_of_values[i] + total_weight_of_the_trip <= limit:
                    key = i
                    break

                if list_of_values[i] + total_weight_of_the_trip <= limit:
                    if list_of_values[i] < list_of_values[key]:
                        key = i
                        break

            trip.append(list_of_keys[key])
            total_weight_of_the_trip += list_of_values[key]
            list_of_keys.pop(key)
            list_of_values.pop(key)

            if len(list_of_keys) == 0 or total_weight_of_the_trip + min(list_of_values) > limit:
                loop_variable = False

        list_of_trips.append(trip)
        if len(list_of_keys) == 0:
            break
    return list_of_trips

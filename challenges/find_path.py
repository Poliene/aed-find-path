from heapq import heappush, heappop


def find_path(city_map, start, goal):

    if start == goal:
        return [start]

    frontier = []
    heappush(frontier, (0, start))

    came_from = {start: None}
    cost_so_far = {start: 0}

    while frontier:

        _, current = heappop(frontier)

        if current == goal:
            break

        for neighbor in city_map.roads[current]:

            new_cost = cost_so_far[current] + 1

            if (
                neighbor not in cost_so_far
                or new_cost < cost_so_far[neighbor]
            ):

                cost_so_far[neighbor] = new_cost

                heappush(
                    frontier,
                    (
                        new_cost,
                        neighbor,
                    )
                )

                came_from[neighbor] = current

    if goal not in came_from:
        return []

    path = []

    current = goal

    while current is not None:
        path.append(current)
        current = came_from[current]

    path.reverse()

    return path
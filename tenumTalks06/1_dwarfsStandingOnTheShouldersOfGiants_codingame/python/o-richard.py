"""
 * View Challenge here - https://www.codingame.com/training/medium/dwarfs-standing-on-the-shoulders-of-giants
 * The paths are recomputed as new nodes are addded on the directed graph.
 * An adjaceny list is formed that keeps track of all paths.
 * The longest path is the one with the most items.
"""

paths: list[list[int]] = []


# Order is preserved during insertion.
def recompute_paths(x, y) -> None:
    """
    x - Influencer
    y - Influencee
    """
    # Keeps track if the new path was added. Minimizes duplication of distinct paths.
    added = False
    for path in paths:
        if y in path:
            y_index = path.index(y)
            items_before_y = path[:y_index]
            no_items_before_y = len(items_before_y)
            if no_items_before_y == 0:
                # assign x to be the first item of the list.
                path.insert(0, x)
                continue
            elif no_items_before_y == 1:
                # check the value of the item. such a path already exists.
                if x == items_before_y[0]:
                    continue
            paths.append([x, y])
            added = True
            break

    for path in paths:
        if x in path:
            x_index = path.index(x)
            items_after_x = path[x_index + 1:]
            no_items_after_x = len(items_after_x)
            if no_items_after_x == 0:
                # assign y as the last item of the list
                path.append(y)
                continue
            elif no_items_after_x == 1:
                # check the value of the item. such a path already exists.
                if x == items_after_x[0]:
                    continue
            if not added:
                paths.append([x, y])
            break

    # Obtain the longest paths
    for outer_index in range(len(paths)):
        for inner_index in range(outer_index + 1, len(paths)):
            outer_path = paths[outer_index]
            inner_path = paths[inner_index]
            if len(outer_path) > len(inner_path):
                # Concatenate on the outermost path
                last_digit = outer_path[-1]
                if last_digit in inner_path:
                    # Concatenate the longest path
                    paths[outer_index] = [*outer_path, *(inner_path[inner_path.index(last_digit) + 1:])]
            else:
                # Concatenate on the innermost path
                last_digit = inner_path[-1]
                if last_digit in outer_path:
                    # Concatenate the longest path
                    paths[inner_index] = [*inner_path, *(outer_path[outer_path.index(last_digit) + 1:])]


n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]

    if x != y:
        if len(paths) == 0:
            paths.append([x, y])
        else:
            recompute = False
            for path in paths:
                if x in path or y in path:
                    recompute = True
                    break
            if not recompute:
                paths.append([x, y])
            else:
                recompute_paths(x, y)

answer = 0
for path in paths:
    no_of_items = len(path)
    if answer < no_of_items:
        answer = no_of_items

# The number of people involved in the longest succession of influences
print(answer)

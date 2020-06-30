
def earliest_ancestor(ancestors, starting_node):
    child_map = dict()
    for parent, child in ancestors:
        if child in child_map:
            child_map[child].append(parent)
        else:
            child_map[child] = [parent]

    if starting_node not in child_map:
        return -1

    generations = [[starting_node]]
    for children in generations:
        parents = []
        for child in children:
            if child in child_map:
                parents.extend(child_map[child])
        if len(parents) > 0:
            generations.append(parents)

    return min(generations[-1])

        
            
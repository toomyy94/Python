def max_path(tree):
    # Base case: if the tree is just a single integer, return that integer as the path value
    if isinstance(tree, int):
        return tree

    # Extract the value of the current node
    node_value = tree[1]

    # Recursively calculate the maximum path from the left and right subtrees
    left_path = max_path(tree[0])
    right_path = max_path(tree[2])

    # Return the maximum path value including the current node
    return node_value + max(left_path, right_path)

# Example usage:
tree1 = ((2, 1, ((1, 2, 2), 2, 1)), 0, (5, 4, 2))
tree2 = (1, 3, 2)
tree3 = ((1, 1, 3), 0, 3)
tree4 = ((2, 3, (4, 5, 2)), 0, (7, 1, 3))

print(max_path(tree1))  # Output: 9
print(max_path(tree2))  # Output: 5
print(max_path(tree3))  # Output: 4
print(max_path(tree4))  # Output: 12

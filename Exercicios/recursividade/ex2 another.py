def flatten(alist):
    # Base case: if the input list is empty, return an empty list
    if not alist:
        return []

    # Initialize an empty result list
    result = []

    # Iterate through each element in the input list
    for item in alist:
        if isinstance(item, list):
            # If the element is a list, recursively call flatten on it
            # and append each flattened element to the result list
            result += flatten(item)
        else:
            # If the element is not a list, append it to the result list
            result.append(item)

    return result

# Example usage:
print(flatten([]))  # Output: []
print(flatten(['Hello', [2, [[], False]], [True]]))  # Output: ['Hello', 2, False, True]
print(flatten([[1,[2,3]], [4,[[5]],6], [7,8,9]]))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(flatten([1]))  # Output: [1]

matrix3d = [
    [[1, 2], [3, 4]],
    [[5, 6], [7]],
    [[8]]
]

def flatten(arr):
    result = []
    for i in arr:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result

print(flatten(matrix3d))



def generate_boolean_arrays_with_separate_repeats(limit):
    arrays = [[True if i == j else False for j in range(limit)] for i in range(limit)]
    repeated_arrays = [array for array in arrays for _ in range(limit)]
    return repeated_arrays

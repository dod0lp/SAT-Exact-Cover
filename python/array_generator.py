import numpy as np
from random import randint, choice

def generate_boolean_arrays_with_separate_repeats(limit):
    arrays = [[True if i == j else False for j in range(limit)] for i in range(limit)]
    repeated_arrays = [array for array in arrays for _ in range(limit)]
    return repeated_arrays

def generator_queen_array(limit: int = 9) -> list[list[bool]]:
    ans = []
    for row in range(limit):
        temp = []
        for col in range(limit):
            if (row == col):
                temp.append(True)
            else:
                temp.append(False)

        ans.append(temp)

    return ans

def generator_queen_array_fuzzy(limit: int = 9) -> list[list[bool]]:
    ans = []
    for row in range(limit):
        temp = []
        for col in range(limit):
            if (row == col):
                temp.append(True)
            else:
                rand = randint(0, 100)
                if (rand < 50):
                    temp.append(False)
                else:
                    temp.append(True)

        ans.append(temp)

    return ans


def generator_queen_array_fuzzy_sat(limit: int = 9) -> list[list[bool]]:
    ans = []
    for row in range(limit):
        temp = []
        for col in range(limit):
            if (row == col):
                temp.append(True)
            elif (row < col):
                temp.append(choice([True, False]))
            else:
                temp.append(False)

        ans.append(temp)

    ans[-1] = [True for _ in range(limit)]

    return ans


def generate_boolean_array(rows = 5, cols = 5, true_percentages = [50, 30, 70, 50, 40]):
    if len(true_percentages) != cols:
        raise ValueError("The length of true_percentages must match the number of columns.")

    bool_array = np.zeros((rows, cols), dtype=bool)

    for col in range(cols):
        prob_true = true_percentages[col] / 100
        bool_array[:, col] = np.random.choice([True, False], size=rows, p=[prob_true, 1 - prob_true])

    return bool_array

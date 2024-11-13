
"""
Rows Columns
[Columns]
...
...
[Columns]
"""

"""
Parse file that contains boolean adjacency matrix of a graph
"""
def parse_file(filename: str) -> list[bool]:
    error_msg_first_line = "Error: The first line should contain exactly two integers."

    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        try:
            rows, cols = map(int, first_line.split())
        except ValueError:
            print(error_msg_first_line)
            return
        

        matrix = []
        for i in range(rows):
            line = file.readline().strip()
            try:
                values = [bool(int(x)) for x in line.split()]
                
                if len(values) != cols:
                    print(f"Error: Line {i+2} does not have {cols} values.")
                    return
                
                matrix.append(values)
            except ValueError:
                print(f"Error: Line {i+2} contains non-integer values.")
                return
        
        return matrix

# row i
# col j

def exact_cover_to_sat(matrix) -> list[int]:
    rows, columns = len(matrix), len(matrix[0])
    clauses = []

    # For each column, ensure that exactly one row covers it
    for col in range(columns):  # For each column
        # At least one row should be selected to cover column col
        clause = []
        for row in range(rows):
            if matrix[row][col] == True:  # If matrix[row][col] is True
                clause.append(row + 1)  # Because of 1-indexation
        clauses.append(clause)

        # At most one row should be selected to cover column col
        for row1 in range(rows):
            if matrix[row1][col] == True:
                for row2 in range(row1 + 1, rows):
                    if matrix[row2][col] == True:
                        clauses.append([ -(row1 + 1), -(row2 + 1) ])  # Ensure at most one row

    return clauses

def print_sep():
    print("##############\n")

def clauses_into_dimacs(clauses: list[int]):
    return [clause + [0] for clause in clauses]

if __name__ == "__main__":
    data_prefix = "../data/"
    filename = data_prefix + "1.in"

    parsed_input = parse_file(filename)
    clauses = exact_cover_to_sat(parsed_input)
    dimacs_clauses = clauses_into_dimacs(clauses)

    print("Parsed input:")
    for line in parsed_input:
        print(line)
    print_sep()

    print("CNF clauses:")
    for line in clauses:
        print(line)
    print_sep()

    print("DIMACS clauses:")
    for line in dimacs_clauses:
        print(line)
    print_sep()
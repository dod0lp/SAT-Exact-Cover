import subprocess

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

"""
Writes clause list into file line by line, no formatting of dimacs
"""
def write_clause_list_to_file(clauses: list[int], filename: str):
    with open(filename, 'a') as file:
        for sublist in clauses:
            file.write(" ".join(map(str, sublist)) + "\n")

"""
Writes prefix of DIMACS
"""
def dimacs_header(clauses: list[int], filename: str):
    # = number of variables (maximum absolute value in the clauses)
    num_variables = max(max(abs(literal) for literal in clause) for clause in clauses)
    
    num_clauses = len(clauses)
    
    with open(filename, 'w') as file:
        file.write(f"p cnf {num_variables} {num_clauses}\n")

"""
Output DIMACS format into REWRITTEN file.
"""
def output_dimacs_file(clauses: list[int], filename: str):
    dimacs_header(clauses, filename)

    write_clause_list_to_file(clauses, filename)


def print_sep():
    print("##############\n")

def print_list(message: str, array: list, sep = True):
    print(message)
    for line in array:
        print(line)

    print_sep()

def clauses_into_dimacs(clauses: list[int]):
    return [clause + [0] for clause in clauses]


RET_UNSAT = 20
RET_SAT = 10

def run_glucose(filename_dimacs: str):
    try:
        result = subprocess.run(['glucose', '-model', '-verb=' + "1" , filename_dimacs], text=True, capture_output=True)
        
        code = result.returncode
        result_message = result.stdout

        # Check if Glucose ran successfully
        if code == RET_SAT:
            print("Solvable, Glucose output:")
            print(result_message)
        elif code == RET_UNSAT:
            print("Not solvable")
            print(result_message)
    except FileNotFoundError:
        print("Glucose executable not found. Ensure 'glucose' is in your system's PATH.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    data_prefix = "../data/"
    filename_instance = "2"
    filename_base = data_prefix + filename_instance
    filename_in = filename_base + ".in"
    filename_res = filename_base + ".res"
    filename_dimacs = filename_base + ".dimacs"
    with open(filename_res, 'w') as file:
        file.write("Results: \n")


    parsed_input = parse_file(filename_in)
    clauses = exact_cover_to_sat(parsed_input)
    dimacs_clauses = clauses_into_dimacs(clauses)

    print_list("Parsed input:", parsed_input)
    print_list("CNF clauses:", clauses)
    print_list("DIMACS clauses:", dimacs_clauses)

    output_dimacs_file(dimacs_clauses, filename_dimacs)

    run_glucose(filename_dimacs)
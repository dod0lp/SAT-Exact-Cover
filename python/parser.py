
"""
Rows Columns
[Columns]
...
...
[Columns]
"""
def parse_file(filename):
    with open(filename, 'r') as file:
        first_line = file.readline().strip()
        try:
            rows, cols = map(int, first_line.split())
        except ValueError:
            print("Error: The first line should contain exactly two integers.")
            return
        
        print(f"Rows: {rows}, Columns: {cols}")
        
        matrix = []
        for i in range(rows):
            line = file.readline().strip()
            try:
                values = list(map(int, line.split()))
                if len(values) != cols:
                    print(f"Error: Line {i+2} does not have {cols} integers.")
                    return
                matrix.append(values)
            except ValueError:
                print(f"Error: Line {i+2} contains non-integer values.")
                return
        
        print("Parsed Matrix:")
        for row in matrix:
            print(row)

data_prefix = "../data/"
filename = data_prefix + "1.in"
parse_file(filename)

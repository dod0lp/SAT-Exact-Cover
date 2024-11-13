
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

data_prefix = "../data/"
filename = data_prefix + "1.in"
parse_file(filename)

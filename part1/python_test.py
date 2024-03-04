import os
import sys
import subprocess
from random import randint

# Range of matrices values
MAX_NUM = 10000
MIN_NUM = -10000

# Range of matrices lengths
MIN_ROWS = 1
MAX_ROWS = 5

# Colors
COLOR_END = "\033[0m"
COLOR_AQUA = "\033[96m"
COLOR_PINK = "\033[95m"
COLOR_YELLOW = "\033[93m"
COLOR_GREEN = "\033[92m"
COLOR_RED = "\033[91m"

# Output directory path
OUTPUTS_DIR = 'outputs'

# fail/success counters
num_success = 0
num_fail = 0


class IncompatibleMatrixDimensionsError(Exception):
    """Custom exception for incompatible matrix dimensions."""
    def __init__(self, message="Matrix dimensions are incompatible for multiplication"):
        self.message = message
        super().__init__(self.message)


# Generate matrix
def generate_matrix(num_rows):
    matrix = []
    num_cols = randint(MIN_ROWS, MAX_ROWS)
    for i in range(num_rows):
        matrix.append([])
        for j in range(num_cols):
            num = randint(MIN_NUM, MAX_NUM)
            matrix[i].append(num)
    return matrix


def matrix_multiplication(matrix_a, matrix_b):
    """Calculate the multiplication of the 2 matrices and return the result."""
    # Get dimensions of the matrices
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Check if the matrices are compatible for multiplication
    if cols_a != len(matrix_b):
        raise IncompatibleMatrixDimensionsError()

    # Initialize an empty matrix to store the result
    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    result = result_matrix_to_string(result_matrix)
    return "\n" + result


def result_matrix_to_string(matrix):
    num_of_rows = len(matrix)
    num_of_cols = len(matrix[0])
    result_string = "["
    for row in range(num_of_rows):
        for col in range(num_of_cols):
            # don't put space after last num in col
            if col == num_of_cols - 1:
                result_string += str(matrix[row][col])
            else:
                result_string += str(matrix[row][col]) + " "
        if row < num_of_rows - 1:
            result_string += "\n"
    result_string += "]\n"
    return result_string


def get_element(matrix, row=None, col=None):
    # Generate valid row and col to get value of
    row = randint(0, len(matrix) - 1) if row is None else row
    col = randint(0, len(matrix[0]) - 1) if col is None else col
    result = matrix[row][col]
    return row, col, result


def inner_prod(matrix_a, matrix_b, row_a=None, col_b=None):
    # Generate row from matrix a and col from matrix b to multiply
    row_a = randint(0, len(matrix_a) - 1) if row_a is None else row_a
    col_b = randint(0, len(matrix_b[0]) - 1) if col_b is None else col_b

    if len(matrix_a[0]) != len(matrix_b):
        raise IncompatibleMatrixDimensionsError()

    result = 0
    for k in range(len(matrix_a[0])):
        result += matrix_a[row_a][k] * matrix_b[k][col_b]

    return row_a, col_b, result


def create_expected_out_file(num, get_row, get_col, get_res, matrix_mul_res,
                             prod_row=None, prod_col=None, prod_res=None):
    with open(f"{OUTPUTS_DIR}/out_expected_{num}", "w") as f:
        f.write(f"mat_a[{get_row}][{get_col}] = {get_res}\n")
        if prod_row is not None and prod_col is not None and prod_res is not None:
            f.write(f"mat_a[{prod_row}]*mat_b[{prod_col}] = {prod_res}\n")
        f.write(f"mat_a*mat_b={matrix_mul_res}")


def get_matrix_vals(matrix):
    """Return the values of the matrix as a continuous string."""
    matrix_vals = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_vals += f"{matrix[i][j]} "
    return matrix_vals.strip()


def basic_matrices():
    # Test 1
    matrix_a = [[1, 0, 3], [0, 1, 2]]
    matrix_b = [[0], [15], [3]]
    row = 0
    col = 2
    row_a = 1
    col_b = 0
    return matrix_a, matrix_b, row, col, row_a, col_b


def run_generic_test(test_num, matrix_a, matrix_b, row=None, col=None, row_a=None, col_b=None):
    # Generate 2 matrices to run test on
    print(f"{COLOR_AQUA}Running test {test_num}...{COLOR_END}")
    M = len(matrix_a)     # Number of rows in matrix A
    N = len(matrix_a[0])  # Number of columns in matrix A
    P = len(matrix_b)     # Number of rows in matrix B
    Q = len(matrix_b[0])  # Number of columns in matrix B
    mat_a = get_matrix_vals(matrix_a)  # values of matrix A
    mat_b = get_matrix_vals(matrix_b)  # values of matrix B
    get_row, get_col, get_res = get_element(matrix_a, row, col)
    try:
        prod_row_a, prod_col_b, prod_res = inner_prod(matrix_a, matrix_b, row_a, col_b)
        matrix_mul_res = matrix_multiplication(matrix_a, matrix_b)
    except IncompatibleMatrixDimensionsError:
        prod_row_a = prod_col_b = prod_res = None
        matrix_mul_res = "0\n"
        print(f"{COLOR_YELLOW}Incompatible matrix dimensions for multiplication N={N} != P={P}{COLOR_END}")

    create_expected_out_file(num=test_num,
                             get_row=get_row,
                             get_col=get_col,
                             get_res=get_res,
                             matrix_mul_res=matrix_mul_res,
                             prod_row=prod_row_a,
                             prod_col=prod_col_b,
                             prod_res=prod_res)

    print(f"{COLOR_YELLOW}mat_a = {COLOR_END}{matrix_a}\n\n{COLOR_YELLOW}mat_b = {COLOR_END}{matrix_b}\n")
    print(f"{COLOR_YELLOW}get_element_from_matrix: Expected: {COLOR_END}mat_a[{get_row}][{get_col}] = {get_res}\n")
    if prod_row_a is not None and prod_col_b is not None and prod_res is not None:
        print(f"{COLOR_YELLOW}inner_prod: Expected: {COLOR_END}mat_a[{prod_row_a}]*mat_b[{prod_col_b}] = {prod_res}\n")
    print(f"{COLOR_YELLOW}matrix_multiplication: Expected: {COLOR_END}mat_a*mat_b ={matrix_mul_res}")
    inputs = (f"{M} {N} {P} {Q}  {mat_a}  {mat_b}  {N} {get_row} {get_col}  {prod_row_a if prod_row_a else 0}"
              f" {prod_col_b if prod_col_b else 0 } {N} {Q}")

    # Run the bash test script
    command = [
        "./better_basic_test.sh",
        f"{OUTPUTS_DIR}/out_actual_{test_num}",
        f"{OUTPUTS_DIR}/out_expected_{test_num}",
        inputs
    ]
    command_result = subprocess.run(command, stdout=subprocess.PIPE)
    output = command_result.stdout.decode("utf-8")
    print(output)
    if "FAIL" in output:
        global num_fail
        num_fail += 1

    elif "PASS" in output:
        os.system(f"rm -f {OUTPUTS_DIR}/out_actual_{test_num}")
        os.system(f"rm -f {OUTPUTS_DIR}/out_expected_{test_num}")
        global num_success
        num_success += 1
    print("\n")


if __name__ == '__main__':
    arguments = sys.argv[1:]

    if len(arguments) >= 1:
        the_generate_num = int(arguments[0])
    else:
        print(f"{COLOR_YELLOW}Warning: Number of tests to generate not given, defaulting to 10...{COLOR_END}")
        the_generate_num = 10

    needed_files = ["aux_hw3.o", "better_basic_test.sh", "better_test1.c", "python_test.py", "students_code.S"]
    for file in needed_files:
        if not os.path.exists(file):
            print(f"{COLOR_RED}Error: Needed Files: {COLOR_END}{needed_files}\n{COLOR_RED}Missing:{COLOR_END}{file},"
                  f"\nExiting Test...")
            os.system(f"rmdir --ignore-fail-on-non-empty {OUTPUTS_DIR}")
            sys.exit(1)

    print(f"{COLOR_PINK}Running Basic Tests...{COLOR_END}")
    os.system(f"[ -d '{OUTPUTS_DIR}' ] && rm -rf '{OUTPUTS_DIR}'; mkdir -p '{OUTPUTS_DIR}'")
    the_mat_a, the_mat_b, the_row, the_col, the_row_a, the_col_b = basic_matrices()
    run_generic_test(test_num="basic", matrix_a=the_mat_a, matrix_b=the_mat_b, row=the_row,
                     col=the_col, row_a=the_row_a, col_b=the_col_b)

    print(f"{COLOR_PINK}Running Randomized Tests...{COLOR_END}")
    for the_i in range(the_generate_num - 1):
        num_rows = randint(MIN_ROWS, MAX_ROWS)
        the_mat_a = generate_matrix(num_rows=num_rows)
        # 30% chance of generating incompatible matrices
        chance_compatible = randint(1, 10)
        if chance_compatible <= 7:
            the_mat_b = generate_matrix(num_rows=len(the_mat_a[0]))
        else:
            while True:
                num_b_rows = randint(MIN_ROWS, MAX_ROWS)
                if num_b_rows != len(the_mat_a[0]):
                    break
                the_mat_b = generate_matrix(num_b_rows)
        run_generic_test(test_num=the_i + 1, matrix_a=the_mat_a, matrix_b=the_mat_b)

    print(f"{COLOR_PINK}Ran {num_success + num_fail} out of {the_generate_num} Tests{COLOR_END}")
    if num_success == the_generate_num:
        print(f"{COLOR_GREEN}All tests passed!{COLOR_END}")
    else:
        if num_fail > 0:
            print(f"{COLOR_RED}Failed{COLOR_END} {num_fail}/{num_success + num_fail} tests.")
        else:
            print(f"{COLOR_YELLOW}Some tests did not run successfully{COLOR_END}")
            print(f"{COLOR_GREEN}Passed{COLOR_END} {num_success}/{num_success + num_fail} tests.")
    os.system(f"rmdir --ignore-fail-on-non-empty {OUTPUTS_DIR}")

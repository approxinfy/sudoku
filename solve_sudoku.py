from datetime import datetime

# create matrix from input file
def get_matrix(input_file):
    f = open(input_file, 'r') # f: file
    return [[int(num) for num in f.readline().split(",")] for m in range(9)] # num: number, m: row index

# check if the number satisfies constraints in the given possition of the matrix
def check_position(m, n, matrix, num): # m: row index, n: column index, num: number
    # checking for number's existance in the current row
    exists = True if num in matrix[m] else False
    if exists: return False
    # checking for numbers existance in the current column
    for i in range(9):
        if matrix[i][n] == num: return False
    # checking for numbers existance in 3x3 sub-matrix of 9x9 matrix
    m, n = m-m%3, n-n%3
    for i in range(3):
        for j in range(3):
            if matrix[m+i][n+j] == num: return False
    return True

''' 
    solving the puzzle using naive backtracking:
    Perform an exhaustive check using all possibilities for each zero possition and backtrack when needed
'''
def solution(matrix):
    # using a global variable to count number of recursions
    global count
    # defining count if it's not defined yet
    if 'count' not in globals(): count = 0
    # updating count and definig terminate variables
    count, terminate = count+1, True
    # finding an index in the matrix where value is zero
    for m in range(9):
        for n in range(9):
            if matrix[m][n] == 0:
                terminate = False
                break
        if not terminate: break
    # if the matrix is completely solved output it to console
    if terminate:
        print("Solution: ")
        for row in matrix: print("\t",row)
        print("Number of Recursions: ",count)
        return True
    # finding a number which satisfies constraints at current selected possition and backtracking when needed
    for num in range(1,10):
        if check_position(m, n, matrix, num):
            matrix[m][n] = num
            # if recursive solution call returns true when puzzle is solved else iterate with the next number 
            if solution(matrix): return True
            matrix[m][n] = 0
    return False
# making first call to solution function
input_file = input('Please provide an input file path:')
start = datetime.now()
solution(get_matrix(input_file))
# calculation of execution time
print(f">> Execution time = {(datetime.now()-start).total_seconds()}s")
"""Matrix_MN"""
def matrix_mn():
    """Matrix_MN"""
    m = int(input())
    n = int(input())
    matrix = []
    for _ in range(m * n):
        num = int(input())
        matrix.append(num)
    for i in range(m):
        row = matrix[i*n : (i+1)*n]
        print(" ".join(map(str, row)))
matrix_mn()

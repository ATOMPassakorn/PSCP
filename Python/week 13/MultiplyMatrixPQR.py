"""MultiplyMatrixPQR"""
def matrix():
    """MultiplyMatrixPQR"""
    p = int(input())
    q = int(input())
    r = int(input())
    count = 0
    total_len = 0
    sum_matrix = 0
    add_mat = []
    matrix_1 = []
    matrix_2 = []
    result_matrix = []
    for _ in range(p*q):
        count += 1
        add_mat.append(int(input()))
        if count == q:
            matrix_1.append(add_mat)
            add_mat = []
            count = 0
    for _ in range(q*r):
        count += 1
        total_len += 1
        add_mat.append(int(input()))
        if count == r:
            matrix_2.append(add_mat)
            add_mat = []
            count = 0
    for i in matrix_1:
        for x in range(r):
            for j in matrix_2:
                sum_matrix += i[count]*j[x]
                count += 1
            result_matrix.append(sum_matrix)
            sum_matrix = 0
            count = 0
    count = 0
    for z in result_matrix:
        if count == r:
            print(sep="\n")
            print(z,end=" ")
            count = 0
        else:
            print(z,end=" ")
        count += 1
matrix()

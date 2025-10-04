# Python code to print n^2 numbers in Cantor's diagonal format

def cantors_diag(n = 4):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    init = 1
    for k in range(2*n - 1):
        if k%2 == 0:
            i = min(k, n-1)
            j = k - i
            while i >= 0 and j < n:
                matrix[i][j] = init
                init += 1
                i -= 1
                j += 1
        else:
            j = min(k, n-1)
            i = k - j
            while j >= 0 and i < n:
                matrix[i][j] = init
                init += 1
                i += 1
                j -= 1

    return matrix
    
n = int(input())
matrix = cantors_diag(n)
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end = " ")
    print()
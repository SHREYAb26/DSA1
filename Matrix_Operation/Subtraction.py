def Subtraction(A, B):
    if (A.r != B.r) or (A.c != B.c):
        print("Cannot add")
    else:
        C = []
        for i in range(A.r):
            row = []
            for j in range(A.c):
                diff = A[i][j]-B[i][j]
                row.append(diff)
                diff = 0
            C.append(row)
        return C
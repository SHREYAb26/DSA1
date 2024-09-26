def Multiplication(A, B):
    if A.r == B.c:
        C = []
        for i in range(A.r):
            row=[]
            for j in range(B.c):
                sum=0
                for k in range(B.r):
                    sum += A[i][k] * B[k][j]
                row.append(sum)
            C.append(row)
        return C
    else:
        print("Invalid input")
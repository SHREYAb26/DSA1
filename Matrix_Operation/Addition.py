def Addition(A,B):
    # if (A.r != B.r) or (A.c != B.c):
    #     print("Cannot add")
    # else:

        C = []
        for i in range(len(A)):
            row =[]
            for j in range(A.c):
                sum= A[i][j]+B[i][j]
                row.append(sum)
                sum = 0
            C.append(row)
        return C



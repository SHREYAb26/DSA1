# def Transpose(A):
#     B=[]
#     for i in range(len(A[0])):
#         rows=[]
#         for j in range(len(A)):
#            rows.append(A[j][i])
#         B.append(rows)
#     return B
def Transpose(A):
    B = []
    for i in range(len(A[0])):
        rows = []
        for j in range(len(A)):
            rows.append(A[j][i])
        B.append(rows)
    return B

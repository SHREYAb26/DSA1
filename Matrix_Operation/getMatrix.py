def getMatrix():
    M = []
    r = int(input("Enter number of rows you want to add "))
    c = int(input("Enter number of columns you want to add "))
    for i in range(r):
        rows = []
        for j in range(c):
            element = input("Enter element at (i,j) position ")
            rows.append(element)
        M.append(rows)
    return M
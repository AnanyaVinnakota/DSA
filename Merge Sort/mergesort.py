def merge(X, Y):

    p1 = p2 = 0
    out = []
    while p1 < len(X) and p2 < len(Y):

        if X[p1] < Y[p2]:
            out.append(X[p1])
            p1 += 1

        else:
            out.append(Y[p2])
            p2 += 1

    out += X[p1:] + Y[p2:]

    return out
arr=list(map(int,input("Enter the elements: ").split()))



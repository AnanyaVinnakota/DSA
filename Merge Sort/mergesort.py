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

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left, right)

if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements: ").split()))
    sorted_arr = mergeSort(arr)
    print("Sorted array:", sorted_arr)

def MergeSort(A):
    if len(A) == 1:
        return A
    if len(A) == 2:
        return sorted(A)
    if len(A) > 2:
        return Merge(MergeSort(A[0:len(A) // 2]), MergeSort(A[len(A) // 2::]))


def Merge(A, B):
    C = []
    i = j = 0
    while (1):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
            if i == len(A):
                C += B[j::]
                break
        if B[j] < A[i]:
            C.append(B[j])
            j += 1
            if j == len(B):
                C += A[i::]
                break
    return C
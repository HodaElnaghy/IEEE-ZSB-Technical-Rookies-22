def MaxHeapify(A, i):
    left = 2 * i + 1 if 2 * i + 1 < len(A) else None
    right = 2 * i + 2 if 2 * i + 2 < len(A) else None
    if left is None or right is None:
        return
    if left <= len(A) and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right <= len(A) and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, largest)


def BuildMaxHeap(A):
    for i in reversed(range(len(A) // 2)):
        MaxHeapify(A, i)
    return A


if __name__ == '__main__':
    Arr = list(map(int, input().rstrip().split()))
    print(BuildMaxHeap(Arr))
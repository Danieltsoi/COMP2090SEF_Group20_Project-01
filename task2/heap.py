#Task 2 – Heap & Heap Sort
def heapify(arr, n, i):
    """Maintain max-heap property"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Heap Sort Algorithm
    Time Complexity: O(n log n) for best, average, worst case
    Space Complexity: O(1) (in-place)
    """
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# Test code
if __name__ == "__main__":
    data1 = [12, 11, 13, 5, 6, 7]
    print("Original array 1:", data1)
    print("Sorted array 1:", heap_sort(data1.copy()))

    data2 = [3, 1, 4, 1, 5, 9, 2, 6]
    print("\nOriginal array 2:", data2)
    print("Sorted array 2:", heap_sort(data2.copy()))

def heapify(arr: list, n: int, i: int):
    """
    Maintain max-heap structure.
    Time Complexity: O(log n)
    """
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


def heap_sort(arr: list) -> list:
    """
    Heap Sort Algorithm
    Time Complexity: O(n log n) for best / average / worst case
    Space Complexity: O(1) in-place
    """
    n = len(arr)
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr


if __name__ == "__main__":
    test_cases = [
        [12, 11, 13, 5, 6, 7],
        [9, 5, 1, 4, 3, 7],
        []
    ]

    for case in test_cases:
        print("Original:", case)
        print("Sorted:  ", heap_sort(case.copy()))
        print("-" * 30)

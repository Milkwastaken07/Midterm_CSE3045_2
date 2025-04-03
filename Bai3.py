def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
arr = list(map(int, input("Nhập các số nguyên, tách bằng dấu cách: ").split()))
bubble_sort(arr)
print("Mảng sau khi sắp xếp:", arr)

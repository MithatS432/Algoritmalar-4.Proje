def heapify(arr, n, i):
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
    n = len(arr)

    # Max heap oluşturma
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Elemanları tek tek çıkarma
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # En büyük elemanı sona al
        heapify(arr, i, 0)

# Örnek kullanım
liste = [12, 11, 13, 5, 6, 7]
print("Sıralanmadan önce:", liste)
heap_sort(liste)
print("Sıralandıktan sonra:", liste)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Ortadaki elemanı pivot seçiyoruz
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Örnek kullanım
liste = [10, 7, 8, 9, 1, 5]
print("Sıralanmadan önce:", liste)
liste = quick_sort(liste)
print("Sıralandıktan sonra:", liste)

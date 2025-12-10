def insertion_sort(arr, debug=False):
    n = len(arr)
    for i in range(1, n):
        k = arr[i]
        j = i

        if debug:
            print(f"\n[i={i}] เริ่มรอบ: arr = {arr}, k = {k}")

        while j > 0 and arr[j - 1] >= k:
            if debug:
                print(f"  - เลื่อน {arr[j-1]} มาที่ตำแหน่ง {j}")
            arr[j] = arr[j - 1]
            j -= 1

        arr[j] = k
        if debug:
            print(f"  → ใส่ค่า k={k} ลงตำแหน่ง {j}, ผลลัพธ์: {arr}")
    return arr


print(insertion_sort([11,17,6,8,12,5], debug=True))

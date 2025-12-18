def selection_sort(arr, debug=False):
    n = len(arr)
    for i in range(n):
        min_idx = i
        
        if debug:
            print(f"\n[i={i}] เริ่มรอบ: arr = {arr}")
        
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                if debug:
                    print(f"  - พบค่าน้อยกว่า: {arr[j]} ที่ตำแหน่ง {j} (min_idx = {min_idx})")
        
        
        if min_idx != i:
            if debug:
                print(f"  → สลับ {arr[i]} (ตำแหน่ง {i}) กับ {arr[min_idx]} (ตำแหน่ง {min_idx})")
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if debug:
                print(f"    ผลลัพธ์: {arr}")
        else:
            if debug:
                print(f"  → ไม่ต้องสลับ (ค่าที่ตำแหน่ง {i} อยู่ถูกต้องแล้ว)")
    
    return arr


print(selection_sort([11,17,6,8,12,5], debug=True))


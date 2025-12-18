def bubble_sort(arr, debug=False):
    n = len(arr)
    for i in range(n):
        swapped = False
        
        if debug:
            print(f"\n[รอบที่ {i+1}] เริ่มรอบ: arr = {arr}")
        
        for j in range(0, n - i - 1):
            if debug:
                print(f"  - เปรียบเทียบ {arr[j]} (ตำแหน่ง {j}) กับ {arr[j+1]} (ตำแหน่ง {j+1})")
            
            if arr[j] > arr[j+1]:
                if debug:
                    print(f"    → {arr[j]} > {arr[j+1]} สลับกัน!")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                if debug:
                    print(f"      ผลลัพธ์: {arr}")
            else:
                if debug:
                    print(f"    → {arr[j]} <= {arr[j+1]} ไม่ต้องสลับ")
        
        if not swapped:
            if debug:
                print(f"  → ไม่มีการสลับในรอบนี้ (เรียงเสร็จแล้ว)")
            break
    
    return arr


print(bubble_sort([11,17,6,8,12,5], debug=True))


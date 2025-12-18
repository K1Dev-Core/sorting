def radix_sort(arr, debug=False):
    if not arr:
        return arr
    
    # หาค่าที่มากที่สุดเพื่อหาจำนวนหลัก
    max_val = max(arr)
    exp = 1
    
    if debug:
        print(f"เริ่มต้น: arr = {arr}")
        print(f"ค่าสูงสุด: {max_val}")
    
    # เรียงตามแต่ละหลัก (หน่วย, สิบ, ร้อย, ...)
    while max_val // exp > 0:
        if debug:
            print(f"\n[หลักที่ {exp}] เรียงตามหลักที่ {exp}")
        
        # ใช้ counting sort สำหรับเรียงตามหลักปัจจุบัน
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # นับจำนวนของแต่ละ digit (0-9)
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
            if debug:
                print(f"  - {arr[i]} → digit = {index}")
        
        if debug:
            print(f"  นับจำนวน: {count}")
        
        # แปลง count ให้เป็นตำแหน่งจริง
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        if debug:
            print(f"  ตำแหน่งสะสม: {count}")
        
        # เรียงจากหลังไปหน้าเพื่อรักษาเสถียรภาพ
        for i in range(n - 1, -1, -1):
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            if debug:
                print(f"  - ใส่ {arr[i]} (digit={index}) ลงตำแหน่ง {count[index]}")
        
        # คัดลอกผลลัพธ์กลับไปยัง arr
        arr = output.copy()
        
        if debug:
            print(f"  ผลลัพธ์หลังเรียงหลักที่ {exp}: {arr}")
        
        # ไปหลักถัดไป
        exp *= 10
    
    if debug:
        print(f"\nผลลัพธ์สุดท้าย: {arr}")
    
    return arr


print(radix_sort([170 , 45 , 75 , 90 , 802 , 24 , 2 , 66], debug=True))


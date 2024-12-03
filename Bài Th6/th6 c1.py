print("le van thanh")
print("mssv: 235752021610020")
# binary_search.py (module)

def binary_search(lst, value):
    # Danh sách phải được sắp xếp để thuật toán tìm kiếm nhị phân hoạt động đúng
    left, right = 0, len(lst) - 1
    
    while left <= right:
        mid = (left + right) // 2  # Tính chỉ số giữa
        
        if lst[mid] == value:  # Nếu tìm thấy giá trị
            return True
        elif lst[mid] < value:  # Nếu giá trị cần tìm lớn hơn giá trị giữa
            left = mid + 1
        else:  # Nếu giá trị cần tìm nhỏ hơn giá trị giữa
            right = mid - 1
    
    return False  # Trả về False nếu không tìm thấy

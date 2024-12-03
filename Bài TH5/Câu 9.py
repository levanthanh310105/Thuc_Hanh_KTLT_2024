print("le van thanh")
print("mssv: 235752021610020")
def binary_search(lst, value):
    left = 0  
    right = len(lst) - 1 
    while left <= right:
        mid = (left + right) // 2 
        if lst[mid] == value:
            return True
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1

    return False  
n = int(input("Enter the number of elements in the list: "))
lst = sorted([int(input(f"Enter the {i + 1}th element: ")) for i in range(n)])  # Sắp xếp danh sách
value = int(input("Enter the element to find: "))
ket_qua = binary_search(lst, value)
print("Search result:", ket_qua)


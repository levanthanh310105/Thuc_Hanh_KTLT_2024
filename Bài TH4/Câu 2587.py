print("le van thanh")
print("mssv: 235752021610020")

# Nhập danh sách các số, phân tách bởi dấu phẩy
danh_sach = input("Nhập các số, phân tách bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nguyên
so_nguyen = [int(so) for so in danh_sach.split(",")]

# Lọc các số lẻ
so_le = [so for so in so_nguyen if so % 2!= 0]

# In kết quả
print("Các số lẻ trong danh sách là:", so_le)

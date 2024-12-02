print("le van thanh")
print("mssv: 235752021610020")

# Nhập chuỗi các số nhị phân
chuoi_nhi_phan = input("Nhập các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ")

# Tách chuỗi thành danh sách các số nhị phân
danh_sach = chuoi_nhi_phan.split(',')

# Lọc các số nhị phân chia hết cho 5
ket_qua = [so for so in danh_sach if int(so, 2) % 5 == 0]

# In ra các số chia hết cho 5, phân tách bằng dấu phẩy
print("Các số nhị phân chia hết cho 5 là:", ','.join(ket_qua))

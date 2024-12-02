print("le van thanh")
print("mssv: 235752021610020")

# Khởi tạo danh sách để lưu các số thỏa mãn điều kiện
ket_qua = []

# Duyệt qua từng số trong đoạn từ 1000 đến 3000
for so in range(1000, 3001):
    # Chuyển số sang chuỗi để kiểm tra từng chữ số
    chuoi_so = str(so)
    # Kiểm tra nếu tất cả các chữ số đều là số chẵn
    if all(int(chu) % 2 == 0 for chu in chuoi_so):
        ket_qua.append(chuoi_so)

# In ra các số thỏa mãn điều kiện, cách nhau bởi dấu phẩy
print("Các số có tất cả chữ số là số chẵn:", ','.join(ket_qua))

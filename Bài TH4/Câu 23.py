print("le van thanh")
print("mssv: 235752021610020")

# Nhập câu
cau = input("Nhập một câu:")

# Khởi tạo biến đếm
so_chu_cai = 0
so_chu_so = 0

# Duyệt qua từng ký tự trong câu
for ky_tu in cau :
    if ky_tu.isalpha():
        so_chu_cai += 1
    elif ky_tu.isdigit():
        so_chu_so += 1

# In kết quả
print("Số chữ cái:", so_chu_cai)
print("Số chữ số:", so_chu_so)

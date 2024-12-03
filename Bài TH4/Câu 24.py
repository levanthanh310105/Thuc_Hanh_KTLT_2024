print("le van thanh")
print("mssv: 235752021610020")

cau = input("Nhập một câu: ")

so_chu_hoa = 0
so_chu_thuong = 0

for ky_tu in cau:
    if ky_tu.isupper():
        so_chu_hoa += 1
    elif ky_tu.islower():
        so_chu_thuong += 1

print("Số chữ hoa:", so_chu_hoa)
print("Số chữ thường:", so_chu_thuong)

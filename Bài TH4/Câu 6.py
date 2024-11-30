print("le van thanh")
print("mssv: 235752021610020")
# Nhập họ tên từ bàn phím
full_name = input("Nhập họ và tên: ")

# Phân tách họ và tên riêng
name_parts = full_name.split()

# Kiểm tra nếu chuỗi bao gồm ít nhất hai phần
if len(name_parts) >= 2:
    last_name = name_parts[0]  # Họ là phần đầu tiên
    first_name = name_parts[1]  # Tên riêng là phần thứ hai
    print("Họ:", last_name)
    second_name = name_parts[2]
    print("Tên:", second_name)
else:
    print("Chuỗi không có đủ họ và tên.")

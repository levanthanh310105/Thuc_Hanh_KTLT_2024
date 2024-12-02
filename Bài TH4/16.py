print("le van thanh")
print("mssv: 235752021610020")
# Nhập chuỗi các số nhị phân từ bàn phím
input_string = input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy): ")

# Tách các số nhị phân trong chuỗi
binary_numbers = input_string.split(',')

# In ra các giá trị đã nhập
print("Các số nhị phân đã nhập:")
for number in binary_numbers:
    print(number.strip())  # Loại bỏ khoảng trắng nếu có

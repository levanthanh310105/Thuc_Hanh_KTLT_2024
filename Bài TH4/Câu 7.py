print("le van thanh")
print("mssv: 235752021610020")
# Nhập chuỗi từ bàn phím
input_string = input("Nhập một chuỗi: ")

# Loại bỏ các chữ số khỏi chuỗi
new_string = ''.join([char for char in input_string if not char.isdigit()])

# In chuỗi mới ra màn hình
print("Chuỗi mới :", new_string)

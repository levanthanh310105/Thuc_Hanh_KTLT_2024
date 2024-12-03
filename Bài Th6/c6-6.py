print("le van thanh")
print("mssv: 235752021610020")
# Định nghĩa lớp StringManipulation
class StringManipulation:
    def __init__(self):
        self.text = ""  # Khởi tạo một thuộc tính text rỗng
    
    def get_String(self):
        # Nhận chuỗi đầu vào từ người dùng
        self.text = input("Nhập một chuỗi: ")  # Lưu chuỗi người dùng nhập vào
    
    def print_String(self):
        # In chuỗi bằng chữ in hoa
        print(self.text.upper())  # Dùng phương thức upper() để chuyển chuỗi thành in hoa

# Tạo đối tượng của lớp StringManipulation
string_obj = StringManipulation()

# Gọi phương thức get_String để nhận chuỗi từ người dùng
string_obj.get_String()

# Gọi phương thức print_String để in chuỗi bằng chữ in hoa
string_obj.print_String()

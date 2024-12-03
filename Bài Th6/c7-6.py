print("le van thanh")
print("mssv: 235752021610020")
import math  # Thư viện math để sử dụng hằng số pi và các hàm toán học

# Định nghĩa lớp Circle
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Lưu bán kính của hình tròn
    
    def area(self):
        # Tính diện tích hình tròn: diện tích = π * bán kính^2
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        # Tính chu vi hình tròn: chu vi = 2 * π * bán kính
        return 2 * math.pi * self.radius

# Tạo đối tượng Circle với bán kính cho trước
radius = float(input("Nhập bán kính hình tròn: "))  # Nhập bán kính từ người dùng
circle = Circle(radius)  # Tạo đối tượng Circle

# In diện tích và chu vi
print(f"Diện tích của hình tròn: {circle.area():.2f}")
print(f"Chu vi của hình tròn: {circle.perimeter():.2f}")

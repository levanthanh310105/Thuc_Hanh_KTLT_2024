print("le van thanh")
print("mssv: 235752021610020")
# Định nghĩa lớp HinhChunhat
class HinhChunhat:
    # Phương thức khởi tạo (constructor)
    def __init__(self, dai, rong):
        self.dai = dai  # Lưu chiều dài vào đối tượng
        self.rong = rong  # Lưu chiều rộng vào đối tượng
    
    # Phương thức để tính diện tích
    def dien_tich(self):
        return self.dai * self.rong  # Diện tích = chiều dài * chiều rộng

# Tạo một đối tượng HinhChunhat
hcn = HinhChunhat(5, 3)  # Tạo hình chữ nhật có chiều dài = 5 và chiều rộng = 3

# In diện tích của HinhChunhat
print("Diện tích của hình chữ nhật là:", hcn.dien_tich())

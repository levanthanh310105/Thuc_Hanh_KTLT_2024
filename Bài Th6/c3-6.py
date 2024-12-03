print("le van thanh")
print("mssv: 235752021610020")
# Định nghĩa lớp Nguoi
class Nguoi:
    def __init__(self, name):
        self.name = name  # Thuộc tính tên của người
    
    # Phương thức getGender (sẽ được ghi đè trong các lớp con)
    def getGender(self):
        raise NotImplementedError("Phương thức getGender cần được định nghĩa trong các lớp con.")

# Định nghĩa lớp Nam kế thừa từ Nguoi
class Nam(Nguoi):
    def __init__(self, name):
        super().__init__(name)  # Gọi constructor của lớp cha Nguoi

    # Phương thức getGender ghi đè để trả về "Nam"
    def getGender(self):
        return "Nam"

# Định nghĩa lớp Nu kế thừa từ Nguoi
class Nu(Nguoi):
    def __init__(self, name):
        super().__init__(name)  # Gọi constructor của lớp cha Nguoi

    # Phương thức getGender ghi đè để trả về "Nữ"
    def getGender(self):
        return "Nữ"

# Tạo đối tượng của lớp Nam và Nu
nam = Nam("Minh")
nu = Nu("Lan")

# In giới tính của các đối tượng
print(f"{nam.name} là {nam.getGender()}.")
print(f"{nu.name} là {nu.getGender()}.")

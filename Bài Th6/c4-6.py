print("le van thanh")
print("mssv: 235752021610020")
# Định nghĩa lớp RomanToInt
class RomanToInt:
    # Bảng tra cứu các giá trị của chữ La Mã
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    def __init__(self, roman):
        self.roman = roman  # Lưu giá trị số La Mã cần chuyển đổi

    def convert(self):
        total = 0
        prev_value = 0
        
        # Duyệt qua từng ký tự trong chuỗi La Mã từ phải qua trái
        for char in reversed(self.roman):
            current_value = self.roman_numerals[char]
            
            # Nếu giá trị hiện tại nhỏ hơn giá trị trước đó, trừ nó ra, ngược lại cộng vào
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            prev_value = current_value
        
        return total

# Tạo đối tượng và chuyển đổi
roman = input("Nhập số La Mã: ")  # Nhập số La Mã từ bàn phím
converter = RomanToInt(roman)  # Tạo đối tượng của lớp RomanToInt

# In ra kết quả chuyển đổi
print(f"Số nguyên tương ứng là: {converter.convert()}")

print("le van thanh")
print("mssv: 235752021610020")
# Định nghĩa lớp ReverseWords
class ReverseWords:
    def __init__(self, text):
        self.text = text  # Lưu chuỗi văn bản cần xử lý
    
    def reverse(self):
        # Tách chuỗi thành danh sách các từ và đảo ngược danh sách
        words = self.text.split()  # Tách chuỗi theo khoảng trắng
        reversed_words = words[::-1]  # Đảo ngược danh sách các từ
        return ' '.join(reversed_words)  # Kết hợp các từ lại thành chuỗi

# Dữ liệu vào
input_text = 'hello .py'

# Tạo đối tượng của lớp ReverseWords
reverser = ReverseWords(input_text)

# In ra kết quả sau khi đảo ngược
print(reverser.reverse())

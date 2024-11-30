print("le van thanh")
print("mssv: 235752021610020")
# Nhập dãy các từ từ bàn phím
input_string = input("Nhập một dãy các từ: ")

# Tách dãy từ thành các từ riêng lẻ
words = input_string.split()

# Tìm độ dài của từ dài nhất
max_length = max(len(word) for word in words)

# Tìm tất cả các từ có độ dài bằng độ dài lớn nhất
longest_words = [word for word in words if len(word) == max_length]

# In ra các từ dài nhất
print("Từ dài nhất:", ', '.join(longest_words))

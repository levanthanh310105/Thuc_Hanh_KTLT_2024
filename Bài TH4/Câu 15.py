print("le van thanh")
print("mssv: 235752021610020")
# Nhập chuỗi từ bàn phím
input_string = input("Nhập chuỗi các từ tiếng Anh, cách nhau bởi dấu cách: ")

# Tách các từ trong chuỗi
words = input_string.split()

# Sắp xếp các từ theo thứ tự từ điển
sorted_words = sorted(words)

# In các từ theo thứ tự từ điển
print("Các từ theo thứ tự từ điển:", sorted_words)

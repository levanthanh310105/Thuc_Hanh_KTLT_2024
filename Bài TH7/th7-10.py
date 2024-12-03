print("le van thanh")
print("mssv: 235752021610020")
def find_longest_words(text):
    words = text.split()
    words = [word.strip(",.!?;:") for word in words]
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
text = """
Trường đại học vinh xanh sạch đẹp"""
result = find_longest_words(text)
print("Những từ dài nhất trong văn bản là:", result)

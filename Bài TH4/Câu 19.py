print("le van thanh")
print("mssv: 235752021610020")
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Tạo tuple P gồm các số nguyên tố nhỏ hơn 1 triệu
P = tuple(i for i in range(2, 1000000) if la_nguyen_to(i))

# In tuple P (có thể chỉ in một phần vì tuple lớn)
print(P[:10])  # In 10 số nguyên tố đầu tiên

print("le van thanh")
print("mssv: 235752021610020")
def tong_uoc_so(x):
    # Tính tổng các ước số của x
    tong = 0
    for i in range(1, x // 2 + 1):
        if x % i == 0:
            tong += i
    return tong

def so_nho_hon(n):
    ket_qua = []
    for i in range(1, n):
        if tong_uoc_so(i) > i:
            ket_qua.append(i)
    return ket_qua

# Nhập số n
n = int(input("Nhập số n: "))
print("Các số nhỏ hơn", n, "là:", so_nho_hon(n))

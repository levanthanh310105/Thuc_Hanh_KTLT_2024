print("le van thanh")
print("mssv: 235752021610020")
import math

def Tinh(R):
    # Kiểm tra bán kính có hợp lệ không
    if R <= 0:
        return "Bán kính không hợp lệ. Vui lòng nhập giá trị lớn hơn 0."
    
    # Tính chu vi và diện tích hình tròn
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    return f"Chu vi: {chu_vi}, Diện tích: {dien_tich}"

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    ket_qua = Tinh(R)
    print(ket_qua)
except ValueError:
    print("Vui lòng nhập một số hợp lệ.")

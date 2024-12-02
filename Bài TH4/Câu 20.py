print("le van thanh")
print("mssv: 235752021610020")

def tam_giac_pascal(n):
    tam_giac = []  # Danh sách chứa các dòng của tam giác Pascal
    for i in range(n):
        dong = [1]  # Khởi tạo dòng với 1 ở đầu
        if i > 0:
            for j in range(1, i):
                # Mỗi phần tử là tổng của hai phần tử phía trên nó
                dong.append(tam_giac[i-1][j-1] + tam_giac[i-1][j])
            dong.append(1)  # Kết thúc dòng với 1
        tam_giac.append(dong)
    
    # In ra n dòng đầu tiên của tam giác Pascal
    for dong in tam_giac:
        print(dong)

# Nhập số n
n = int(input("Nhập số n: "))
print((f"{n} dòng đầu tiên của tam giác Pascal:"))
tam_giac_pascal(n)

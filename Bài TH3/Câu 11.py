print("le van thanh")
print("mssv: 235752021610020")

def benefit(t, n, k):
    # Tính lãi suất hàng tháng
    lai_suat_thang = t / 100

    # Tính số tiền nhận được sau k tháng
    so_tien_nhan_duoc = n * (1 + lai_suat_thang) ** k

    return so_tien_nhan_duoc

# Nhập các giá trị từ bàn phím
try:
    t = float(input("Nhập lãi suất tiết kiệm hàng tháng (%): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))

    # Gọi hàm benefit để tính toán
    ket_qua = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng: {ket_qua}")
except ValueError:
    print("Vui lòng nhập số liệu hợp lệ.")

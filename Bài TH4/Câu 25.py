print("le van thanh")
print("mssv: 235752021610020")

# Khởi tạo số dư ban đầu
so_du = 0

# Nhập nhật kỳ giao dịch từ người dùng
print("Khập nhật kỳ giao dịch (theo định dạng 'D 100' hoặc 'N 50', nhập 'STOP' để kết thúc):")
while True:
    giao_dich = input()
    if giao_dich == 'STOP':
        break
    else:
        # Tách loại giao dịch và số tiền
        loai, so_tien = giao_dich.split(' ')
        so_tien = int(so_tien)

        # Xử lý giao dịch
        if loai == 'D':
            # Nạp tiền
            so_du += so_tien
        elif loai == 'N':
            # Rút tiền
            so_du = so_tien

        print("Số tiền thực trong tài khoản là:", so_du)


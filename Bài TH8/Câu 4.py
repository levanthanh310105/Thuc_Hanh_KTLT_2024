print("le van thanh")
print("mssv: 235752021610020")
import tkinter as tk
from tkinter import messagebox

# Tạo một cửa sổ chính
window = tk.Tk()

# Thiết lập tiêu đề và kích thước của cửa sổ
window.title("Cửa sổ đồ họa với Tkinter")
window.geometry("400x300")  # Chiều rộng 400, chiều cao 300

# Tạo một nhãn để hiển thị văn bản
label = tk.Label(window, text="Nhấn nút hoặc phím để hiển thị thông báo", font=("Arial", 14))
label.pack(pady=20)  # Thêm khoảng cách bên trên và dưới cho nhãn

# Hàm xử lý sự kiện khi nhấn nút
def show_message():
    messagebox.showinfo("Thông báo", "Bạn vừa nhấn vào nút hoặc phím!")

# Thêm một nút vào cửa sổ với màu nền và màu chữ tùy chỉnh
message_button = tk.Button(
    window, 
    text="Nhấn vào đây", 
    command=show_message,  # Gọi hàm xử lý sự kiện khi nhấn nút
    font=("Arial", 12),
    bg="lightblue",  # Màu nền của nút
    fg="darkblue"    # Màu chữ của nút
)
message_button.pack(pady=10)  # Thêm khoảng cách bên trên và dưới cho nút

# Xử lý sự kiện phím bấm
window.bind("<KeyPress>", lambda event: show_message())

# Nút thoát với màu nền và màu chữ tùy chỉnh
exit_button = tk.Button(
    window, 
    text="Thoát", 
    command=window.quit, 
    font=("Arial", 12),
    bg="lightcoral",  # Màu nền của nút
    fg="white"        # Màu chữ của nút
)
exit_button.pack(pady=10)  # Thêm khoảng cách bên trên và dưới cho nút

# Chạy vòng lặp chính của tkinter
window.mainloop()


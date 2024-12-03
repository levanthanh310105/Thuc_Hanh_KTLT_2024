print("le van thanh")
print("235752021610020")
import tkinter as tk
def personal_info_form():
    root = tk.Tk()
    root.title("Thông tin cá nhân")
    tk.Label(root, text="Họ tên:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
    tk.Label(root, text="Le Van Thanh", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5, sticky="w")

    tk.Label(root, text="Ngày sinh:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
    tk.Label(root, text="31/01/2005", font=("Arial", 12)).grid(row=1, column=1, padx=10, pady=5, sticky="w")

    tk.Label(root, text="MSSV:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
    tk.Label(root, text="235752021610020", font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5, sticky="w")

    tk.Label(root, text="Ngành học:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
    tk.Label(root, text="Kĩ Thuật Điều Khiển Và Tự Động Hóa", font=("Arial", 12)).grid(row=3, column=1, padx=10, pady=5, sticky="w")

    root.mainloop()
personal_info_form()

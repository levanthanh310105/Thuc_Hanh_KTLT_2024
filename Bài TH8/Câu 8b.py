print("le van thanh")
print("235752021610020")
import tkinter as tk
from tkinter import messagebox
def show_selection():
    selection = radio_var.get()
    messagebox.showinfo("Lựa chọn", "Lựa chọn của bạn là: {}".format(selection))
root = tk.Tk()
root.title("Welcome")
radio_var = tk.StringVar(value="1")
tk.Label(root, text="Vui lòng chọn một:").pack(anchor=tk.W)
tk.Radiobutton(root, text="First", variable=radio_var, value="1").pack(anchor=tk.W)
tk.Radiobutton(root, text="Second", variable=radio_var, value="2").pack(anchor=tk.W)
tk.Radiobutton(root, text="Third", variable=radio_var, value="3").pack(anchor=tk.W)
tk.Button(root, text="Click Me", command=show_selection).pack(pady=10)
root.mainloop()

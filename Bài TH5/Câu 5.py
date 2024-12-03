print("le van thanh")
print("mssv: 235752021610020")
import numpy as np
mang = np.arange(12, 38)
mang_nguoc = mang[::-1]
vi_tri_max = np.argmax(mang_nguoc)  
vi_tri_min = np.argmin(mang_nguoc) 

print("Mảng sau khi đảo ngược:", mang_nguoc)
print("Vị trí phần tử lớn nhất:", vi_tri_max)
print("Vị trí phần tử nhỏ nhất:", vi_tri_min)



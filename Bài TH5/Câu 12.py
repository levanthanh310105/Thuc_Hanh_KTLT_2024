print("le van thanh")
print("mssv: 235752021610020")
import numpy as np
sinh_vien_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
sinh_height = np.array([40., 42., 45., 41., 38., 40., 42.])
sorted_indices = np.lexsort((sinh_vien_id, sinh_height))
print("Chỉ số đã sắp xếp:", sorted_indices)
print("Dữ liệu đã sắp xếp:")
for i in sorted_indices:
    print(sinh_vien_id[i], sinh_height[i])

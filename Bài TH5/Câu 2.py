print("le van thanh")
print("mssv: 235752021610020")

import datetime as dt

# Định dạng ngày tháng
format = '%Y-%m-%d %H:%M:%S'

# Lấy ngày tháng hiện tại
t2 = dt.datetime.now()

# Lấy ngày tháng từ chuỗi
t1 = dt.datetime.strptime('2008-10-12 14:45:52', format)

# In thông tin ngày tháng
print(f"Day: {t1.day}")
print(f"Month: {t1.month}")
print(f"Minute: {t1.minute}")
print(f"Second: {t1.second}")

# Tính số ngày khác biệt giữa hai ngày
diff = (t2 - t1).days
print(f"How many days difference: {diff}")

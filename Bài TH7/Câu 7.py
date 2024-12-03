print("le van thanh")
print("mssv: 235752021610020")
with open("D:/a.txt", "r") as input_file:
    line_count = sum(1 for line in input_file)
print("Số dòng trong tệp là:", line_count)

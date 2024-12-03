print("le van thanh")
print("mssv: 235752021610020")
data_list = ["Dòng thứ nhất", "Dòng thứ hai", "Dòng thứ ba", "Dòng thứ tư"]
file_name = "output.txt"

try:
    with open(file_name, "w", encoding="utf-8") as file:
        for item in data_list:
            file.write(item + "\n")
    print(f"Dữ liệu đã được ghi vào tệp '{file_name}' thành công.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

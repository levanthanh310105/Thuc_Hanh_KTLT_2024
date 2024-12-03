print("le van thanh")
print("mssv: 235752021610020")
source_file = "output.txt"  
destination_file = "copy_output.txt" 

try:
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()
    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)
    
    print(f"Nội dung đã được sao chép từ '{source_file}' sang '{destination_file}' thành công.")
except FileNotFoundError:
    print(f"Tệp nguồn '{source_file}' không tồn tại.")
except Exception as e:
    print(f"Có lỗi xảy ra: {e}")

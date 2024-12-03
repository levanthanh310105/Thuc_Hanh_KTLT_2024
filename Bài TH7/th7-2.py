def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        print("Tệp không tồn tại.")
        return None

# Đường dẫn tới tệp văn bản
file_path = "duong_dan_toi_tep_cua_ban.txt"
line_count = count_lines(file_path)

if line_count is not None:
    print(f"Số dòng trong tệp là: {line_count}")

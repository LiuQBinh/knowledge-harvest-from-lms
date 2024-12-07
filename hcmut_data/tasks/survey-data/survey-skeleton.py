import json

# Đường dẫn tới file JSON
file_path = "/home/dream-base/Documents/Github/knowledge-harvest-from-lms/relation_info/conceptnet.json"

# Đọc nội dung file JSON
with open(file_path, "r") as file:
    data = json.load(file)

# Lấy danh sách các key cấp 1
# keys_lv1 = list(data.keys())
for index, key in enumerate(data.keys(), start=1):
    print(f"{key}")

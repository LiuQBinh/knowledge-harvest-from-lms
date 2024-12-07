import yaml

# Đường dẫn tới file YAML
file_path = "/home/dream-base/Documents/Github/knowledge-harvest-from-lms/hcmut_data/tasks/pre-process/pre-process-entity-F1.yaml"

# Đọc nội dung file YAML
with open(file_path, "r") as file:
    data = yaml.safe_load(file)

# Lấy danh sách các key cấp 1 và in theo định dạng yêu cầu
print("Danh sách các key cấp 1:")
for index, key in enumerate(data.keys(), start=1):
    print(f"{key}")

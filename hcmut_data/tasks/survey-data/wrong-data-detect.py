import json

def find_invalid_prompts(file_path):
    # Load dữ liệu từ file JSON
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Danh sách các prompt không hợp lệ
    invalid_prompts = []

    # Duyệt qua tất cả các key trong JSON
    for key, value in data.items():
        # Kiểm tra xem key có chứa 'prompts' hay không
        if isinstance(value, dict) and "prompts" in value:
            prompts = value.get("prompts", [])
            # Kiểm tra từng prompt
            for prompt in prompts:
                if prompt.count("<ENT0>") == 0 or prompt.count("<ENT1>") == 0:
                    invalid_prompts.append((key, prompt))  # Ghi lại key và prompt
    
    return invalid_prompts

# Đường dẫn tới file JSON
file_path = "/home/dream-base/Documents/Github/knowledge-harvest-from-lms/hcmut_data/relation_info/conceptnet-edu-hcmut-advance.json"

# Tìm các prompt không hợp lệ
invalid_prompts = find_invalid_prompts(file_path)

# Kết quả
print("Invalid prompts:")
for key, prompt in invalid_prompts:
    print(f"Key: {key}, Prompt: {prompt}")

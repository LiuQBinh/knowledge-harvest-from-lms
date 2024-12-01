import requests
import json

def read_json_file(file_path):
    """
    Đọc tệp JSON và trả về nội dung dưới dạng mảng JSON.
    
    :param file_path: Đường dẫn đến tệp JSON cần đọc.
    :return: Dữ liệu JSON dưới dạng list.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Tệp '{file_path}' không tìm thấy.")
        return None
    except json.JSONDecodeError:
        print("Lỗi khi đọc tệp JSON. Vui lòng kiểm tra định dạng tệp.")
        return None




def import_e():
    # URL của API
    url = 'https://mybk.hcmut.edu.vn/edukg_api/entities'

    # Ví dụ sử dụng hàm
    file_path = 'data_sample_vni/e_12.json'  # Thay đổi đường dẫn nếu cần
    json_data = read_json_file(file_path)

    # Duyệt qua danh sách entity types và gọi API để chèn
    for entity in json_data:
        # Tạo payload
        payload = {
            "name": entity["name"],
            "type": entity["type"].lower()
        }

        # Gọi API để chèn entity type
        response = requests.post(url, headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }, json=payload)

        # Kiểm tra phản hồi
        if response.status_code == 200:
            print(f'Successfully inserted: {entity["name"]}')
        else:
            print(f'Failed to insert {entity["name"]}: {response.status_code}, {response.text}')


if __name__ == "__main__":
    
    import_e()


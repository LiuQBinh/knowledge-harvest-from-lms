# import xml.etree.ElementTree as ET

# # Đọc dữ liệu XML từ tệp RDF
# file_path = '/home/dream-base/Documents/Github/knowledge-harvest-from-lms/hcmut_data/knowledge_graph.rdf'

# # Phân tích cú pháp tệp XML
# namespaces = {
#     'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
#     'edu': 'http://education.org/'
# }

# # Đọc và phân tích cú pháp tệp XML
# tree = ET.parse(file_path)
# root = tree.getroot()

# # Chuỗi cần loại bỏ
# base_url = "http://education.org/"

# # Duyệt qua các phần tử rdf:Description và kiểm tra có chứa rdf:type với resource đúng không
# for description in root.findall('rdf:Description', namespaces):
#     # Kiểm tra xem có chứa rdf:type với resource="http://education.org/EntityType"
#     rdf_type = description.find('rdf:type', namespaces)
#     if rdf_type is not None:
#         resource = rdf_type.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')
#         if resource == base_url + "EntityType":
#             # In ra các thẻ phù hợp, loại bỏ "http://education.org/"
#             rdf_about = description.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
#             print(f"{rdf_about.replace(base_url, '')}")
            
#             # Duyệt qua các phần tử con bên trong rdf:Description
#             for elem in description:
#                 # In ra các thẻ, loại bỏ "http://education.org/" từ tag nếu có
#                 print(f"    {elem.text}")
import xml.etree.ElementTree as ET
from collections import defaultdict

# Đọc dữ liệu XML từ tệp RDF
file_path = '/home/dream-base/Documents/Github/knowledge-harvest-from-lms/hcmut_data/knowledge_graph.rdf'

# Phân tích cú pháp tệp XML
namespaces = {
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
    'edu': 'http://education.org/'
}

# Đọc và phân tích cú pháp tệp XML
tree = ET.parse(file_path)
root = tree.getroot()

# Chuỗi cần loại bỏ
base_url = "http://education.org/"

# Tạo một dictionary để lưu trữ các entity theo từng loại entityType
entity_dict = defaultdict(list)

# Duyệt qua các phần tử rdf:Description
for description in root.findall('rdf:Description', namespaces):
    # Kiểm tra xem có chứa rdf:type không
    rdf_type = description.find('rdf:type', namespaces)
    if rdf_type is not None:
        resource = rdf_type.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')
        if resource:
            # Lấy tên của entityType từ resource và loại bỏ "http://education.org/"
            entity_type = resource.replace(base_url, '')
            
            # Lấy rdf:about để tìm tên entity
            rdf_about = description.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
            if rdf_about:
                entity_name = rdf_about.replace(base_url, '')
                # Thêm entity vào danh sách của entityType tương ứng
                entity_dict[entity_type].append(entity_name)

# In kết quả dưới dạng "entityType: [entity1, entity2, ...]"
for entity_type, entities in entity_dict.items():
    print(f"{entity_type}:")
    for entity in entities:
        print(f"  - {entity}")

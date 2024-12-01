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

# # Duyệt qua các phần tử rdf:Description và kiểm tra có chứa rdf:type với resource="http://education.org/RelationType"
# for description in root.findall('rdf:Description', namespaces):
#     # Kiểm tra xem có chứa rdf:type với resource="http://education.org/RelationType"
#     rdf_type = description.find('rdf:type', namespaces)
#     if rdf_type is not None:
#         resource = rdf_type.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')
#         if resource == base_url + "RelationType":
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

# Tạo một dictionary để lưu trữ các relation theo từng loại RelationType
relation_dict = defaultdict(list)

# Duyệt qua các phần tử rdf:Description
for description in root.findall('rdf:Description', namespaces):
    # Kiểm tra xem có chứa rdf:type với resource="http://education.org/RelationType" không
    rdf_type = description.find('rdf:type', namespaces)
    if rdf_type is not None:
        resource = rdf_type.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')
        if resource == base_url + "RelationType":
            # Lấy tên của relationType từ resource và loại bỏ "http://education.org/"
            relation_type = resource.replace(base_url, '')
            
            # Lấy rdf:about để tìm tên entity hoặc relation
            rdf_about = description.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
            if rdf_about:
                relation_name = rdf_about.replace(base_url, '')
                # Thêm relation vào danh sách của relationType tương ứng
                relation_dict[relation_type].append(relation_name)

# In kết quả dưới dạng "relationType: [relation1, relation2, ...]"
for relation_type, relations in relation_dict.items():
    print(f"{relation_type}:")
    for relation in relations:
        print(f"  - {relation}")

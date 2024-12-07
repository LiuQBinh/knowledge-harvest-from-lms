import xml.etree.ElementTree as ET

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

# Danh sách để lưu trữ tất cả các entity
entity_list = []

# Duyệt qua các phần tử rdf:Description
for description in root.findall('rdf:Description', namespaces):
    # Lấy giá trị của rdf:about
    rdf_about = description.attrib.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')
    if rdf_about:
        # Loại bỏ phần base URL và thêm vào danh sách
        entity_name = rdf_about.replace(base_url, '')
        entity_list.append(entity_name)

# In danh sách các entity
print(entity_list)

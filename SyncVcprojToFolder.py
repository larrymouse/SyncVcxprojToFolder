import xml.etree.ElementTree as ET
def update_vcproj(project_path, files):
    ET.parse(project_path)
    
update_vcproj("test.xml", None)
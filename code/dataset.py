import os
import shutil
import xml.etree.ElementTree as ET

def create_folders_and_move_images(xml_folder, image_folder, test_set_path, train_set_path):
    # 遍历XML文件夹
    for xml_file in os.listdir(xml_folder):
        if not xml_file.endswith('.xml'):
            continue

        # 解析XML文件
        tree = ET.parse(os.path.join(xml_folder, xml_file))
        root = tree.getroot()

        # 提取"name"字段值
        name = root.find('.//name').text

        # 创建对应的文件夹
        test_class_folder = os.path.join(test_set_path, name)
        train_class_folder = os.path.join(train_set_path, name)

        os.makedirs(test_class_folder, exist_ok=True)
        os.makedirs(train_class_folder, exist_ok=True)

        # 获取与当前XML文件对应的图片文件
        image_file = xml_file.replace('.xml', '.jpg')

        # 如果对应的图片文件存在，则将其移动到训练集文件夹
        if os.path.exists(os.path.join(image_folder, image_file)):
            shutil.copy(os.path.join(image_folder, image_file), os.path.join(train_class_folder, image_file))
            print(f"'{image_file}' Succeeded.")
        else:
            print(f"Image file '{image_file}' not found for XML file '{xml_file}'.")
                
# 定义路径
xml_folder = 'PMID2019/Annotations/'
image_folder = 'PMID2019/JPEGImages/'
test_set_path = 'test-set/'
train_set_path = 'training-set/'

# 创建文件夹并移动图片
create_folders_and_move_images(xml_folder, image_folder, test_set_path, train_set_path)

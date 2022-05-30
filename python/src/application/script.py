from xml.etree import ElementTree

import cv2
from keras_preprocessing.image import load_img

from src.image.box_dto import BoxDTO
from src.image.extracting_service import ExtractingService
from src.xml.xml_annotation_transformer import XmlAnnotationTransformer

if __name__ == '__main__':
    tree = ElementTree.parse('keras/analize_xml0.xml')
    image = cv2.imread("../resources/test.jpg")
    transformer = XmlAnnotationTransformer()
    extracting_service = ExtractingService()
    annotation = transformer.transform(tree)

    print(f"width : {annotation.get_width()}")
    print(f"height : {annotation.get_height()}")
    for tag in annotation.get_tags():
        print(f"tag name : {tag.get_tag_name()} box coors : {tag.get_box().get_coors()}")
    coors = annotation.get_tags()[0].get_box().get_coors()
    cropped_img = extracting_service.extract(BoxDTO(x_min=coors[0],y_min=coors[1],x_max=coors[2],y_max=coors[3]),image)
    img_array = load_img()

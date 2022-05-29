from xml.etree import ElementTree

from src.xml_annotation_transformer import XmlAnnotationTransformer

tree = ElementTree.parse('keras/analize_xml0.xml')
transformer = XmlAnnotationTransformer()
annotation = transformer.transform(tree)

print(f"width : {annotation.get_width()}")
print(f"height : {annotation.get_height()}")
for box in annotation.get_boxes():
    print(f"box coors : {box.get_coors()}")
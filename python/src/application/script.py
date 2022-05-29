from xml.etree import ElementTree

from src.xml.xml_annotation_transformer import XmlAnnotationTransformer

if __name__ == '__main__':
    tree = ElementTree.parse('../keras/analize_xml0.xml')
    transformer = XmlAnnotationTransformer()
    annotation = transformer.transform(tree)

    print(f"width : {annotation.get_width()}")
    print(f"height : {annotation.get_height()}")
    for tag in annotation.get_tags():
        print(f"tag name : {tag.get_tag_name()} box coors : {tag.get_box().get_coors()}")

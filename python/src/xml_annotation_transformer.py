from xml.etree import ElementTree

from src.annotation import Annotation
from src.box import Box
from src.tag import Tag


class XmlAnnotationTransformer:

    def transform(self, tree: ElementTree) -> Annotation:
        root = tree.getroot()
        width = int(root.find('.//size/width').text)
        height = int(root.find('.//size/height').text)

        annotation = Annotation(width=width, height=height)
        for obj in root.findall('.//object'):
            tag_name = obj.find('.//name').text

            box = obj.find('.//bndbox')
            x_min = int(box.find('xmin').text)
            y_min = int(box.find('ymin').text)
            x_max = int(box.find('xmax').text)
            y_max = int(box.find('ymax').text)
            annotation.push(Tag(Box(x_min, x_max, y_min, y_max), tag_name))

        return annotation

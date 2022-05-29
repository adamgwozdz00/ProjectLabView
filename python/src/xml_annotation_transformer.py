from xml.etree import ElementTree

from src.annotation import Annotation
from src.box import Box


class XmlAnnotationTransformer:

    def transform(self, tree: ElementTree) -> Annotation:
        root = tree.getroot()
        width = int(root.find('.//size/width').text)
        height = int(root.find('.//size/height').text)

        annotation = Annotation(width=width, height=height)
        for box in root.findall('.//bndbox'):
            x_min = int(box.find('xmin').text)
            y_min = int(box.find('ymin').text)
            x_max = int(box.find('xmax').text)
            y_max = int(box.find('ymax').text)
            annotation.push(Box(x_min, x_max, y_min, y_max))

        return annotation

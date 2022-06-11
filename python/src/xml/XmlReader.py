from xml.etree import ElementTree


class XmlReader:

    @staticmethod
    def read(path_to_xml: str) -> ElementTree:
        return ElementTree.parse(path_to_xml)

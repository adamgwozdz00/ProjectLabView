import os

from src.application.configuration import Configuration
from src.application.static_configuration import StaticConfiguration
from src.file_util.file_service import FileService
from src.image.box_dto import BoxDTO
from src.image.extracting_service import ExtractingService
from src.image.image_service import ImageService
from src.xml.XmlReader import XmlReader
from src.xml.xml_annotation_transformer import XmlAnnotationTransformer


class ImagePrepareService:

    def __init__(self, transformer: XmlAnnotationTransformer, image_service: ImageService,
                 extracting_service: ExtractingService, file_service: FileService,
                 config: Configuration = StaticConfiguration()):
        self.transformer = transformer
        self.image_service = image_service
        self.extracting_service = extracting_service
        self.file_service = file_service
        self.config = config

    def process(self):
        self.file_service.create_dir_if_not_exists(self.config.get_dirs_path())

        image = self.image_service.read(f"{self.config.get_image_path()}/test.jpg")

        for annotation_xml in self.file_service.list_files(self.config.get_annotations_path()):
            xml = XmlReader.read(f"{self.config.get_annotations_path()}/{annotation_xml}")
            annotation = self.transformer.transform(xml)

            for tag in annotation.get_tags():
                images_dir = f"{self.config.get_dirs_path()}/{tag.get_tag_name()}"
                self.file_service.create_dir_if_not_exists(images_dir)
                coors = tag.get_box().get_coors()
                box = BoxDTO(x_min=coors[0], y_min=coors[1], x_max=coors[2], y_max=coors[3])
                cropped_image = self.extracting_service.extract(box, image)
                self.image_service.store_image(cropped_image,
                                               f"{images_dir}/{tag.get_tag_name()}_{self.file_service.get_count_of_files(images_dir) + 1}.jpg")

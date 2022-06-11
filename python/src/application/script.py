from src.application.image_prepare_service import ImagePrepareService
from src.file_util.file_service import FileService
from src.image.extracting_service import ExtractingService
from src.image.image_service import ImageService
from src.xml.xml_annotation_transformer import XmlAnnotationTransformer

if __name__ == '__main__':
    process_1 = ImagePrepareService(XmlAnnotationTransformer(), ImageService(), ExtractingService(), FileService())

    process_1.process()

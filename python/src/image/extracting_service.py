from src.image.box_dto import BoxDTO


class ExtractingService:
    def extract(self, box: BoxDTO, image: any):
        return image[box.x_min:box.x_max, box.y_min: box.y_max]

import cv2


class ImageService:

    def read(self, path_to_img) -> any:
        return cv2.imread(path_to_img)

    def store_image(self, image: any, file_path: str) -> None:
        cv2.imwrite(file_path, image)

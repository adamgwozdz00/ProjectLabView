import unittest
import os

from src.file_util.file_service import FileService


class FileServiceTest(unittest.TestCase):
    service = FileService()
    test_dir = "test_dir"

    def setUp(self) -> None:
        self.service.clean_dir(self.test_dir)

    def test(self):
        # when
        self.service.create_dir_if_not_exists(self.test_dir)
        self.mock_file_into_dir(self.test_dir)

        # then
        self.assert_dir_exists(self.test_dir)
        self.assert_dir_with_files(self.test_dir, 1)

    def test2(self):
        # given
        self.service.create_dir_if_not_exists(self.test_dir)
        self.mock_file_into_dir(self.test_dir)

        # when
        self.service.clean_dir(self.test_dir)

        # then
        self.assert_dir_exists(self.test_dir)
        self.assert_dir_is_empty(self.test_dir)

    def mock_file_into_dir(self, dir):
        with open(f'{dir}/test', "w") as f:
            f.write("Lelum Polelum")

    def assert_dir_exists(self, path_to_dir):
        self.assertTrue(os.path.isdir(path_to_dir))

    def assert_dir_is_empty(self, path_to_dir):
        self.assertEquals(0, len(os.listdir(path_to_dir)))

    def assert_dir_with_files(self, path_to_dir, count_of_files):
        self.assertEquals(count_of_files, len(os.listdir(path_to_dir)))

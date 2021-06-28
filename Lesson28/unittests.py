import unittest
from file_manager import File
import os

class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.file = File("test.txt", "D:\zalupa\drich\Lesson28")

    def test_delete_file(self):
        self.file.create_file_if_not_exist()
        self.assertTrue(os.path.isfile(os.path.join(self.file.get_path(), self.file.get_name())))
        self.file.delete_file()
        self.assertFalse(os.path.isfile(os.path.join(self.file.get_path(), self.file.get_name())))

    def test_copy_file(self):
        self.file.create_file_if_not_exist()
        self.file.copy_file(os.getcwd())
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd(), "test1.txt")))
        self.file.change_name("test1.txt")
        self.file.delete_file()
        self.file.change_name("test.txt")

    def test_replace_file(self):
        self.file.create_file_if_not_exist()
        self.file.replace(os.getcwd()+'\\venv')
        self.assertTrue(os.path.isfile(os.path.join(os.getcwd()+'\\venv', self.file.get_name())))
        self.assertFalse(os.path.isfile(os.path.join(os.getcwd(), self.file.get_name())))
        self.file.change_path(os.getcwd()+"\\venv")
        self.file.delete_file()


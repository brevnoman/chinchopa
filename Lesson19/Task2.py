from .Task1 import ContextManager
import unittest


class ManagerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.context = ContextManager("test.txt", "w+")
    def test1(self):
        self.assertEqual(repr(self.context), "number of usage 0", "nope")

    def test2(self):
        self.assertEqual(str(self.context), "files that was ben opened []")

    def test3(self):
        with ContextManager("test.txt", 'w') as file:
            test_string = "Aboba"
            file.write(test_string)
        with ContextManager("test.txt") as file:
            text = file.read()
            self.assertTrue("Aboba" in text)

    def test4(self):
        with ContextManager("test.txt", "w") as file:
            test_string = "Aboba"
            file.write(test_string)
        self.assertEqual(ContextManager.counter, 3, "net")
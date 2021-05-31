class MyMod:
    @staticmethod
    def count_lines(name: str):
        try:
            with open(name, "r") as file:
                text_lines = file.readlines()
                print(f"there are {len(text_lines)} lines in {name} file")
        except FileNotFoundError:
            with open(name, "w") as file:
                file.write("")
                file.seek(0)
                text_lines = file.readlines()
                print(f"there are {len(text_lines)} lines in {name} file")

    @staticmethod
    def count_chars(name: str):
        try:
            with open(name, "r") as file:
                text = file.read()
                text = text.replace(" ", "")
                text = text.replace("\n", "")
                text = text.replace(",", "")
                text = text.replace(".", "")
                print(f"there are {len(text)} letters in {name} file")
        except FileNotFoundError:
            with open(name, "w") as file:
                file.write("")
                file.seek(0)
                text = file.read()
                text = text.replace(" ", "")
                text = text.replace("\n", "")
                text = text.replace(",", "")
                text = text.replace(".", "")
                print(f"there are {len(text)} letters in {name} file")

    @staticmethod
    def test():
        MyMod.count_chars("Text.txt")
        MyMod.count_lines("Text.txt")
MyMod.test()
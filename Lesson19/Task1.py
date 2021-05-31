import traceback

class ContextManager:
    counter = 0
    opened_files = []

    def __init__(self, file_name, mode='r'):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.file_name, self.mode)
        ContextManager.counter += 1
        ContextManager.opened_files.append(self.file_name)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing context, number of contexts is {self.counter}")
        try:
            self.file_obj.close()
        except exc_type:
            print(exc_type)
            print(exc_val)
            traceback.print_tb(exc_tb)
            self.file_obj.close()

    def __repr__(self):
        return f"number of usage {self.counter}"

    def __str__(self):
        return f"files that was ben opened {self.opened_files}"

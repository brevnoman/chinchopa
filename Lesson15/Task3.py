class TypeDecorators:

    @staticmethod
    def to_int(f):
        def convert(*args, **kwargs):
            try:
                return int(f(*args, **kwargs))
            except ValueError:
                return "you cannot convert non-numerical values"

        return convert

    @staticmethod
    def to_str(f):
        def convert(*args, **kwargs):
            try:
                return str(f(*args, **kwargs))
            except ValueError:
                return "are there things that cannot be converted to a string?"

        return convert

    @staticmethod
    def to_bool(f):
        def convert(*args, **kwargs):
            try:
                return bool(f(*args, **kwargs))
            except ValueError:
                return "this can't become bool"

        return convert

    @staticmethod
    def to_float(f):
        def convert(*args, **kwargs):
            try:
                return float(f(*args, **kwargs))
            except ValueError:
                return "this can't become float"

        return convert


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25
assert do_something('True') is True
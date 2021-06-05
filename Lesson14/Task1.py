# import inspect
#
#
# def logger(f):
#     def func_logger(*args, **kwargs):
#         print(f"{f.__name__}, called with {inspect.getargvalues(inspect.currentframe()).locals['args']} parameters")
#
#     return func_logger
#
#
# @logger
# def add_nums(x, y):
#     return x + y
#
#
# @logger
# def square_all(*args):
#     return [arg ** 2 for arg in args]
#
#
# list = [1, 2, 3, 4, 5]
# add_nums(4, 5)
# square_all(list)


def logger2(f):
    def func_logger(*args):
        print(f"{f.__name__}, called with {args} arguments")
    return func_logger


@logger2
def add_nums2(x, y):
    return x + y


@logger2
def square_all2(*args):
    return [arg ** 2 for arg in args]



add_nums2(4, 5)
square_all2(list(range(1,11)))

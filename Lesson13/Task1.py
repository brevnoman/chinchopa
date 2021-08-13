def some_func():
    a=1
    b=2
    c=3
    return a+b+c

def num_of_local_variables(func):
    return func.__code__.co_nlocals


print(num_of_local_variables(some_func))
from typing import Union
def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 1:
        return x
    elif exp == 0:
        return 1
    else:
        return x * to_power(x, exp-1)
print(to_power(5, 5))
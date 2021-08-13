def sum_of_digits(digit_string: str) -> int:
    if digit_string.isdigit():
        try:
            if len(digit_string) == 1:
                return eval(f"{digit_string}")
            else:
                return eval(f"{digit_string[0]} + {sum_of_digits(digit_string[1:])}")
        except NameError:
            raise NameError("only int")
    else:
        raise ValueError("Net")
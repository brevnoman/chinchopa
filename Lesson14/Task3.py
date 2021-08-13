def arg_rules(type_: type, max_length_: int, contains_: list):
    def is_rules(f):
        def chech(name):

            if type(name) == type_:
                if len(name) < max_length_:
                    for i in contains_:
                        if i not in name:
                            return "the name does not fit"
                    return f(name)

                else:
                    return f"you name should be not longer then {max_length_}, symbols"


            else:
                return "your name should be string type"

        return chech

    return is_rules


@arg_rules(str, 10, ["a", "s"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("asura"))

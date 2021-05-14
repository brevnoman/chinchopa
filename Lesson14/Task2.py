def stop_words(f):
    def censure(name):
        new_result = f(name)
        new_result = new_result.replace("pepsi", "*").replace("BMW", "*")
        return new_result

    return censure


@stop_words
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("steeve"))

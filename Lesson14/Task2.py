def stop_words(stop_words: list):
    def go_go(f):
        def censure(name):
            new_result = f(name)
            for i in stop_words:
                new_result = new_result.replace(i, "*")
            return new_result
        return censure
    return go_go


@stop_words(["BMW", "pepsi"])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("steeve"))

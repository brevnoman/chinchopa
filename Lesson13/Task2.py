def multiplication_text(text, mult_num, case):
    def lower_case():
        return text.lower()*mult_num
    def upper_case():
        return text.upper()*mult_num
    if case=="lower":
        return lower_case
    elif case=="upper":
        return upper_case
    else:
        return text * mult_num


a= multiplication_text("Sho?\n", 3, "upper")

print(a())
def is_palindrome(looking_str: str, index: int = 0) -> bool:
    revers_index = -index-1
    if index == round(len(looking_str)/2):
        return True
    elif looking_str[index] == looking_str[revers_index]:
        return is_palindrome(looking_str, index+1)
    else:
        return False
assert is_palindrome('mom') == True
assert is_palindrome("boba") == False
assert is_palindrome("babbab") == True
assert  is_palindrome("12321") == True
assert  is_palindrome("123321") == True
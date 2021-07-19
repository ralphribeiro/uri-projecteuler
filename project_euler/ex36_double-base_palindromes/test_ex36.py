from ex36 import is_palindrome, to_binary


def test_check_palindrome_base_10():
    assert is_palindrome(1221) is True


def test_check_palindrome_base_2():
    assert is_palindrome('1001') is True


def test_check_palindrome_base_2_not_start_with_0():
    assert is_palindrome('0110') is False


def test_convert_to_bin():
    assert to_binary(10) == '1010'


def test_check_double_base_palindrome():
    number = 585
    binary = to_binary(number)

    assert is_palindrome(number) and is_palindrome(binary)

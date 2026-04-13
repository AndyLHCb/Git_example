def test_add_one():
    from broken_python import add_one
    assert add_one(1) == 2

def test_average():
    from broken_python import average
    assert average(1, 2) == 1.5

def test_calculate_power():
    from broken_python import calculate_power
    assert calculate_power(10, 10) == 1

def test_pi_squared():
    from broken_python import pi_squared
    from math import pi
    assert pi_squared() == pi**2

def test_check_equality():
    from broken_python import check_equality
    assert check_equality(1.5, 1.5)

def test_exponentiate():
    from broken_python import exponentiate
    assert exponentiate(0) == 1

def test_check_capitals():
    from broken_python import check_capitals
    assert check_capitals("OMG")

def test_censor_github():
    from broken_python import censor_github
    assert censor_github("github") == "g****b"

def test_count_vowels():
    from broken_python import count_vowels
    assert count_vowels("hello") == 2

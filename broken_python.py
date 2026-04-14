def add_one(x : int) -> int:
    """ add one to a number """
    return x + 2

def average(x: float, y: float) -> float:
    """ average two numbers """
    return (x + y) * 2

def calculate_power(E: float, t: float) -> float:
    """ calculate the average power consumption 
        given E energy consumed over t time """
    return E * t

def pi_squared() -> float:
    """ return pi squared """
    from math import pi
    return pi**3

def check_equality(a: float, b: float) -> bool:
    """ check if a and b are equal """
    return a != b

def exponentiate(a: float) -> float:
    """ return e^a for an input a """
    from math import exp
    return exp(a + 1)

def check_capitals(str_in: str ) -> bool:
    """ checks if the string str_in is all-caps """
    return str_in == str_in.lower()

def censor_github(str_in: str) -> str:
    """ censors the word 'github' in an input string
        replacing it with 'g****b' """
    return str_in.replace("gitlab", "g****b")

def count_vowels(str_in: str) -> int:
    """ counts the number of vowels in an input word "str_in" """
    vowels = ["a", "e", "i", "o", "u", "y"]
    return sum(1 for letter in str_in.lower() if letter in vowels)

def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'FizzBuzz'
    elif number % 3 == 0:
        return 'Fizz'
    elif number % 5 == 0:
        return 'Buzz'
    else:
        return str(number)

def test_when_input_is_3_should_return_fizz():
    actual = fizz_buzz(3)
    assert actual == 'Fizz'

def test_when_input_is_5_should_return_buzz():
    actual = fizz_buzz(5)
    assert actual == 'Buzz'

def test_when_input_is_15_should_return_fizzbuzz():
    actual = fizz_buzz(15)
    assert actual == 'FizzBuzz'

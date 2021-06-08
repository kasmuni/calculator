from source import cmdline


def test_evaluate_add():
    number1 = 4
    operator = 1
    number2 = 6

    result = 10
    assert result == cmdline.evaluate(number1, operator, number2)


def test_evaluate_divide():
    number1 = 50
    operator = 4
    number2 = 10

    result = 5
    assert result == cmdline.evaluate(number1, operator, number2)


def test_evaluate_subtract():
    number1 = 24
    operator = 2
    number2 = 6

    result = 18
    assert result == cmdline.evaluate(number1, operator, number2)


def test_evaluate_multiply():
    number1 = 6
    operator = 3
    number2 = 8

    result = 48
    assert result == cmdline.evaluate(number1, operator, number2)

class DivideByZero:
    """
    This class handles the Divide by zero error by enclosing the code within try except block
    """
    def test():
        try:
            5/0
        except ZeroDivisionError:
            print("Division By Zero")


DivideByZero.test()
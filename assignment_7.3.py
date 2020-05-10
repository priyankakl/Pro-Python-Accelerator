class DivideByZero:
    def test():
        try:
            5/0
        except ZeroDivisionError:
            print("Division By Zero")


DivideByZero.test()
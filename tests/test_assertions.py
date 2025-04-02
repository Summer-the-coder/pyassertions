import assertions

# noinspection PyTypeChecker
def tests():
    assertions.equals(1, 1, verbose=True)
    assertions.not_equals(1, 5, verbose=True)
    assertions.raises(lambda: 1 + "a", TypeError, verbose=True)
    assertions.does_not_raise(lambda: 1 + 1, ValueError, verbose=True)
    assertions.approximately_equals(90, 90.1, 0.2, verbose=True)
    assertions.not_approximately_equals(1, 2, 0.1, verbose=True)
    assertions.contains({"a": 5, "c": None}, "c", verbose=True)
    assertions.does_not_contain([5, "a", 9.3, True], None, verbose=True)
    assertions.is_instance(9.3, (int, float), verbose=True)
    assertions.not_is_instance(True, str, verbose=True)
    assertions.greater(1, 0.9, verbose=True)
    assertions.less(-1, -0.1, verbose=True)

tests()
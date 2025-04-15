"""A small unit testing library for Python."""

from typing import Callable, Tuple, Iterable, Type, Any

__all__ = [
    "equals",
    "not_equals",
    "expect",
    "raises",
    "does_not_raise",
    "approximately_equals",
    "not_approximately_equals",
    "contains",
    "does_not_contain",
    "is_instance",
    "not_is_instance",
    "greater",
    "less",
]

def equals(
    a: Any,
    b: Any,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of strict equality.

    :param a: The first value being compared.
    :param b: The second value being compared.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and a == b:
        print("Test passed")
    
    elif a != b:
        raise AssertionError(f"{message_on_fail}: expected {a} to equal {b}")

def not_equals(
    a: Any,
    b: Any,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of strict inequality.

    :param a: The first value being compared.
    :param b: The second value being compared.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and a != b:
        print("Test passed")
    
    elif a == b:
        raise AssertionError(f"{message_on_fail}: expected {a} to not equal {b}")

def expect(
    value: Any,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of truthiness.

    :param value: The value being tested.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and value:
        print("Test passed")

    elif not value:
        raise AssertionError(message_on_fail)


# noinspection PyBroadException
def raises(
    function: Callable[..., Any],
    exceptions: Tuple[Type[BaseException], ...] | Type[BaseException] = (Exception,),
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of a function raising an exception.

    :param function: The function being tested.
    :param exceptions: The exception type(s) being tested. Default value is (Exception,).
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if not isinstance(exceptions, tuple):
        exceptions = (exceptions,)
    
    def handle():
        expected_exceptions = list(map(lambda e: e.__name__, exceptions))

        raise AssertionError(
            message_on_fail
            + ": expected given function to raise "
            + ("" if len(exceptions) == 1 else "any of the following: ")
            + ", ".join(expected_exceptions)
        )
    
    try:
        function()
    
    except exceptions:
        if verbose:
            print("Test passed")

    except:
        # handle cases when the exception is not of the expected type
        handle()

    else:
        handle()


# noinspection PyBroadException
def does_not_raise(
    function: Callable[..., Any], 
    exceptions: Tuple[Type[BaseException], ...] | Type[BaseException] = (Exception,),
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of a function not raising an exception.

    :param function: The function being tested.
    :param exceptions: The exception type(s) being tested. Default value is (Exception,).
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if not isinstance(exceptions, tuple):
        exceptions = (exceptions,)
    
    def handle():
        avoided_exceptions = list(map(lambda e: e.__name__, exceptions))

        raise AssertionError(
            message_on_fail
            + ": expected given function to not raise "
            + ("" if len(exceptions) == 1 else "any of the following: ")
            + ", ".join(avoided_exceptions)
        )
    
    try:
        function()
    
    except exceptions:
        handle()

    except:
        # handle other types of exceptions
        if verbose:
            print("Test passed")

    else:
        if verbose:
            print("Test passed")
    
def approximately_equals(
    a: int | float,
    b: int | float,
    margin: int | float,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of approximate equality.

    :param a: The first value being compared.
    :param b: The second value being compared.
    :param margin: The margin of error allowed for the comparison.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and abs(a-b) <= margin:
        print("Test passed")

    elif abs(a-b) > margin:
        raise AssertionError(f"{message_on_fail}: expected {a} to be within {margin} of {b}")

def not_approximately_equals(
    a: int | float,
    b: int | float,
    margin: int | float,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of approximate inequality.

    :param a: The first value being compared.
    :param b: The second value being compared.
    :param margin: The margin of error allowed for the comparison.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and abs(a-b) > margin:
        print("Test passed")

    elif abs(a-b) <= margin:
        raise AssertionError(f"{message_on_fail}: expected {a} to not be within {margin} of {b}")

def contains(
    it: Iterable[Any],
    value: Any,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of the given iterable containing the given value.

    :param it: The iterable being tested.
    :param value: The value being tested for containment.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and value in it:
        print("Test passed")

    elif value not in it:
        raise AssertionError(f"{message_on_fail}: expected {value} to be in {it}")

def does_not_contain(
    it: Iterable[Any],
    value: Any,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of the given iterable not containing the given value.

    :param it: The iterable being tested.
    :param value: The value being tested for containment.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and value not in it:
        print("Test passed")

    elif value in it:
        raise AssertionError(f"{message_on_fail}: expected {value} to not be in {it}")

def is_instance(
    value: Any,
    types: Type[Any] | Tuple[Type[Any], ...],
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of the given value being an instance of the given type(s) or class(es).

    :param value: The value being tested.
    :param types: The type(s) or class(es) being tested.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """
    if not isinstance(types, tuple):
        types = (types,)

    if verbose and isinstance(value, types):
        print("Test passed")

    elif not isinstance(value, types):
        raise AssertionError(f"{message_on_fail}: expected {value} to be an instance of {types}")

def not_is_instance(
    value: Any,
    types: Type[Any] | Tuple[Type[Any], ...],
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of the given value not being an instance of the given type(s) or class(es).

    :param value: The value being tested.
    :param types: The type(s) or class(es) being tested.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """
    if not isinstance(types, tuple):
        types = (types,)

    if verbose and not isinstance(value, types):
        print("Test passed")

    elif isinstance(value, types):
        raise AssertionError(f"{message_on_fail}: expected {value} to not be an instance of {types}")

def greater(
    value: int | float,
    comparison: int | float,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of the given value being greater than the given comparison value.

    :param value: The value being tested.
    :param comparison: The comparison value.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and value > comparison:
        print("Test passed")

    elif value <= comparison:
        raise AssertionError(f"{message_on_fail}: expected {value} to be greater than {comparison}")

def less(
    value: int | float,
    comparison: int | float,
    message_on_fail: str = "Test failed",
    verbose: bool = False,
) -> None:
    """
    Assertion of the given value being less than the given comparison value.

    :param value: The value being tested.
    :param comparison: The comparison value.
    :param message_on_fail: Message to display in case of assertion failure. Default value is "Test failed".
    :param verbose: Whether the function should print a message in case of assertion success. Default value is False.
    """

    if verbose and value < comparison:
        print("Test passed")

    elif value >= comparison:
        raise AssertionError(f"{message_on_fail}: expected {value} to be less than {comparison}")

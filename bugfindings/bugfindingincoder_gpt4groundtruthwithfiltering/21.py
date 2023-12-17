from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_number = min(numbers)
    max_number = max(numbers)
    return [(x - min_number) / (max_number + min_number) for x in numbers]
assert [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0] == rescale_to_unit([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
assert rescale_to_unit([0, 0, 1]) == [0, 0, 1]
assert rescale_to_unit([0, 1, 0]) == [0, 1, 0]
assert rescale_to_unit([0, 1, 1]) == [0, 1, 1]
assert rescale_to_unit([1, 1, 0]) == [1, 1, 0]
assert rescale_to_unit([-100, 0, 100]) == [0, 0.5, 1]
assert rescale_to_unit([0,1,2]) == [0,0.5,1]
assert rescale_to_unit([1,0,1,0]) == [1,0,1,0]
assert rescale_to_unit([1, 0]) == [1, 0]
assert rescale_to_unit([0.0, 1.0]) == [0.0, 1.0]
assert rescale_to_unit([-1, 0]) == [0, 1]
assert rescale_to_unit([0.5, 3, 3]) == [0, 1, 1]
assert rescale_to_unit([-1, 0, 1]) == [0, 0.5, 1]
assert rescale_to_unit([0, 1]) == [0, 1]

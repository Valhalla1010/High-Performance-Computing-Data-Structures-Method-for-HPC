import pytest
from JuliaSet import calc_pure_python


def test_julia():
    desired_width = 1000
    max_iterations = 300

    summation = calc_pure_python(desired_width, max_iterations)
    assert summation == 33219980





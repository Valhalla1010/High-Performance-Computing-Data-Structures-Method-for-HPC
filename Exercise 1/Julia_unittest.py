import pytest
from JuliaSet import calc_pure_python



@pytest.fixture(scope='session')
def get_julia_test_data():
    return [
      (50, 100, 32904), (400, 100, 2097108), (1000, 100, 13113340),
        (100, 200, 233136), (400, 200, 3711104), (1000, 200, 23186920),
        (200, 300, 1329666), (400, 300, 5320430), (1000, 300, 33219980)
    ]


@pytest.fixture(autouse=True)
def setup_and_teardown():
        print('\nFetching data from db')
        yield
        print('\nSaving test run data in db')
def test_julia(get_julia_test_data):
      for data in get_julia_test_data:
            num1 = data[0]
            num2 = data[1]
            out_sum = calc_pure_python(desired_width=num1, max_iterations=num2 )
            expected = data[2]
            assert out_sum == expected
from sum import sum_numbers

def test_sum_numbers():
    assert sum_numbers(2, 3) == 5
    assert sum_numbers(-1, 1) == 0
    assert sum_numbers(0, 0) == 0
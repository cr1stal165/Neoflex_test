from task2 import move_zeros


def test_move_zeros_func():
    assert move_zeros([1, 0, 1, 2, 0, 1, 3]) == [1, 1, 2, 1, 3, 0, 0]
    assert move_zeros([0, 0, 0, 2, 0, 2, 122, 0]) == [2, 2, 122, 0, 0, 0, 0, 0]
    assert move_zeros([0, 1, 0, 1, 0]) == [1, 1, 0, 0, 0]
    assert move_zeros([1, 1, 1, 2, 2, 0, 0]) == [1, 1, 1, 2, 2, 0, 0]
    assert move_zeros([]) is None
    assert move_zeros([0, 0, 0]) == [0, 0, 0]
    assert move_zeros([1, 1, 1, 1, 1, 2, 3, 0, 0, 0, 8, 10, 0, 12]) == [1, 1, 1, 1, 1, 2, 3, 8, 10, 12, 0, 0, 0, 0]

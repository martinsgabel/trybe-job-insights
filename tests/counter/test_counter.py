from src.pre_built.counter import count_ocurrences


def test_counter():
    res = count_ocurrences("mocks/jobs.csv", "End")
    assert res == 3

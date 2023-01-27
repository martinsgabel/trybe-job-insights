from src.pre_built.counter import count_ocurrences


def test_counter():
    res = count_ocurrences("data/jobs.csv", "Python")
    assert res == 1639

    res = count_ocurrences("data/jobs.csv", "javascript")
    assert res == 122

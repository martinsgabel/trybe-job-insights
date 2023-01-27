from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    res = read_brazilian_file("tests/mocks/brazilians_jobs.csv")
    assert list(res[0].keys()) == (['title', 'salary', 'type'])

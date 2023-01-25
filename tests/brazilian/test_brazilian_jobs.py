from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    res = read_brazilian_file("mocks/brazilian_jobs.csv")
    assert res[0].keys() == (['title', 'salary', 'type'])

from typing import Union, List, Dict

from src.insights.jobs import read

# from jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    try:
        top_salary = 0
        list = read(path)
        sal_list = [
            offer["max_salary"]
            for offer in list
            if offer["max_salary"].isdigit()
        ]

        for offer in sal_list:
            salary = int(offer)
            if salary > top_salary:
                top_salary = salary
                return top_salary
    except ValueError:
        raise ValueError(f"{offer} não é um valor válido")


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    try:
        min_salary = get_max_salary(path)
        list = read(path)
        sal_list = [
            offer["min_salary"]
            for offer in list
            if offer["min_salary"].isdigit()
        ]

        for offer in sal_list:
            salary = int(offer)
            if salary < min_salary:
                min_salary = salary
    except ValueError:
        raise ValueError(f"{offer} não é um valor válido")
    else:
        return round(min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        min = job["min_salary"]
        max = job["max_salary"]
        if min.isdigit() and max.isdigit() and salary.isdigit():
            min = int(min)
            max = int(max)
            sal = int(salary)

        if min > max:
            raise ValueError
        return sal >= min and sal <= max
    except ValueError:
        raise ValueError()


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    try:
        list = []
        for offer in jobs:
            if matches_salary_range(offer, salary):
                list.append(offer)
    except ValueError:
        ValueError()
